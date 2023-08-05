'''
A GlycoCT (Condensed) parser.
Supports RES, LIN, and un-nested REP sections.

.. code-block:: python

    >>>from glypy.io import glycoct
    >>>glycoct.loads("""RES
    1b:o-dman-HEX-0:0|1:aldi
    2b:a-lido-HEX-1:5|6:a
    3s:sulfate
    LIN
    1:1o(3+1)2d
    2:2o(2+1)3n
    3:2o(4+1)4d
    """)
    >>>
'''

import re
import warnings
from collections import defaultdict, Counter, deque
from functools import cmp_to_key

from glypy.utils import opener, StringIO, enum, root as rootp, tree as treep, make_counter, invert_dict
from glypy.utils.multimap import OrderedMultiMap
from glypy.structure import monosaccharide, substituent, link, glycan
from .format_constants_map import (anomer_map, superclass_map,
                                   link_replacement_composition_map, modification_map)
from .file_utils import ParserError
from glypy.composition import Composition

try:
    range = xrange
except NameError:
    pass


__id = id

Glycan = glycan.Glycan
Monosaccharide = monosaccharide.Monosaccharide
Substituent = substituent.Substituent
Link = link.Link
AmbiguousLink = link.AmbiguousLink

START = "!START"
REPINNER = "!REPINNER"
RES = "RES"
LIN = "LIN"
REP = "REP"
ALT = "ALT"
UND = "UND"
ISO = "ISO"
NON = "NON"

TERMINAL_STATES = {
    RES,
    LIN,
    ISO,
    NON
}

subsituent_start = "s"
base_start = "b"
repeat_start = "r"
alternative_start = "a"

#: Pattern for parsing the lines of the RES section corresponding
#: to individual |Monosaccharide| residues
res_pattern = re.compile(
    '''
    (?P<anomer>[abxo])?
    (?P<conf_stem>(?:-[dlx][a-z]+)+)?-?
    (?P<superclass>[A-Z]+)-?
    (?P<indices>[0-9x]+:[0-9x]+)
    (?P<modifications>(\|[0-9x]+:[0-9a-z]+)+)?
    ''', re.VERBOSE)

#: Pattern for parsing the potentially repeated |Configuration| and |Stem|
#: regions of the lines of the RES section.
conf_stem_pattern = re.compile(r'(?P<config>[dlx])(?P<stem>[a-z]+)')

#: Pattern for parsing modifications found on monosaccharide residue
#: lines in the RES section
modification_pattern = re.compile(r"\|?(\d+):([^\|;\n]+)")


#: Pattern for parsing |Link| lines found in the LIN section
link_pattern = re.compile(
    r'''(?P<doc_index>\d+)?:
    (?P<parent_residue_index>\d+)
    (?P<parent_atom_replaced>[odhnx])
    \((?P<parent_attachment_position>-?[0-9\-\|]+)[\+\-]
        (?P<child_attachment_position>-?[0-9\-\|]+)\)
    (?P<child_residue_index>\d+)
    (?P<child_atom_replaced>[odhnx])
        ''', re.VERBOSE)


#: Special truncation of the :data:`link_pattern` which is used on
#: REP header sections
internal_link_pattern = re.compile(
    r'''(?P<parent_residue_index>\d+)
    (?P<parent_atom_replaced>[odhnx])
    \((?P<parent_attachment_position>-?[0-9\-\|]+)[\+\-]
        (?P<child_attachment_position>-?[0-9\-\|]+)\)
    (?P<child_residue_index>\d+)
    (?P<child_atom_replaced>[odhnx])
    ''',
    re.VERBOSE)

#: Pattern for interpreting the REP# instance header section
rep_header_pattern = re.compile(
    r'''REP(?P<repeat_index>\d+):
    (?P<internal_linkage>.+)
    =(?P<lower_multitude>-?\d+)-(?P<higher_multitude>-?\d+)''', re.VERBOSE)

repeat_line_pattern = re.compile("^(?P<graph_index>\d+)r:r(?P<repeat_index>\d+)")


def parse_link(line):
    link_dict = link_pattern.search(line)
    if link_dict is not None:
        link_dict = link_dict.groupdict()
    else:
        raise GlycoCTError("Could not interpret link", line)
    id = link_dict['doc_index']
    parent_residue_index = int(link_dict['parent_residue_index'])
    child_residue_index = int(link_dict['child_residue_index'])

    parent_atom_replaced = link_replacement_composition_map[link_dict["parent_atom_replaced"]]
    parent_attachment_position = list(map(int, link_dict["parent_attachment_position"].split("|")))

    child_atom_replaced = link_replacement_composition_map[link_dict["child_atom_replaced"]]
    child_attachment_position = list(map(int, link_dict["child_attachment_position"].split("|")))

    return (id, parent_residue_index, parent_atom_replaced, parent_attachment_position,
            child_residue_index, child_atom_replaced, child_attachment_position)


def form_link(parent, child, parent_position, child_position, parent_loss, child_loss, id=None):
    if parent.node_type is Substituent.node_type and\
            child.node_type is Monosaccharide.node_type:
        warnings.warn(
            "A monosaccharide with a substituent parent has been detected. "
            "These structures are not fully supported and may not traverse as expected "
            "by default.", stacklevel=7)
    if len(parent_position) > 1 or len(child_position) > 1:
        ambilink = AmbiguousLink(parent, child,
                                 parent_position=list(map(int, parent_position)),
                                 child_position=list(map(int, child_position)),
                                 parent_loss=parent_loss, child_loss=child_loss, id=id)
        ambilink.find_open_position()
    else:
        Link(parent, child, parent_position=int(parent_position[0]),
             child_position=int(child_position[0]),
             parent_loss=parent_loss, child_loss=child_loss)


class StructurePrecisionEnum(enum.Enum):
    unknown = -1
    ranging = 1
    exact = 2


def decorate_tree(tree, decorate_value):
    '''
    Transform each node in the tree's id value
    into a tuple of `(decorate_value, node.id)`
    to use common ids across identical graphs but
    discriminable between attached copies.

    Parameters
    ----------
    tree: Glycan
    decorate_value: int

    Returns
    -------
    Glycan
    '''
    for node in tuple(tree):
        node.id = (decorate_value, node.id)
    return tree


def decorated_value(tree):  # pragma: no cover
    '''
    Get the decorating value from a tree's root node.id.

    Returns `None` if the tree is undecorated

    Parameters
    ----------
    tree: Glycan

    Returns
    -------
    int or None
    '''
    try:
        return next(iter(tree.root.id))
    except Exception:
        return None


def get_decorated(tree, id):  # pragma: no cover
    '''
    As :meth:`Glycan.get`, but with awareness of decorated
    node.id attributes. Will fall back to the normal get method
    if the tree is undecorated.

    Parameters
    ----------
    tree: Glycan
    id: int

    Returns
    -------
    Monosaccharide
    '''
    d = decorated_value(tree)
    if d is None:
        return tree.get(id)
    else:
        return tree.get((d, id))


def undecorate_tree(tree):
    '''
    Remove decoration from a tree and reindex its nodes.

    Depends upon  :attr:`Glycan.index` to find nodes

    Parameters
    ----------
    tree: Glycan

    Returns
    -------
    Glycan
    '''
    i = 1
    for node in list(tree):
        node.id = i
        i += 1
    tree.reindex()
    return tree


def find_root(tree):
    root = rootp(tree)
    while True:
        parents = root.parents()
        if not parents:
            break
        root = parents[0][1]
    return root


class RepeatRecord(object):
    def __init__(self, graph_index, repeat_index, internal_linkage=None,
                 external_linkage=None, multitude=(-1, -1), graph=None,
                 parser=None):
        if graph is None:
            graph = {}
        self.graph_index = graph_index
        self.repeat_index = repeat_index
        self.internal_linkage = internal_linkage
        self.external_linkage = external_linkage
        self.multitude = multitude
        self.graph = {}
        self.original_graph = None
        self.parser = parser

    def __contains__(self, k):
        if self.original_graph is not None:
            return k in self.original_graph
        else:
            return k in self.graph

    def is_exact(self):
        if -1 in self.multitude:
            return StructurePrecisionEnum.unknown
        elif self.multitude[0] == self.multitude[1]:
            return StructurePrecisionEnum.exact
        return StructurePrecisionEnum.ranging

    def expand_inner(self, n=None):
        if n is None:
            if self.multitude[1] != -1:
                n = self.multitude[1]
            elif self.multitude[0] != -1:
                n = self.multitude[0]
            else:
                n = 1

        if self.is_exact() is not StructurePrecisionEnum.unknown:
            if not (self.multitude[0] <= n <= self.multitude[1]):  # pragma: no cover
                raise GlycoCTError("{} is not within the range of {}".format(n, self.multitude))
        sub_unit_indices = sorted(map(try_int, self.graph.keys()))

        if self.original_graph is None:
            glycan_graph = Glycan(find_root(self.graph[sub_unit_indices[0]]), index_method=None).clone()
            self.original_graph = {}
            for k, v in self.graph.items():
                try:
                    self.original_graph[k] = glycan_graph.get(v.id)
                except IndexError:
                    self.original_graph[k] = self.graph[k]

        else:
            self.graph = {k: v.clone() for k, v in self.graph.items()}
        glycan_graph = Glycan(self.graph[sub_unit_indices[0]], index_method=None)

        graph = {1: glycan_graph.clone(index_method=None)}
        decorate_tree(graph[1], 1)

        parent_residue_index = int(self.internal_linkage["parent_residue_index"])
        parent_atom_replaced = link_replacement_composition_map[self.internal_linkage["parent_atom_replaced"]]
        parent_attachment_position = self.internal_linkage["parent_attachment_position"]

        child_residue_index = int(self.internal_linkage["child_residue_index"])
        child_atom_replaced = link_replacement_composition_map[self.internal_linkage["child_atom_replaced"]]
        child_attachment_position = self.internal_linkage["child_attachment_position"]

        op_stack = []

        for i in range(2, n + 1):
            graph[i] = glycan_graph.clone(index_method=None)
            graph[i] = decorate_tree(graph[i], i)
            parent_graph = graph[i - 1]
            child_graph = graph[i]
            parent_node = parent_graph.get((i - 1, parent_residue_index))
            child_node = child_graph.get((i, child_residue_index))
            op_stack.append(
                (form_link, [parent_node, child_node],
                 dict(parent_position=parent_attachment_position,
                      child_position=child_attachment_position,
                      parent_loss=parent_atom_replaced, child_loss=child_atom_replaced)))
        for op in op_stack:
            f, args, kwargs = op
            f(*args, **kwargs)

        self.graph = graph

    def handle_incoming_link(self, parent, parent_position, parent_loss,
                             child_position, child_loss, id=None):
        sub_unit_indices = sorted(self.graph.keys())
        child_graph = self.graph[sub_unit_indices[0]]
        parent = parent()
        child = child_graph.get((1, int(self.external_linkage['child_residue_index'])))
        if parent_loss == Composition("H"):
            child_loss = Composition("OH")

        form_link(parent, child, parent_position=parent_position, child_position=child_position,
                  parent_loss=parent_loss, child_loss=child_loss, id=id)

    def handle_outgoing_link(self, child, parent_position, parent_loss,
                             child_position, child_loss, id=None):
        sub_unit_indices = sorted(self.graph.keys())
        parent_graph = self.graph[sub_unit_indices[-1]]
        child = child()
        parent = parent_graph.get((len(sub_unit_indices), int(self.external_linkage['parent_residue_index'])))
        if isinstance(child, RepeatRecord):
            child.handle_incoming_link(
                lambda: parent, parent_position=parent_position,
                child_position=child_position, parent_loss=parent_loss, child_loss=child_loss, id=id)
        else:
            form_link(
                parent, child, parent_position=parent_position, child_position=child_position,
                parent_loss=parent_loss, child_loss=child_loss, id=id)

    def get_node(self, id, direction=None):  # pragma: no cover
        id = int(id)
        if direction is None or direction == "in":
            sub_unit_indices = sorted(self.graph.keys())
            child_graph = self.graph[sub_unit_indices[0]]
            child = child_graph.get((1, id))
            return child
        elif direction == "out":
            sub_unit_indices = sorted(self.graph.keys())
            parent_graph = self.graph[sub_unit_indices[-1]]
            parent = parent_graph.get((len(sub_unit_indices), id))
            return parent
        else:
            raise Exception("Unknown direction %s" % direction)

    def __root__(self):  # pragma: no cover
        root_node = find_root(self.graph[1])
        return root_node

    def prepare_glycan(self):
        glycan = self.graph[1]
        glycan.deindex()
        return glycan


# Remark: Should this use a different "NoValue" type when input is not int-able?
def try_int(v):
    try:
        return int(v)
    except Exception:
        return None


class GlycoCTError(ParserError):
    pass


class GlycoCTSectionUnsupported(GlycoCTError):
    pass


class GlycoCTReader(object):
    '''
    Simple State-Machine parser for condensed GlycoCT representations. Yields
    |Glycan| instances.
    '''

    @classmethod
    def loads(cls, glycoct_str, structure_class=Glycan, allow_repeats=True):
        '''Parse results from |str|'''
        rep = StringIO(glycoct_str)
        return cls(rep, structure_class=structure_class, allow_repeats=allow_repeats)

    def __init__(self, stream, structure_class=Glycan, allow_repeats=True):
        '''
        Creates a parser of condensed GlycoCT.

        Parameters
        ----------
        stream: basestring or file-like
            A path to a file or a file-like object to be processed
        '''
        self._state = None
        self.graph = {}
        self.handle = opener(stream, "r")
        self.state = START
        self.current_repeat = None
        self.in_repeat = False
        self.repeats = {}
        self.postponed = []
        self.context_stack = []
        self.root = None
        self._iter = None
        self.allow_repeats = allow_repeats
        self.structure_class = structure_class
        self._index = 0
        self._source_line = 0

    def _read(self):
        for line in self.handle:
            self._source_line += 1
            for segment in re.split(r"\s|;", line):
                if "" == segment.strip():
                    continue
                self._current_segment = segment
                yield segment

    def _reset(self):
        self.graph.clear()
        self.root = None
        self.postponed = []
        self.repeats.clear()
        self.context_stack = []
        self.current_repeat = None
        self.in_repeat = False
        self._index += 1

    def push_repeat_context(self, repeat):
        self.context_stack.append(repeat)
        self.current_repeat = self.context_stack[-1]

    def pop_repeat_context(self):
        popped = self.context_stack.pop(-1)
        if self.context_stack:
            self.current_repeat = self.context_stack[-1]
        else:
            self.current_repeat = None
            self.in_repeat = False
        return popped

    def __iter__(self):
        '''
        Calls :meth:`parse` and stores it for reuse with :meth:`__next__`
        '''
        if self._iter is None:
            self._iter = self.parse()
        return self._iter

    def next(self):
        '''
        Calls :meth:`parse` if the internal iterator has not been instantiated
        '''
        if self._iter is None:
            iter(self)
        return next(self._iter)

    #: Alias for next. Supports Py3 Iterator interface
    __next__ = next

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        # print "Entering State: ", value
        self._state = value

    def deferred_retrieval(self, id, direction=None):
        def retrieval():
            try:
                return self.graph[id]
            except KeyError:
                for repeat_ix, repeater in self.repeats.items():
                    if id in repeater:
                        return repeater.get_node(id, direction)
        return retrieval

    def handle_residue_line(self, line):
        '''
        Handle a base line, creates an instance of |Monosaccharide|
        and adds it to :attr:`graph` at the given index.

        Called by :meth:`parse`
        '''
        _, ix, residue_str = re.split(r"^(\d+)b", line, maxsplit=1)
        residue_dict = res_pattern.search(residue_str).groupdict()

        mods = residue_dict.pop("modifications")
        modifications = OrderedMultiMap()
        if mods is not None:
            for p, mod in modification_pattern.findall(mods):
                modifications[try_int(p)] = modification_map[mod]

        residue_dict["modifications"] = modifications
        is_reduced = "aldi" in modifications[1]
        if is_reduced:
            modifications.pop(1, "aldi")
            residue_dict['reduced'] = True

        conf_stem = residue_dict.pop("conf_stem")
        if conf_stem is not None:
            config, stem = zip(*conf_stem_pattern.findall(conf_stem))
        else:
            config = ('x',)
            stem = ('x',)
        residue_dict['stem'] = stem
        residue_dict['configuration'] = config

        residue_dict["ring_start"], residue_dict["ring_end"] = list(map(
            try_int, residue_dict.pop("indices").split(":")))

        residue_dict['anomer'] = anomer_map[residue_dict['anomer']]
        residue_dict['superclass'] = superclass_map[residue_dict['superclass']]
        residue = monosaccharide.Monosaccharide(**residue_dict)
        if self.in_repeat:
            graph = self.current_repeat.graph
        else:
            graph = self.graph
        graph[int(ix)] = residue

        residue.id = int(ix)
        if self.root is None:
            if self.in_repeat:
                self.root = self.current_repeat
            else:
                self.root = residue

    def handle_residue_substituent(self, line):
        '''
        Handle a substituent line, creates an instance of |Substituent|
        and adds it to :attr:`graph` at the given index. The |Substituent| object is not yet linked
        to a |Monosaccharide| instance.

        Called by :meth:`parse`

        '''
        _, ix, subsituent_str = re.split(r"^(\d+)s:", line, maxsplit=1)
        sub = Substituent(subsituent_str.strip())

        if self.in_repeat:
            graph = self.current_repeat.graph
        else:
            graph = self.graph

        graph[int(ix)] = sub

    def get_node(self, id):
        if self.in_repeat:
            try:
                return self.current_repeat.graph[id]
            except KeyError:
                return self.graph[id]
        else:
            return self.graph[id]

    def handle_linkage(self, line):
        '''
        Handle a linkage line, creates an instance of |Link| and
        attaches it to the two referenced nodes in :attr:`graph`. The parent node is always
        an instance of |Monosaccharide|, and the child node
        may either be an instance of |Monosaccharide| or
        |Substituent| or |Monosaccharide|.

        Called by :meth:`parse`

        See also |Link| for more information on the impact of instantiating
        a |Link| object.
        '''
        id, parent_residue_index, parent_atom_replaced, parent_attachment_position,\
            child_residue_index, child_atom_replaced, child_attachment_position = parse_link(line)

        parent = self.get_node(parent_residue_index)
        child = self.get_node(child_residue_index)

        if isinstance(parent, RepeatRecord):
            self.postponed.append((
                parent.handle_outgoing_link,
                self.deferred_retrieval(child_residue_index),
                parent_attachment_position, parent_atom_replaced,
                child_attachment_position, child_atom_replaced, id))
            return
        if isinstance(child, RepeatRecord):
            self.postponed.append((
                child.handle_incoming_link,
                self.deferred_retrieval(parent_residue_index),
                parent_attachment_position, parent_atom_replaced,
                child_attachment_position, child_atom_replaced, id))
            return

        form_link(
            parent, child,
            parent_position=parent_attachment_position, child_position=child_attachment_position,
            parent_loss=parent_atom_replaced, child_loss=child_atom_replaced, id=id)

    def handle_repeat_stub(self, line):
        if not self.allow_repeats:
            raise GlycoCTSectionUnsupported(
                "Repeat are not allowed (set allow_repeats=True to allow them)")
        match = repeat_line_pattern.search(line).groupdict()
        graph_index = (match['graph_index'])
        repeat_index = (match["repeat_index"])
        repeat = RepeatRecord(int(graph_index), int(repeat_index), parser=self)
        repeat._index = self._index
        self.graph[int(graph_index)] = repeat
        self.repeats[int(repeat_index)] = repeat

    def postprocess(self):
        '''
        Handle all deferred operations such as binding together and expanding
        repeating units. Removes any distinguishing markers on node ids, and
        constructs a new instance of :attr:`structure_class` from the accumulated
        graph

        Returns
        -------
        Glycan
        '''
        for repeat_index, repeater in self.repeats.items():
            repeater.expand_inner()

        for postop in self.postponed:
            # logger.debug("Postprocessing %s", postop)
            postop[0](*postop[1:])

        return undecorate_tree(self.structure_class(root=rootp(self.root), index_method=None))

    def parse(self):
        '''
        Returns an iterator that yields each complete :class:`Glycan` instance
        from the underlying text stream.
        '''
        for line in self._read():
            if RES == line.strip():
                if self.state == START or self.state == REPINNER:
                    pass
                elif self.state in TERMINAL_STATES:
                    self.in_repeat = False
                    yield self.postprocess()
                    self._reset()
                else:
                    raise GlycoCTError("Invalid State Transition at line %d" % self._source_line)

                self.state = RES

            elif LIN == line.strip():
                if self.state != RES:
                    raise GlycoCTError("LIN before RES at line %d" % self._source_line)
                self.state = LIN

            elif REP == line.strip():
                if not self.allow_repeats:
                    raise GlycoCTSectionUnsupported(
                        "Repeat are not allowed (set allow_repeats=True to allow them) at line %d" % self._source_line)
                self.state = REP
                # logger.debug("REP")
                self.in_repeat = True

            elif line.strip()[:3] == REP:
                # logger.debug(line)
                if not self.in_repeat:
                    raise GlycoCTError("Encountered %r outside of REP at line %d" % (line, self._source_line))
                header_dict = rep_header_pattern.search(line).groupdict()

                repeat_index = int(header_dict['repeat_index'])
                repeat_record = self.repeats[repeat_index]

                self.push_repeat_context(repeat_record)

                linkage = internal_link_pattern.search(header_dict['internal_linkage']).groupdict()
                repeat_record.internal_linkage = linkage
                repeat_record.external_linkage = linkage
                repeat_record.multitude = tuple(map(try_int, (header_dict['lower_multitude'],
                                                              header_dict['higher_multitude'])))
                self.state = REPINNER
            elif ALT == line.strip():
                raise GlycoCTSectionUnsupported(ALT)
            elif UND == line.strip():
                raise GlycoCTSectionUnsupported(UND)

            elif re.search(r"^(\d+)b", line) and self.state == RES:
                # logger.debug("handling residue")
                self.handle_residue_line(line)
            elif re.search(r"^(\d+)s:", line) and self.state == RES:
                # logger.debug("handling subsituent")
                self.handle_residue_substituent(line)
            elif re.search(r"^(\d+)r:", line) and self.state == RES:
                # raise GlycoCTSectionUnsupported(REP)
                self.handle_repeat_stub(line)
            elif re.search(r"^(\d+):(\d+)", line) and self.state == LIN:
                # logger.debug("handling linkage")
                self.handle_linkage(line)
            else:
                raise GlycoCTError("Unknown format error: %s on line %d" % (line, self._source_line))

        if self.root is not None:
            self.in_repeat = False
            yield self.postprocess()
            self._reset()


GlycoCT = GlycoCTReader


def read(stream, structure_class=Glycan, allow_repeats=True):
    '''
    A convenience wrapper for :class:`GlycoCTReader`
    '''
    return GlycoCTReader(stream, structure_class=structure_class, allow_repeats=allow_repeats)


def loads(glycoct_str, structure_class=Glycan, allow_repeats=True):
    '''
    A convenience wrapper for :meth:`GlycoCTReader.loads`

    As additional convenience, this function does not return an
    iterator over glycans, and returns a single instance if only
    one is present, or a list of instances otherwise.
    '''

    g = GlycoCTReader.loads(glycoct_str, structure_class=structure_class, allow_repeats=allow_repeats)
    first = next(g)
    second = None
    try:
        second = next(g)
        collection = [first, second] + list(g)
        return collection
    except StopIteration:
        return first


def detect_glycoct(string):
    return string.lstrip()[:3] == "RES"


invert_anomer_map = invert_dict(anomer_map)
invert_superclass_map = invert_dict(superclass_map)


class GlycoCTWriterBase(object):
    def __init__(self, structure=None, buffer=None, full=True):
        self.nobuffer = False
        if buffer is None:
            buffer = StringIO()
            self.nobuffer = True

        self.buffer = buffer
        self.structure = structure
        self.full = full

        self.res_counter = make_counter()
        self.lin_counter = make_counter()

        # Look-ups for mapping RES nodes to objects by section index and id,
        # respectively
        self.index_to_residue = {}
        self.residue_to_index = {}

        # Accumulator for linkage indices and mapping linkage indices to
        # dependent RES indices
        self.lin_accumulator = []
        self.dependencies = defaultdict(dict)

    @property
    def structure(self):
        return self._structure

    @structure.setter
    def structure(self, value):
        if value is None:
            self._structure = value
            return
        try:
            structure = treep(value)
        except TypeError:
            try:
                root = rootp(value)
                structure = Glycan(root, index_method=None)
            except TypeError:
                raise TypeError("Could not extract or construct a tree structure from %r" % value)
        self._structure = structure

    def _reset(self):
        self.res_counter = make_counter()
        self.lin_counter = make_counter()

        self.index_to_residue = {}
        self.residue_to_index = {}

        self.lin_accumulator = []
        self.dependencies = defaultdict(dict)

        if self.nobuffer:
            self.buffer = StringIO()

    def _glycoct_sigils(self, link):
        '''
        Helper method for determining which GlycoCT symbols and losses to present
        '''
        parent_loss_str, child_loss_str = link._glycoct_sigils()

        return parent_loss_str, child_loss_str

    def handle_link(self, link, ix, parent_ix, child_ix):
        parent_loss_str, child_loss_str = self._glycoct_sigils(link)

        if link.has_ambiguous_linkage:
            rep = "{ix}:{parent_ix}{parent_loss}({parent_position}+{child_position}){child_ix}{child_loss}"
            return rep.format(
                ix=ix,
                parent_ix=parent_ix,
                parent_loss=parent_loss_str,
                parent_position='|'.join(map(str, link.parent_position_choices)),
                child_ix=child_ix,
                child_loss=child_loss_str,
                child_position='|'.join(map(str, link.child_position_choices)))
        else:
            rep = "{ix}:{parent_ix}{parent_loss}({parent_position}+{child_position}){child_ix}{child_loss}"
            return rep.format(
                ix=ix,
                parent_ix=parent_ix,
                parent_loss=parent_loss_str,
                parent_position=link.parent_position,
                child_ix=child_ix,
                child_loss=child_loss_str,
                child_position=link.child_position)

    def handle_substituent(self, substituent):
        return "s:{0}".format(substituent.name.replace("_", "-"))

    def handle_monosaccharide(self, monosaccharide):
        residue_template = "{ix}b:{anomer}{conf_stem}{superclass}-{ring_start}:{ring_end}{modifications}"

        # This index is reused many times
        monosaccharide_index = self.res_counter()

        # Format individual fields
        anomer = invert_anomer_map[monosaccharide.anomer]
        conf_stem = ''.join("-{0}{1}".format(c.name, s.name)
                            for c, s in zip(monosaccharide.configuration, monosaccharide.stem))
        superclass = "-" + invert_superclass_map[monosaccharide.superclass]

        modifications = '|'.join(
            "{0}:{1}".format(k, v.name) for k, v in monosaccharide.modifications.items())

        modifications = "|" + modifications if modifications != "" else ""
        ring_start = monosaccharide.ring_start if monosaccharide.ring_start is not None else 'x'
        ring_end = monosaccharide.ring_end if monosaccharide.ring_end is not None else 'x'

        # The complete monosaccharide residue line
        residue_str = residue_template.format(ix=monosaccharide_index, anomer=anomer, conf_stem=conf_stem,
                                              superclass=superclass, modifications=modifications,
                                              ring_start=ring_start, ring_end=ring_end)
        res = [residue_str]
        lin = []
        visited_subst = dict()
        # Construct the substituent lines
        # and their links
        for lin_pos, link_obj in monosaccharide.substituent_links.items():
            sub = link_obj.to(monosaccharide)
            if sub.id not in visited_subst:
                sub_index = self.res_counter()
                subst_str = str(sub_index) + self.handle_substituent(sub)
                res.append(subst_str)
                visited_subst[sub.id] = sub_index
            lin.append(
                self.handle_link(
                    link_obj, self.lin_counter(), monosaccharide_index, visited_subst[sub.id]))

        return [res, lin, monosaccharide_index]

    def handle_glycan(self):
        if self.structure is None:
            raise GlycoCTError("No structure is ready to be written.")

        self.buffer.write("RES\n")

        visited = set()
        for node in (self.structure):
            if node.id in visited:
                continue
            visited.add(node.id)
            res, lin, index = self.handle_monosaccharide(node)

            self.lin_accumulator.append((index, lin))
            self.residue_to_index[node.id] = index
            self.index_to_residue[index] = node

            if self.full:
                for pos, lin in node.links.items():
                    if lin.is_child(node):
                        continue
                    self.dependencies[lin.child.id][node.id] = ((self.lin_counter(), lin))
            for line in res:
                self.buffer.write(line + '\n')

            # If this serialization is not meant to be full
            # do not visit residues beyond the first.
            if not self.full:
                break

        self.buffer.write("LIN\n")
        for res_ix, links in self.lin_accumulator:
            for line in links:
                self.buffer.write(line + '\n')
            residue = self.index_to_residue[res_ix]
            if self.full:
                for pos, lin in residue.links.items():
                    if lin.is_child(residue):
                        continue
                    child_res = lin.child
                    ix, lin = self.dependencies[child_res.id][residue.id]
                    self.buffer.write(
                        self.handle_link(lin, ix, res_ix, self.residue_to_index[child_res.id]) + "\n")
        return self.buffer

    def dump(self):
        buffer = self.handle_glycan()
        if self.nobuffer:
            value = buffer.getvalue()
            self._reset()
            return value
        return buffer

    def write(self, structure):
        self.structure = structure
        self._reset()
        return self.dump()


class OrderingComparisonContext(object):
    def __init__(self, parent):
        self.parent = parent
        self.branch_to_terminal_count = self.build_branch_to_terminal_count()

    @property
    def structure(self):
        return self.parent.structure

    def get_branch_from_link_label(self, link):
        return link.label[0]

    def build_branch_to_terminal_count(self):
        counter = Counter()
        try:
            for key in sorted(self.structure.branch_parent_map.keys(), reverse=True):
                parent = self.structure.branch_parent_map[key]
                counter[parent] += counter[key] + 1
        except AttributeError:
            pass
        return counter

    def compare_residue_ordering(self, res_a, res_b):
        n_child_residues_a = monosaccharide.depth(res_a)
        n_child_residues_b = monosaccharide.depth(res_b)
        diff_child_res = n_child_residues_a - n_child_residues_b

        if diff_child_res != 0:
            return diff_child_res

        try:
            branch_length_a = max((monosaccharide.depth(cr) for p, cr in res_a.children()))
        except ValueError:
            branch_length_a = 0
        try:
            branch_length_b = max((monosaccharide.depth(cr) for p, cr in res_b.children()))
        except ValueError:
            branch_length_b = 0

        diff_longest_branch = branch_length_a - branch_length_b

        if diff_longest_branch != 0:
            return diff_longest_branch

        n_branches_from_a = 0
        n_branches_from_b = 0
        for link in res_a.links.values():
            if link.is_parent(res_a):
                branch_label = self.get_branch_from_link_label(link)
                n_branches_from_a = max(n_branches_from_a, self.branch_to_terminal_count[branch_label])

        for link in res_b.links.values():
            if link.is_parent(res_b):
                branch_label = self.get_branch_from_link_label(link)
                n_branches_from_b = max(n_branches_from_b, self.branch_to_terminal_count[branch_label])
        diff_n_branches_from = n_branches_from_a - n_branches_from_b

        if diff_n_branches_from != 0:
            return diff_n_branches_from

        subtree_a = GlycoCTWriter(Glycan.subtree_from(self.structure, res_a)).dump()
        subtree_b = GlycoCTWriter(Glycan.subtree_from(self.structure, res_b)).dump()
        return subtree_a < subtree_b

    def compare_link_ordering(self, link_a, link_b):
        # Ignoring # of links for now since it is difficult
        # to compute
        parent_pos_a = link_a.parent_position
        parent_pos_b = link_b.parent_position
        try:
            diff_parent = parent_pos_a - parent_pos_b
        except TypeError as e:
            print(parent_pos_a, parent_pos_b, link_a, link_b)
            raise e

        if diff_parent != 0:
            return diff_parent

        child_pos_a = link_a.child_position
        child_pos_b = link_b.child_position
        diff_child = child_pos_a - child_pos_b

        if diff_child != 0:
            return diff_child

        sigils_a = link_a._glycoct_sigils()
        sigils_b = link_b._glycoct_sigils()

        if sigils_a[0] != sigils_b[0]:
            return ord(sigils_a[0]) - ord(sigils_b[0])

        if sigils_a[1] != sigils_b[1]:
            return ord(sigils_a[1]) - ord(sigils_b[1])

        child_a = link_a.child
        child_b = link_b.child
        ordered = self.compare_residue_ordering(child_a, child_b)

        return ordered

    def sort_links(self, links):
        return sorted(links, key=cmp_to_key(self.compare_link_ordering))

    def sort_residues(self, residues):
        return sorted(residues, key=cmp_to_key(self.compare_residue_ordering))


class OrderRespectingGlycoCTWriter(GlycoCTWriterBase):
    def __init__(self, structure, buffer=None, full=True):
        self.nobuffer = False
        if buffer is None:
            buffer = StringIO()
            self.nobuffer = True

        self.ordering_context = OrderingComparisonContext(self)

        self.buffer = buffer
        self.structure = structure
        self.full = full

        self.link_queue = deque()
        self.res_counter = make_counter()
        self.lin_counter = make_counter()

        # Look-ups for mapping RES nodes to objects by section index and id,
        # respectively
        self.index_to_residue = {}
        self.residue_to_index = {}

        # Accumulator for linkage indices and mapping linkage indices to
        # dependent RES indices
        self.lin_accumulator = []
        self.dependencies = defaultdict(dict)

    def handle_monosaccharide(self, monosaccharide):
        residue_template = "{ix}b:{anomer}{conf_stem}{superclass}-{ring_start}:{ring_end}{modifications}"

        # This index is reused many times
        monosaccharide_index = self.res_counter()

        self.index_to_residue[monosaccharide_index] = monosaccharide
        self.residue_to_index[monosaccharide.id] = monosaccharide_index

        # Format individual fields
        anomer = invert_anomer_map[monosaccharide.anomer]
        conf_stem = ''.join("-{0}{1}".format(c.name, s.name)
                            for c, s in zip(monosaccharide.configuration, monosaccharide.stem))
        superclass = "-" + invert_superclass_map[monosaccharide.superclass]

        modifications = '|'.join(
            "{0}:{1}".format(k, v.name) for k, v in monosaccharide.modifications.items())

        modifications = "|" + modifications if modifications != "" else ""
        ring_start = monosaccharide.ring_start if monosaccharide.ring_start is not None else 'x'
        ring_end = monosaccharide.ring_end if monosaccharide.ring_end is not None else 'x'

        # The complete monosaccharide residue line
        residue_str = residue_template.format(ix=monosaccharide_index, anomer=anomer, conf_stem=conf_stem,
                                              superclass=superclass, modifications=modifications,
                                              ring_start=ring_start, ring_end=ring_end)

        link_collection = list(monosaccharide.substituent_links.values())
        if self.full:
            link_collection.extend([cl for p, cl in monosaccharide.children(links=True)])

        links = self.ordering_context.sort_links(link_collection)
        self.link_queue.extend(links)
        return residue_str

    def handle_substituent(self, substituent):
        substituent_index = self.res_counter()

        self.index_to_residue[substituent_index] = substituent
        self.residue_to_index[substituent.id] = substituent_index

        subst_str = "%ss:%s" % (substituent_index, substituent.name.replace("_", "-"))

        links = self.ordering_context.sort_links([cl for p, cl in substituent.children(links=True)])
        self.link_queue.extend(links)
        return subst_str

    def handle_glycan(self):
        if self.structure is None:
            raise GlycoCTError("No structure is ready to be written.")

        self.buffer.write("RES\n")

        visited = set()
        if self.structure.root.node_type is Monosaccharide.node_type:
            res_str = self.handle_monosaccharide(self.structure.root)
            self.buffer.write(res_str + "\n")
        else:
            res_str = self.handle_substituent(self.structure.root)
        links_in_order = []
        while self.link_queue:
            link = self.link_queue.popleft()
            # Explicitly add before skipping to avoid double-writing
            # residues, but including multiple-link cases
            links_in_order.append(link)
            if link.child.id in visited:
                continue
            visited.add(link.child.id)
            if link.child.node_type is Monosaccharide.node_type:
                line = self.handle_monosaccharide(link.child)
            else:
                line = self.handle_substituent(link.child)
            self.buffer.write(line + "\n")

        self.buffer.write("LIN\n")
        for link in links_in_order:
            if not link.is_substituent_link() and not self.full:
                continue
            parent_ix = self.residue_to_index[link.parent.id]
            child_ix = self.residue_to_index[link.child.id]
            line = self.handle_link(link, self.lin_counter(), parent_ix, child_ix)
            self.buffer.write(line + "\n")

        return self.buffer


GlycoCTWriter = OrderRespectingGlycoCTWriter


def dump(structure, buffer=None):
    '''
    Serialize the |Glycan| graph object into condensed GlycoCT, using
    `buffer` to store the result. If `buffer` is |None|, then the
    function will operate on a newly created :class:`~glypy.utils.StringIO` object.

    Parameters
    ----------
    structure: |Glycan|
        The structure to serialize
    buffer: file-like or None
        The stream to write the serialized structure to. If |None|, uses an instance
        of `StringIO`

    Returns
    -------
    file-like or str if ``buffer`` is :const:`None`

    '''
    return GlycoCTWriter(structure, buffer).dump()


def dumps(structure, full=True):
    return GlycoCTWriter(structure, None, full=full).dump()


def _postprocessed_single_monosaccharide(monosaccharide, convert=True):
    if convert:
        monostring = dumps(monosaccharide, full=False)
    else:
        monostring = monosaccharide
    monostring = monostring.replace("\n", " ")
    if monostring.endswith("LIN "):
        monostring = monostring.replace(" LIN ", "")
    else:
        monostring = monostring.strip()
    return monostring


Monosaccharide.register_serializer("glycoct", _postprocessed_single_monosaccharide)
Glycan.register_serializer("glycoct", dumps)

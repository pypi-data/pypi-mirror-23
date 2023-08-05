import os
import traceback

def _lastmodified(a):
    return os.stat(a.name).st_mtime

def is_older(a, b):
    """ Returns true if Dataset *a* was last modified before Dataset *b*

    Parameters
    ----------
    a, b : Dataset

    Returns
    -------
    bool
    """
    if isinstance(a, DatasetGroup):
        mtime_a = max(os.stat(d.name).st_mtime for d in a)
    elif isinstance(a, Dataset):
        mtime_a = os.stat(a.name).st_mtime
    else:
        raise TypeError("must be Dataset or DatasetGroup")

    if isinstance(b, DatasetGroup):
        mtime_b = min(os.stat(d.name).st_mtime for d in b)
    elif isinstance(b, Dataset):
        mtime_b = os.stat(b.name).st_mtime
    else:
        raise TypeError("must be Dataset or DatasetGroup")

    return mtime_a < mtime_b

class Reason(object):
    """ A Reason describes why a build step is performed.

    Parameters
    ----------
    explanation : str
    """

    def __init__(self, explanation):
        self._explanation = explanation

    def __str__(self):
        return self._explanation

PARENTMISSING = Reason("a parent doesn't exist")
PARENTNEWER = Reason("a parent is newer than the child")
MISSING = Reason("the dataset doesn't exist")

class Dataset(object):
    """ Dataset represents a dataset or a step along a dependency chain.

    Parameters
    ----------
    name : str
        imagined to be a filename

    Other keyword arguments are accessible as instance attributes.
    """

    __hash__ = object.__hash__

    def __init__(self, name, **kw):
        self.name = name
        self._parents = []
        self._children = []
        self._store = kw
        return

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return (self.name == other.name) and (self._store == other._store)

    def __neq__(self, other):
        return not (self == other)

    def __getattr__(self, name):
        if name in self._store:
            return self._store[name]
        else:
            raise AttributeError("'{0}'".format(name))

    def dependson(self, *datasets):
        """ Declare that Dataset depends on one or more other Dataset instances.
        Does not affect previous declarations.
        """
        newparents = set(datasets)
        oldparents = set(self._parents)
        intrx = newparents.intersection(oldparents)
        if len(intrx) != 0:
            raise RedundantDeclaration("{0} already depends on "
                            "{1}".format(self, list(intrx)[0]))

        self._parents = list(newparents.union(oldparents))
        for parent in newparents:
            if self not in parent.children(0):
                parent._children.append(self)

    def parents(self, depth=-1):
        """ Return the Dataset instances that this Dataset depends on.

        Parameters
        ----------
        depth : int
            Recursion depth. 0 means no recursion, while -1 means infinite
            recursion.
        """
        yielded = []
        for dataset in self._parents:
            if dataset not in yielded:
                yielded.append(dataset)
                yield dataset
            if depth != 0:
                for grandparent in dataset.parents(depth=depth-1):
                    if grandparent not in yielded:
                        yielded.append(grandparent)
                        yield grandparent

    def children(self, depth=-1):
        """ Return the Dataset instances that depend on this Dataset.

        Parameters
        ----------
        depth : int
            Recursion depth. 0 means no recursion, while -1 means infinite
            recursion.
        """
        yielded = []
        for dataset in self._children:
            if dataset not in yielded:
                yielded.append(dataset)
                yield dataset
            if depth != 0:
                for grandchild in dataset.children(depth=depth-1):
                    if grandchild not in yielded:
                        yielded.append(grandchild)
                        yield grandchild

    def buildnext(self, ignore=None):
        """ Generator for datasets that require building/rebuilding in order to
        build this (target) Dataset, given the present state of the dependency
        graph.

        These targets are necessary but not necessarily sufficient to build the
        objective Dataset after a single iteration. Intended use is to call
        `buildnext` repeatedly, building the targets after each call, until the
        objective Dataset can be built.

        Parameters
        ----------
        ignore : list, optional
            list of dependencies to ignore building (e.g., because unbuildable
            or otherwise broken for reasons not encoded in the dependency
            graph).

        Yields
        ------
        (Dataset, Reason)
        """
        if not is_acyclic(self):
            raise CircularDependency()

        def needsbuild(child):
            if not all(os.path.exists(p.name) for p in child.parents(0)):
                return False, PARENTMISSING
            elif os.path.exists(child.name) and \
                    any(is_older(child, p) for p in child.parents(0)):
                return True, PARENTNEWER
            elif not os.path.exists(child.name):
                return True, MISSING
            else:
                return False, None

        def walkbranch(stem, ancestors, branches):
            """ Breadth-first search through branch for broken branches
            involving ancestors """
            for child in stem.children(0):
                if child not in ancestors:
                    continue

                build, reason = needsbuild(child)

                if build:
                    if reason in (PARENTNEWER, MISSING):
                        yield child, reason
                    else:
                        raise RuntimeError("unexpected reason")

                elif reason is PARENTMISSING:
                    # A parent derived from another stem is missing, so delay
                    # build until that branch is traversed
                    pass

                elif not build:
                    # Child is up to date, so append it as a new 'stem' to walk down
                    if child not in branches:
                        branches.append(child)

        ancestors = list(self.parents())
        branches = list(self.roots())

        if ignore is None:
            ignore = []
        built = [_ for _ in ignore]

        while True:
            if len(branches) == 0:
                break

            for dep, reason in walkbranch(branches[0], ancestors, branches):
                if dep not in built:
                    built.append(dep)
                    yield dep, reason
            branches = branches[1:]
        return

    def roots(self):
        """ Generator for the roots (dependency-less parents) of this Dataset.

        Yields
        ------
        Dataset
        """
        yielded = []
        for dataset in self._parents:
            if len(dataset._parents) == 0:
                if dataset not in yielded:
                    yield dataset
                    yielded.append(dataset)
            else:
                for gp in dataset.roots():
                    if gp not in yielded:
                        yield gp
                        yielded.append(gp)

class DatasetGroup(Dataset):
    """ DatasetGroup represents multiple Dataset instances that are build
    together. For example, these might be a dataset and associated metadata.
    These should be built together, and dependent files are sensitive to
    updates in any member of a DatasetGroup.
    """

    __hash__ = object.__hash__

    def __init__(self, name, datasets, **kw):
        self.name = name
        self.datasets = datasets
        self._parents = []
        self._children = []
        self._store = kw

    def __iter__(self):
        for d in self.datasets:
            yield d

class RedundantDeclaration(Exception):
    def __init__(self, msg):
        self.message = msg

class CircularDependency(Exception):
    def __init__(self, msg="graph not acyclic"):
        self.message = msg

def is_acyclic(dataset):
    """ Verifies that the portion of the dependency graph *above* a particular
    dataset is acyclic, i.e. it contains no circular dependencies.

    Parameters
    ----------
    dataset : Dataset

    Returns
    -------
    bool
    """
    def visit(dataset, temp_marks, perm_marks):
        if dataset in temp_marks:
            raise CircularDependency()
        if dataset not in perm_marks:
            temp_marks.append(dataset)
            for parent in dataset.parents(0):
                visit(parent, temp_marks, perm_marks)
            perm_marks.append(dataset)
            idx = temp_marks.index(dataset)
            del temp_marks[idx]
        return True

    temp_marks = []
    perm_marks = []
    try:
        return visit(dataset, temp_marks, perm_marks)
    except CircularDependency:
        return False

def buildall(target):
    """ Yield groups of dependencies in the order they should be built to
    satisfy a target dataset.

    Parameters
    ----------
    target : Dataset
        dataset to be built

    Yields
    ------
    lists of (Dataset, Reason) tuples
        datasets that must be built (potentially in parallel) before the next
        group of datasets

    Raises
    ------
    CircularDependency if graph is not acyclic

    Notes
    -----
    Compared to Dataset.buildnext, this obviates the need to traverse the
    entire graph at every step.
    """
    if not is_acyclic(target):
        raise CircularDependency()

    def needsbuild(dataset):
        if os.path.exists(dataset.name) and \
                any(is_older(dataset, p) for p in dataset.parents(0)
                                         if os.path.exists(p.name)):
            return True, PARENTNEWER
        elif not os.path.exists(dataset.name):
            return True, MISSING
        else:
            return False, None

    def mark_children_breadthfirst(*roots):
        """ Set marks """
        marks = {}
        queue = [(0, root) for root in roots]
        while len(queue) != 0:
            i, dep = queue.pop(0)
            for child in dep.children(0):
                iold = marks.get(child, -1)
                if i > iold:
                    marks[child] = i
                queue.append((i+1, child))
        return marks

    parents = set(target.parents())

    # Map of Dataset -> integer, where the integer indicates the build step
    marks = mark_children_breadthfirst(*target.roots())

    groups = []
    maxi = 0
    for dep, i in marks.items():
        nb, reason = needsbuild(dep)
        if nb and dep in parents:
            while i >= maxi:
                groups.append([])
                maxi += 1
            groups[i].append((dep, reason))

    for group in groups:
        if target in (a[0] for a in group):
            yield [(target, MISSING)]
        else:
            yield group

def get_ancestor_edges(dataset):
    edges = []
    for parent in dataset.parents(0):
        e = (parent, dataset)
        if e not in edges:
            edges.append(e)
        edges.extend(e for e in get_ancestor_edges(parent) if e not in edges)
    return edges

def get_descendent_edges(dataset):
    edges = []
    for child in dataset.children(0):
        e = (dataset, child)
        if e not in edges:
            edges.append(e)
        edges.extend(e for e in get_descendent_edges(child) if e not in edges)
    return edges

def graphviz(*datasets, **kwargs):
    """ Return a graphviz diagram in dot format describing the dependency
    graph.

    Parameters
    ----------
    *datasets : Dataset instances
    include : function, optional
        Callable taking a Dataset and returning a boolean indicating whether a
        dataset should be included in the graph. Default is to include all
        datasets.
    style : function, optional
        Callable taking a Dataset and returning graphviz styling attributes.
        Default is bare styling.

    Returns
    -------
    str : graphviz visualization in dot format
    """
    f_incl = kwargs.get("include", lambda d: True)
    f_style = kwargs.get("style", lambda d: "")

    # Make a list of edges (parent, child)
    edges = []
    for ds in datasets:
        edges.extend(e for e in get_descendent_edges(ds) if e not in edges)
        edges.extend(e for e in get_ancestor_edges(ds) if e not in edges)

    relations = []
    for e in edges:
        if f_incl(e[0]) and f_incl(e[1]):
            s = f_style(e[1])
            if len(s) != 0:
                s = " [{0}]".format(s)
            relations.append("\"{0}\" -> \"{1}\"{2}".format(e[0].name, e[1].name, s))

    dotstr = """strict digraph {{
  {0}
}}""".format("\n  ".join(relations))
    return dotstr

def buildmanager(delegator):
    """ Decorator to be used for constructing build managers.

    Wraps
    -----
    A delegator function (f(target, reason)) that given a build target and a
    reason, attempts to build the target

    Returns
    -------
    A function that takes a target Dataset and repeatedly calls the delegator
    with the correct sequence of intermediate Datasets to develop the target.

    Additional keyword arguments of the returned function are *max_attampts*,
    which is an integer indicating how many times a Dataset should be
    attempted, and a string *onfailure* that may be one of ("raise", "print",
    "ignore"), indicating how to handle exceptions during the build.

    Example
    -------
    ::
        @buildmanager(print)
        def run_build(dependency, reason):
            # performs actions to build *dependency*
            # ...
            return exitcode

        # Calling `run_build` now enters a loop that builds all dependencies
        run_build(target, max_attempts=1)
    """
    def executor(target, max_attempts=1, onfailure="raise"):
        """ Perform action to build a target.

        Parameters
        ----------
        target : Dataset
            terminal dataset to build
        max_attempts : int, optional
            maximum number of times a dependency build should be attempted
        onfailure : str
            if "raise" then propagate failures
            if "print" then print traceback and continue
            if "ignore" then continue silently
        """
        noop = False
        attempts = {}
        while not noop:
            noop = True
            for build_stage in buildall(target):
                for dep, reason in build_stage:
                    if attempts.get(dep, 0) < max_attempts:
                        noop = False
                        try:
                            exitcode = delegator(dep, reason)
                        except Exception as exc:
                            if onfailure == "raise":
                                raise exc
                            elif onfailure == "print":
                                traceback.print_exc()
                            elif onfailure == "ignore":
                                pass
                            attempts[dep] = attempts.get(dep, 0) + 1
        if (not os.path.exists(target.name)) or \
                any(is_older(target, parent) for parent in target.parents(0)):
            delegator(target, Reason("it was requested by the caller"))
        return attempts
    return executor

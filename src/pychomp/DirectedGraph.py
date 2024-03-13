### DirectedGraph.py
### MIT LICENSE 2022 Marcio Gameiro

class DiGraph:
    """A simple directed graph class"""
    def __init__(self):
        """Initialize an empty graph"""
        self.graph_vertices = set()
        self.adjacency_lists = {}
        self.vertex_labels = {}

    def add_vertex(self, v, label=None):
        """Add vertex v to the graph"""
        if v in self.graph_vertices:
            return
        self.graph_vertices.add(v)
        self.adjacency_lists[v] = set()
        if label is not None:
            self.vertex_labels[v] = label

    def add_edge(self, u, v):
        """Add edge u -> v to the graph"""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency_lists[u].add(v)

    def remove_edge(self, u, v):
        """Remove the edge u -> v from the graph"""
        self.adjacency_lists[u].discard(v)

    def vertex_label(self, v):
        """Return the label of vertex v"""
        if v in self.vertex_labels:
            return self.vertex_labels[v]
        return str(v)

    def vertices(self):
        """Return the set of vertices"""
        return self.graph_vertices

    def adjacencies(self, v):
        """Return the set of adjacencies of v"""
        return self.adjacency_lists[v]

    def edges(self):
        """Return the list of edges"""
        return [(u,v) for u in self.vertices() for v in self.adjacencies(u)]

    def graphviz(self):
        """Return a graphviz string representing the graph"""
        gv = 'digraph {\n'
        indices = {v: str(k) for k, v in enumerate(self.vertices())}
        for v in self.vertices():
            gv += indices[v] + '[label="' + self.vertex_label(v) + '"];\n'
        for (u,v) in self.edges():
            gv += indices[u] + ' -> ' + indices[v] +  ';\n'
        return gv + '}\n'

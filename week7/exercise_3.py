from mrjob.job import MRJob
from mrjob.step import MRStep


class exercise3(MRJob):

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                reducer=self.reducer
            ),
            MRStep(reducer=self.discover_triangles),
            MRStep(reducer=self.count_triangles),
            MRStep(reducer=self.sum_triangles)
        ]

    def mapper(self, _, line):
        node_a, node_b = line.split()
        yield int(node_a), int(node_b)
        yield int(node_b), int(node_a)

    def reducer(self, node, connecting_nodes):
        """
        It returns a tuple of two connecting nodes and their respective connecting nodes in a list:
             (node_a, node_b), [(node_a, nodes), (node_b, nodes)]
        :param node:
        :param connecting_nodes:
        """
        nodes = reduce(lambda x, y: x + [y], connecting_nodes, [])

        for n in nodes:
            yield sorted([node, n]), (n, nodes)

    def discover_triangles(self, node_pair, connecting_nodes):
        """
        All nodes are associated with both nodes in node_pair (connecting_nodes)
        If both nodes in node_pair have the same connecting node, they must form a triangle
        :param node_pair:
        :param connecting_nodes:
        """
        node_a, node_b = node_pair
        common_nodes = []

        for node, nodes in connecting_nodes:
            for connected_node in nodes:
                if connected_node != node:
                    if connected_node in common_nodes:
                        # this yields True for every point in the triangle.
                        yield sorted([node_a, node_b, connected_node]), True
                    else:
                        common_nodes += [connected_node]

    def count_triangles(self, _, triangles):
        yield "triangles", 1

    def sum_triangles(self, _, triangles):
        yield _, sum(triangles)

if __name__ == "__main__":
    exercise3.run()
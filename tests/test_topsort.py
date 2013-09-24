from topsort.network import Network
from topsort.node import Node



class N(object):
    def __init__(self, thing):
        self.data = thing


def test_basic_sort():
    """ Ensure that we can do a basic top-sort. """

    NODES = {x: Node(x) for x in [5, 11, 2, 7, 8, 9, 10, 3]}
    EDGES = [
        (3, 8),
        (3, 10),
        (5, 11),
        (7, 8),
        (7, 11),
        (8, 9),
        (11, 2),
        (11, 9),
        (11, 10),
    ]

    network = Network()

    for fro, to in EDGES:
        network.add_edge(NODES[fro], NODES[to])

    assert [x.data for x in network.sort()] == [3, 5, 7, 8, 11, 10, 9, 2,]
    # The implementation is deterministic, so we can assert order here, since
    # we know the order that nodes are added.

import networkx as nx

initial_partitions = [
    [[0]],
    [[0], [1]],
    [[0], [1, 2]],
    [[0, 3], [1, 2]],
    [[0, 3, 4], [1, 2]],
    [[0, 3, 4], [1, 2], [5]],
    [[0, 3, 4], [1, 2], [5], [6]],
    [
        [0, 3, 4],
        [1, 2],
        [5],
        [6],
        [7],
    ],
    [
        [0, 3, 4],
        [1, 2],
        [5, 8],
        [6],
        [7],
    ],
    [
        [0, 3, 4],
        [1, 2, 9],
        [5, 8],
        [6],
        [7],
    ],
]


def create_graph(edges, size):
    nodes = [i for i in range(size)]

    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    return graph


def create_graph_partition_tuple(graph):
    return (graph, initial_partitions[len(graph.nodes) - 1])


graph_partition_tuples = list(
    map(
        lambda edges: create_graph_partition_tuple(create_graph(edges=edges[1:], size=edges[0])),
        [
            [
                10,
                (0, 6),
                (1, 2),
                (1, 4),
                (2, 7),
                (3, 7),
                (4, 2),
                (5, 2),
                (5, 8),
                (6, 1),
                (6, 4),
                (6, 8),
                (8, 1),
                (9, 2),
                (9, 4),
            ],
            [
                10,
                (0, 1),
                (0, 7),
                (0, 8),
                (3, 2),
                (4, 2),
                (4, 6),
                (7, 1),
                (7, 2),
                (8, 0),
                (8, 1),
                (8, 9),
                (9, 6),
            ],
            [
                10,
                (0, 2),
                (0, 3),
                (0, 5),
                (1, 3),
                (1, 4),
                (2, 6),
                (2, 9),
                (4, 9),
                (5, 8),
                (6, 7),
                (7, 9),
                (8, 3),
            ],
            [
                10,
                (0, 6),
                (1, 0),
                (1, 2),
                (1, 4),
                (2, 0),
                (2, 3),
                (3, 1),
                (4, 1),
                (4, 5),
                (6, 2),
                (9, 4),
                (9, 6),
            ],
            [5, (0, 2), (2, 0), (2, 3), (2, 4), (3, 0), (3, 1), (4, 0), (4, 2), (4, 3)],
            [5, (0, 3), (1, 3), (2, 1), (2, 3), (3, 0), (3, 4), (4, 0), (4, 2), (4, 3)],
            [5, (0, 1), (0, 2), (0, 3), (1, 2), (2, 4), (3, 0), (3, 2), (4, 1), (4, 3)],
            [
                5,
                (0, 2),
                (0, 3),
                (1, 2),
                (1, 3),
                (2, 0),
                (2, 1),
                (2, 3),
                (3, 2),
                (4, 0),
                (4, 1),
                (4, 2),
                (4, 3),
            ],
            [3, (0, 1), (0, 2), (1, 0), (2, 0), (2, 1)],
            [3, (0, 1), (0, 2), (1, 0), (1, 2)],
            [3, (0, 1), (1, 2), (2, 0), (2, 1)],
            [3, (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)],
        ],
    )
)

edges_partition_rscp_tuples = [
    (
        [6, (0, 2), (0, 3), (1, 2), (2, 4), (3, 4)],
        [(2, 4), (0, 1, 3, 5)],
        set([(0,), (1,), (2,), (3,), (4,), (5,)]),
    ),
    (
        [
            8,
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 5),
            (0, 7),
            (1, 2),
            (1, 7),
            (2, 3),
            (2, 4),
            (2, 5),
            (2, 6),
            (2, 7),
            (3, 4),
            (3, 5),
            (4, 7),
            (5, 6),
            (6, 7),
        ],
        [(1,), (2,), (3,), (4,), (0, 5, 6, 7)],
        set([(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,)]),
    ),
    (
        [
            6,
            (0, 2),
            (0, 3),
            (0, 5),
            (1, 2),
            (1, 4),
            (1, 5),
            (2, 4),
            (2, 5),
            (3, 5),
            (4, 5),
        ],
        [(2,), (3,), (1, 4), (0, 5)],
        set([(0,), (1,), (2,), (3,), (4,), (5,)]),
    ),
    (
        [
            7,
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 5),
            (0, 6),
            (1, 2),
            (1, 3),
            (1, 4),
            (1, 5),
            (1, 6),
            (2, 3),
            (2, 4),
            (2, 5),
            (3, 4),
            (3, 5),
            (3, 6),
            (4, 5),
            (4, 6),
        ],
        [(3,), (4,), (5,), (0, 1, 2, 6)],
        set([(0,), (1,), (2,), (3,), (4,), (5,), (6,)]),
    ),
    (
        [
            9,
            (0, 1),
            (0, 4),
            (0, 5),
            (0, 8),
            (1, 3),
            (1, 4),
            (1, 5),
            (2, 3),
            (2, 4),
            (2, 6),
            (2, 8),
            (3, 4),
            (3, 7),
            (3, 8),
            (4, 5),
            (4, 6),
            (4, 7),
            (5, 6),
            (5, 7),
            (5, 8),
            (6, 7),
            (6, 8),
        ],
        [(0,), (2, 5, 7), (1, 3, 4, 6, 8)],
        set([(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,)]),
    ),
    (
        [5, (0, 2), (0, 3), (0, 4), (1, 3), (2, 3), (2, 4), (3, 4)],
        [(1,), (3,), (0, 2, 4)],
        set([(0,), (1,), (2,), (3,), (4,)]),
    ),
    (
        [
            6,
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 5),
            (1, 2),
            (1, 4),
            (1, 5),
            (2, 3),
            (2, 4),
            (2, 5),
            (3, 4),
            (3, 5),
            (4, 5),
        ],
        [(0, 2, 4), (1, 3, 5)],
        set([(0,), (1,), (2,), (3,), (4,), (5,)]),
    ),
    (
        [9, (0, 4), (0, 7), (5, 7), (6, 8)],
        [(2,), (3,), (0, 4), (5,), (1, 7), (6, 8)],
        set([(0,), (1, 7), (2,), (3,), (4,), (5,), (6,), (8,)]),
    ),
    (
        [
            8,
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 6),
            (1, 2),
            (1, 3),
            (1, 4),
            (1, 5),
            (1, 6),
            (1, 7),
            (2, 3),
            (2, 4),
            (2, 5),
            (2, 7),
            (3, 4),
            (3, 6),
            (3, 7),
            (4, 6),
            (4, 7),
            (5, 6),
            (5, 7),
            (6, 7),
        ],
        [(4,), (1, 2, 5), (6,), (0, 3, 7)],
        set([(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,)]),
    ),
    (
        [
            8,
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 5),
            (0, 6),
            (0, 7),
            (1, 2),
            (1, 3),
            (1, 5),
            (1, 7),
            (2, 3),
            (2, 4),
            (2, 5),
            (2, 6),
            (3, 4),
            (3, 5),
            (4, 7),
            (5, 6),
        ],
        [(1,), (2,), (3, 5), (0, 4, 6), (7,)],
        set([(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,)]),
    ),
]

graph_partition_rscp_tuples = [
    (create_graph(edges=edges[1:], size=edges[0]), partition, rscp)
    for (edges, partition, rscp) in edges_partition_rscp_tuples
]

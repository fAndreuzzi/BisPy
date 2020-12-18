![Python package](https://github.com/fAndreuzzi/Bisimulation-Algorithms/workflows/Python%20package/badge.svg?branch=master) <a href='https://coveralls.io/github/fAndreuzzi/Bisimulation-Algorithms'><img src='https://coveralls.io/repos/github/fAndreuzzi/Bisimulation-Algorithms/badge.svg' alt='Coverage Status' /></a>
 [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) <img src='https://img.shields.io/badge/code style-black-black' alt='Code style' />

# Bisimulation-Algorithms

## The problem
Let's consider a directed graph G=(V,E). A *bisimulation* on G is a binary relation R on V which satisfies the following property:

<img src="https://render.githubusercontent.com/render/math?math=\forall a,b \mid R(a,b)">

the following conditions hold:

<img src="https://render.githubusercontent.com/render/math?math=1. \,\,\forall a_1 \mid \left(a, a_1\right) \in E, \exists \, b_1 \mid \left(b, b_1\right) \in E \lor R(a_1,b_1)">
<img src="https://render.githubusercontent.com/render/math?math=2. \,\forall b_1 \mid \left(b, b_1\right) \in E, \exists \, a_1 \mid \left(a, a_1\right) \in E \lor R(a_1,b_1)">

This is in fact a condition on the *behavior* of the nodes: two nodes *behave* in the *same way* if for each node reached by one of them, there's a fourth node reached by the other node which *behaves* like the third.

This informal definition of bisimulation is equivalent to the formal one above, but it's somewhat more explicit.

## Algorithmic approach
The somewhat recursive statement of the problem makes the bisimulation an apparently difficult problem from an algorithmic point of view. However, as Kanellakis C. and Smolka S. shown in their paper published in 1990, computing the *maximum* bisimulation of a graph (namely the *biggest* bisimulation, the one which relates the highest number of nodes) is equivalent to determining the *relational stable coarsest partition*.

The *RSCP* of a set S given a binary relation R, as the name suggests, is the *coarsest* (which contains the fewest number of blocks) *stable partition*, where *stability* is a quality of partitions which is defined as follows for a given partition P:

<img src="https://render.githubusercontent.com/render/math?math=\forall A,B \in P, A \subseteq R^{-1}(B) \lor A \cap R^{-1}(B) = \emptyset">

This statemente is reassuring: in order to verify that two nodes are *bisimilar* (which is quite interesting for the applications) we do not need to visit exhaustively their children, and then the children of the children, and so on. We only need to compute the RSCP of V with respect to the relation E, and check whether the two nodes are in the same block.

## Algorithms
This library contains the implementation in Python 3 of the following algorithms:
|  Name        |  Strategy   | Complexity  |
|--------------|:-------------:|:---:|
| Paige-Tarjan | Negative    | <img src="https://render.githubusercontent.com/render/math?math=O(\mid E\mid \log \mid V \mid)">  |
| Dovier-FBA   | Negative    | <img src="https://render.githubusercontent.com/render/math?math=O(\mid E\mid \log \mid V \mid)">  |
| Saha         | Incremental |  Depends on the entity of the changes. |

## Installation
The package isn't published, therefore the following steps are needed:
1. Open a terminal window;
2. Navigate to a suitable directory;
3. Clone the repository: `git clone https://github.com/fAndreuzzi/Bisimulation-Algorithms.git`;
4. Open the new directory `cd Bisimulation-Algorithms`;
5. Install the package in development mode: `pip install -e ./` or `pip3 install -e ./`.

## Usage
This example shows how to use the PTA algorithm on a given graph. We use [NetworkX](https://networkx.org/) to represent the input.

The following snippet:
```python
import networkx as nx

graph = nx.DiGraph()
graph.add_nodes_from(range(5))
graph.add_edges_from([(0,1), (0,3), (1,4), (2,3), (4,3)])
```
intializes a graph which contains 5 nodes (from 0 to 4) and some edges. We assume that the initial partition is the trivial one:
`{0,1,2,3,4}`.

We can obtain the RSCP with the Paige-Tarjan Algorithm as follows:
```python
from bisimulation_algorithms import paige_tarjan

rscp = paige_tarjan(graph)
print(rscp)
```
Output: `[(3,), (1,), (2, 4), (0,)]`

If we wanted to use a different initial partition, like:
```
initial_partition = [(0,1,2), (3,4)]
```

the code would have been:
```python
rscp = paige_tarjan(graph, initial_partition)
print(rscp)
```
Output: `[(3,), (1,), (2,) (4,), (0,)]`

## Examples
Initial partition | RSCP
--- | ---
![](res/pta-before.png) | ![](res/pta-after.png)
![](res/pta-before2.png) | ![](res/pta-after2.png)

## Applications
Work in progress.

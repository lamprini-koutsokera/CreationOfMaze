# CreationOfMaze
MazeCreator

We know that if we want to run a graph we can use either the [Depth First](https://en.wikipedia.org/wiki/Depth-first_search) or 
the [Breath First Search](https://en.wikipedia.org/wiki/Breadth-first_search). We also know that these methods correspond to ways 
of exploring a maze. Ιn this project used the reverse way. More specifically, we think we have a graph nxn. The nodes correspond 
to the rooms of the maze. Initially we consider that each node is connected to all its neighboring nodes. The corner nodes have 
two neighbors, nodes on the periphery of the graph but not in the corners have three neighbors and internal nodes have four neighbors.

1. We start from a node in the graph.

2. We note that we have visited this node and get the list of neighboring nodes.We take randomly neighboring elements and proceed as 
follows:

- If we have not visited the neighboring node, go to this node, store the link between two nodes and recursively continue the 
procedure from step 2 with the neightboring element.

In essence we run a Depth First Search of the graph where each node get its neighbors randomly and store somewhere the links followed.

When we completed the process we have a new graph. The vertices are the vertices of the original graph and the links are the links that 
followed. This graph is a maze.

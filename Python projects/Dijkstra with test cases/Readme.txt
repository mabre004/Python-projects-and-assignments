Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm, SPF algorithm)[1] is an algorithm for finding the
shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer
scientist Edsger W. Dijkstra in 1956 and published three years later.[2][3][4]

The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes,[4]
but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other
nodes in the graph, producing a shortest-path tree.

For a given source node in the graph, the algorithm finds the shortest path between that node and every other.
[5]:196–206 It can also be used for finding the shortest paths from a single node to a single destination node by
stopping the algorithm once the shortest path to the destination node has been determined. For example, if the nodes of
the graph represent cities and edge path costs represent driving distances between pairs of cities connected by a direct
road (for simplicity, ignore red lights, stop signs, toll roads and other obstructions), Dijkstra's algorithm can be
used to find the shortest route between one city and all other cities. A widely used application of shortest path
algorithm is network routing protocols, most notably IS-IS (Intermediate System to Intermediate System) and
Open Shortest Path First (OSPF). It is also employed as a subroutine in other algorithms such as Johnson's.

The Dijkstra algorithm uses labels that are positive integers or real numbers, which are totally ordered.
It can be generalized to use any labels that are partially ordered, provided the subsequent labels
(a subsequent label is produced when traversing an edge) are monotonically non-decreasing.
This generalization is called the Generic Dijkstra shortest-path algorithm.[6]

Dijkstra's algorithm uses a data structure for storing and querying partial solutions sorted by distance from the start.
The original algorithm uses a min-priority queue and runs in time
{\displaystyle O(|V|^{2})}O(|V|^{2})(where {\displaystyle |V|}|V|is the number of nodes).
The idea of this algorithm is also given in Leyzorek et al. 1957. Fredman & Tarjan 1984 propose using a Fibonacci heap
min-priority queue to optimize the running time complexity to {\displaystyle O(|E|+|V|\log |V|)}O(|E|+|V|\log |V|)
(where {\displaystyle |E|}|E|is the number of edges). This is asymptotically the fastest known single-source
shortest-path algorithm for arbitrary directed graphs with unbounded non-negative weights.
However, specialized cases (such as bounded/integer weights, directed acyclic graphs etc.) can indeed be improved
further as detailed in Specialized variants.

In some fields, artificial intelligence in particular, Dijkstra's algorithm or a variant of it is known as uniform cost
search and formulated as an instance of the more general idea of best-first search.[7]


Extra Credit Project
Implement a working version of Dijkstra's Algorithm following the implementation guidelines shown in the Textbook and in
the slides, subject to the following conditions:
The program should take a directed graph as the input. The input should be represented by an adjacency matrix whose
entries are the costs, i.e., M(i,j) is the cost of edge (i, j). The nodes will be represented with single lower case
letters. The adjacency matrix should be read from a text file whose first row will be the letters for the initial and
final nodes, the costs should be separated by blanks, so an excerpt from your input file could look like:
s t
1.3 2.5 0.0 0.0 4.2 0.0 ...
0.0 0.0 0.7 0.0 3.2 2.1 ...
.
 .
  .
0.0 1.3 0.4 8.2 5.1 0.0 ...
Dijkstra has to run for directed graphs. The node names should not be included in the data. Once you read them you may
refer to them by their indices, in other words, you may label the nodes with their index, so if your index origin is 0,
a data file like:
2 3
0.0 3.3 0.0 4.5
3.3 0.0 5.2 3.1
8.5 5.2 0.2.0.0
4.5 3.1 5.2 0.0

would mean, for example that the cost from node 0 to node 3 would be 4.5, from node 2 to node 0 would be 8.5, etc.

The program should use a priority queue with the ChangeKey(node, value), or ChangePriority(n,v), running in O(log n)
time. If you do not find a library guaranteeing this execution time then you should code the priority queue yourself
following the guidelines in the textbook, so you can be sure it runs in O(log n) time.
You should build your own test cases including simple examples from the slides and the textbook, as well as other cases
built by yourself. Build at least five test sets. Your program should run correctly on those sets and on those that
I may use. The code should be documented with a readme file and with comments inserted in the code. The program should
run when called from a command line in Linux, with the following form:
python myDijkstra(<file>)
where <file> is a string with the name of an input file.
The output should be a sequence of nodes indicating the shortest path (for example, s-b-d-f-t), followed by a line with
the cost of the shortest path indicated as follows: Cost: xxx, where xxx is a number with the cost of the shortest
path. Put all the relevant files and directories within a directory named csc321_extracredit_<your last name>, and then
go to the parent directory and make a tar or a zip file of that directory. Submit this file. If your program earns a
grade higher than or equal to 80% it will substitute your lowest grade in any homework, quiz, exam, or project.

Rubric
Landmark	Weight
Successful compilation	10%
Documentation	10%
Runs on your test cases	40%
Runs on my test cases	20%
Runs in O(m log n) time	20%
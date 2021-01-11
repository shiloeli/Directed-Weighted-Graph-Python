# Directed-Weighted-Graph-Python

<p align="center">
<img src="https://thumbs.gfycat.com/IncomparableSmugCollie-small.gif" width="1100" height="300">
</p>  

<h2>Description</h2>

This project deals with the construction of directed weighted graph starting from the creation of the nodes in the graph,<br>
continues with the creation of the graph itself (such as connecting the nodes in the graph and more) and basic algorithms related to the graph <br>
(paths in the parent link graph and more).<br>
A graph is made up of three interfaces main arranged according to the hierarchy from the creation of a node to the execution of an algorithm on the graph.<br>



class:
---------------

**NodeData class:**<br>
this class represents the set of operations applicable on a node (vertex) in a (directional) weighted graph.<br>
The node in the graph consists of five things:<br>
* key - Unique ID of the node in graph<br>
* info - Contains some characteristic of the node such as color and more .. In this project it stores the parent node.<br>
* tag - Temporal data which can be used be algorithms.<br>
* location - location of this node.<br>
* weight - Weight of the node.<br>
    
**DiGraph class:**<br>
This class represent directed weighted graph<br>
That possible different actions on the graph, node and edge<br>
Graph is represented by:<br>
* Vertices - contains all the nodes in the graph using dictionary.<br>
* neighborsOut - Represents the edges protruding from a node.<br>
* neighborsIn - Represents the edges entering the node.<br>
* MC- number of changes made to the graph.<br>
* edgeSize-number of edges in the graph.<br>

Main functions - add_edge(), add_node(),remove_node(), remove_edge().<br> 

**GraphAlgo class:**<br>
This class represents a Directed (positive) Weighted Graph Theory Algorithms including.<br>
* graph - Is an abstract representation of a set of nodes and edge, each edge has a weight.<br>

Main methods and a brief explanation:<br>
**__init__()** - Initialize the graph.<br>
**get_graph()** - Returns the graph.<br>
**load_from_json()** - load a graph to this graph.<br>
**save_to_json()** - Saves this weighted (directed) graph to the given.<br>
**shortest_path()** - Returns the shortest path from node src to node dest using Dijkstra's Algorithm.<br>
**connected_component()** - This method gets a vertex Finds the Strongly Connected Component (SCC).<br>
**connected_components()** - Finds all the Strongly Connected Component(SCC) in the graph.<br>
**plot_graph()** - Plots the graph.<br>

**PlotGraph class:**<br>
This class is responsible for transferring the graph data to a graphical representation with<br>
the help of the matplotlib library<br>
Main functions:<br>
**have_pos()** - checks whether the graph vertices are positioned.<br>
**random_pos()** - The method guerrilla random points for the position of the vertex.<br>
**paint()** - This method draws the graph.<br>

**Data Structure:**<br>
*directory*-It Because by key you can get a number of values that depend on it.<br>
*List*-Convenient to store values in desired order (and we were required to use it)r.<br>
*PriorityQueue*-Because it has the ability to adjust the position of the object by definition.<br>

>**Algorithms:**<br>
* Dijkstra - Solves the problem of finding the easiest route from a point on the graph to a destination in a weighted graph. Because using this algorithm you can find, at the same time, the fast paths to all the points in the graph.<br>
The algorithm works on a given graph, intentional or unintentional, with non-negative weights on the arcs. The weights in the graph symbolize distance. The shortest route<br> between two points means the route with the lowest amount of weights between the two points.<br>
For more explanation: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm <br>

* DFS - Is an algorithm used to move or search a graph.<br>
Intuitively, the algorithm starts the search from an arbitrary node in the graph and advances along the graph until it gets stuck, then it repeats its traces until it can choose to advance to the node it has not yet reached.<br>
For more explanation: https://en.wikipedia.org/wiki/Depth-first_search <br>

*For more information on project* **Wiki**


<p align="center">
<img src="http://www.up2me.co.il/imgs/35483045.jpg" width="700" height="400">   
</p>




<p align="center">
The game can be played from:
<img src="http://up419.siz.co.il/up3/zwmomgyy2ykj.png" width="50" height="50">      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/IntelliJ_IDEA_Logo.svg/1024px-IntelliJ_IDEA_Logo.svg.png" width="50" height="50"> 
<img src="https://sdtimes.com/wp-content/uploads/2019/03/jW4dnFtA_400x400.jpg" width="50" height="50" background="white">  
 </p>   
 
 
**Authors** @Shilo Elimelech @Lior Atiya


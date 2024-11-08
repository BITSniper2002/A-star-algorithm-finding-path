# A-star-algorithm-finding-path
A simple implementation of A* algorithm for finding path. A* is an algorithm that can be regarded as a combination of BFS and Dijkstra’s Algorithm. It not only tries to find all the paths, but also consider the cost of a path in the meantime. Which can reduce the operation time. 

# Overview
A* algorithm is a path-finding algorithm. It can be regarded as a combination of BFS and Dijkstra’s Algorithm. It will try to find all possible paths and take cost into
consideration in the meantime. Thus, it is more efficient and more practical.

# Introduction
In this part, I will briefly introduce how to use my class A_star to solve a path_finding problem

- Initialization
  - To initialize a class object, you need to specify the graph of your path-finding problem. It can include some obstacles. However, take notice that in my algorithm,
    I assume the graph is in some kind of 2D array format and the obstacles are represented using '*'.
  - The cost function is the Euclidean distance by default.
- Main function
  - The main path-finding algorithm is in `search` function. This function takes two parameters `start` and `end`, representing the start position and the end position.
    I use a priorityqueue to store every position during visited during the algorithm.
    To record path and cost of every position, I create two dictionaries `came_from` and `cost`. Initially, `came_from[start] = None` and <br>
    `cost[start] = 0`.
  - The logic of this algorithm is as follows. While there is some element in the priorityqueue, I will select the one with the least cost and search all its possible neighbors.
    If a neighbor has not been visited before or the cost to this neighbor is less than previous cost, update the cost and add this neighbor to the priorityqueue until the end position
    is reached.
- Visualization
  - For readability, I also define two functions `display_graph` for displaying the finding-path problem graph and `display_path` for displaying the path found.

# Acknowledgement
This work is inspired by [redblobgames](https://www.redblobgames.com/pathfinding/a-star/introduction.html)

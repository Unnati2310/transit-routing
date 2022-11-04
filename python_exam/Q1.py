"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""

import os
def Dij_generator():
    File1 = open("Chicago-Sketch/ChicagoSketch_net.tntp", "r")
    data= my_file.read()
    data_into_list = data.replace('\n', ' ').split(".")
    print(data_into_list)
    File1.close()
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information.
    """
    graph_object = None
    try:
        # Enter your code here
        n=933
        m=2950
        for i in range(n)
        distance[i+1] = INF
        distance[x] = 0
        q.push({0,x})
        while (!q.empty())
        int a = q.top().second 
        q.pop()
        if (processed[a])
        continue
        processed[a] = true

        for (auto u : adj[a])
        int b = u.first, w = u.second
        if (distance[a]+w < distance[b])
        distance[b] = distance[a]+w
        q.push({-distance[b],b});

        return graph_object
    except: 
        return graph_object


def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1
    try:
        # Enter your code here
        return shortest_path_distance
    except:
        return shortest_path_distance

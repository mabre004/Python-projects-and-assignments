#!/usr/bin/python 3
import heapq
import math
import sys
# function to calculate distance from source
def myDijkstra(adj_matrix, src, dest):
    dist = {vertex: float(math.inf) for vertex in range(len(adj_matrix))} # initialize every vertex with infinity
    dist[src] = 0       # initialize the source distance to zero
    prev_nodes = {}   # dictionary for storing the visited nodes
    pq = []           # priority queue used as a python list

    for vertex, distance in dist.items():
        heapq.heappush(pq, (distance, vertex))

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor in range(len(adj_matrix[current_vertex])):
            if adj_matrix[current_vertex][neighbor] != 0:
                distance = dist[current_vertex] + adj_matrix[current_vertex][neighbor]
                if distance < dist[neighbor]:
                    prev_nodes[neighbor] = current_vertex
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

    return dist[dest], prev_nodes
def print_path(src, dest, prev_nodes):
    path_string = str(dest)
    while dest != src:
        dest = prev_nodes[dest]
        path_string = str(dest) + "-" + path_string
    print(path_string)

def matrixreader(filename):
    #making the matrix to a list
    matrix = list()
    #open and readline reads one entire line from the file.
    with open(filename) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            # appends everything the line read into the matrix
            matrix.append(list(map(lambda x: float(x) if cnt > 1 else int(x), line.strip().split(' '))))
            line = fp.readline()
            cnt += 1
    begin, end = matrix.pop(0)
    #return the matrix and the start node and end node
    return matrix, begin, end

def main():
    graph, begin, end = matrixreader(sys.argv[1])
    cost, prev_nodes = myDijkstra(graph, begin, end)
    print_path(begin, end, prev_nodes)
    print(cost)

if __name__ == "__main__":
   main()
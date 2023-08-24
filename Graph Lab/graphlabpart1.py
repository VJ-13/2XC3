from collections import deque

import random
import timeit
import matplotlib.pyplot as plot


#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

#Breadth First Search 2 - Returns a path between two given nodes
def BFS2(G, node1, node2):
    Q = deque([(node1, [node1])])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node, path = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return path + [node]
            if not marked[node]:
                Q.append((node, path + [node]))
                marked[node] = True
    return []



#Breadth First Search 3 - Returns predeccesor dictonary
def BFS3(G, node):
    Q = deque([node])
    marked = {node: True}
    predecessor = {node: None}
    final = {}
    for n in G.adj:
        if n != node:
            marked[n] = False
            predecessor[n] = None
    while len(Q) != 0:
        current_node = Q.popleft()
        for neighbor in G.adj[current_node]:
            if not marked[neighbor]:
                Q.append(neighbor)
                marked[neighbor] = True
                predecessor[neighbor] = current_node
    
    for x in predecessor:
        if predecessor[x] is not None:
            final[x] = predecessor[x]
    return final




#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:            
                if node == node2:
                    return True
                S.append(node)
    return False

#Depth First Search 2 - Returns a path between two given nodes
def DFS2(G, node1, node2):
    S = [(node1, [node1])]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node, path = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            if current_node == node2:
                return path
            for node in G.adj[current_node]:
                if not marked[node]:
                    S.append((node, path + [node]))
    return None

#Depth First Search 3 - Returns predeccesor dictionary
def DFS3(G, node):
    S = [node]
    marked = {node: None}
    final = {}
    while len(S) != 0:
        current_node = S.pop()
        for neighbor in G.adj[current_node]:
            if neighbor not in marked:
                marked[neighbor] = current_node
                S.append(neighbor)
    for x in marked:
        if marked[x] is not None:
            final[x] = marked[x]            
    return final


# Checks for a cycle in graph
def has_cycle(G):
    marked = {}
    for node in G.adj:
        marked[node] = False
    for node in G.adj:
        if not marked[node]:
            if helper(G, node, None, marked):
                return True
    return False

def helper(G, node, parent, marked):
    marked[node] = True
    for neighbor in G.adj[node]:
        if not marked[neighbor]:
            if helper(G, neighbor, node, marked):
                return True
        elif neighbor != parent:
            return True
    return False

# Checks if there is a path that exists between two nodes
def is_connected(G):
    marked = set()
    graph = deque([0])
    while graph:
        node = graph.popleft()
        marked.add(node)
        graph.extend(cell for cell in G.adj[node] if cell not in marked)
    return len(marked) == len(G.adj)
   

#Creates a random graph given i nodes and j edges
def create_random_graph(i, j):
    g = Graph(i)
    edges = []
    for n1 in range(i):
        for n2 in range(n1+1, i):
            edges.append((n1, n2))
    random.shuffle(edges)
    for k in range(j):
        (n1, n2) = edges[k]
        g.add_edge(n1, n2)
    return g


def graphCopy(G):
    length = G.number_of_nodes()
    G_copy = Graph(length)
    for node1 in G.adj.keys():
        for node2 in G.adjacent_nodes(node1):
            G_copy.add_edge(node1, node2)
    return G_copy


#Use the methods below to determine minimum vertex covers
def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


# Testing
# x is the number of nodes
# n is the number of edges
# m is number of graphs
# step is space between

#Experiment 1

# G1 = Graph(10)
# G1.add_edge(0, 1)
# G1.add_edge(0, 4)
# G1.add_edge(0, 7)
# G1.add_edge(1, 2)
# G1.add_edge(2, 3)
# G1.add_edge(4, 5)
# G1.add_edge(5, 6)
# G1.add_edge(7, 8)
# G1.add_edge(8, 9)
# G1.add_edge(2, 8)

# print(is_connected(G1))


def experiment1(x, n, m, step):
    size_plot = []
    cycle_probability = []
    for j in range(0, n+1, step):
        cycle = 0
        size_plot.append(j)
        for _ in range(m):
            print("Experiment 1 running")


            L = create_random_graph(x, j)

            if has_cycle(L):
                cycle += 1

        cycle_probability.append(cycle/m)

    plot.plot(size_plot, cycle_probability)
    plot.ylabel("Cycle Probability")
    plot.xlabel("Number of edges")
    plot.title("Edges vs Cycle Probability")
    plot.legend()
    plot.show()

#Number of nodes should be constant, like 1000
#Change number of edges from 100, 1000, 10000  (More depending on your step)
#Your looking at number of edges vs cycle probability, essentially if the number of edges has an impact on a graph having a cycle
#Repeat this but with number of edges being constant - see if there is any change

# step = 1
# nodes = 100
# edges = 100 # changing
# number_of_lists = 100

# experiment1(nodes, edges, number_of_lists, step)

#Experiment 2

def experiment2(x, n, m, step):
    size_plot = []
    is_connected_probability = []
    for j in range(0, n+1, step):
        connect = 0
        size_plot.append(j)
        for _ in range(m):
            print("Experiment 2 running")
            L = create_random_graph(x, j)

            if is_connected(L) == True:
                connect += 1

        is_connected_probability.append(connect/m)

    plot.plot(size_plot, is_connected_probability)
    plot.ylabel("Connected Probability")
    plot.xlabel("Number of edges")
    plot.title("Edges vs Connected Probability")
    plot.legend()
    plot.show()


#Number of nodes should be constant, like 1000
#Change number of edges from 100, 1000, 10000  (More depending on your step)
#Your looking at number of edges vs connect probability, essentially if the number of edges has an impact on a graph having a path between two nodes
#Repeat this but with number of edges being constant - see if there is any change

step = 10
nodes = 100
edges = 500 # changing
number_of_lists = 100

experiment2(nodes, edges, number_of_lists, step)
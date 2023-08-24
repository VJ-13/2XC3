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
    
    def get_size(self):
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

def create_random_graph(i, j):
    graph = Graph(i)
    edges = []
    for x in range(i):
        for y in range(x+1, i):
            edges.append((x, y))
    random.shuffle(edges)
    for k in range(j):
        (x, y) = edges[k]
        graph.add_edge(x, y)
    return graph
#BFS2 returns the path from node1 to node2
def BFS2(G, node1, node2):
    BFSpath = [node1]
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                BFSpath.append(node2)
                return BFSpath
            if not marked[node]:
                BFSpath.append(node)
                Q.append(node)
                marked[node] = True
    return []

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




#DFS2 returns the path from node1 to node2
def DFS2(G, node1, node2):
    DFSpath = []
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            DFSpath.append(current_node)
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    DFSpath.append(node2)
                    return DFSpath
                if not marked[node]:
                    S.append(node)
    return []


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

def is_independent_set(G, C):
    for start in C:
        for end in G.adj[start]:
            if end in C:
                return False
    return True

def MIS(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    max_cover = []
    for subset in subsets:
        if is_independent_set(G,subset):
            if len(subset) > len(max_cover):
                max_cover = subset
    return max_cover

G1 = Graph(10)
G1.add_edge(0, 1)
G1.add_edge(0, 4)
G1.add_edge(0, 7)
G1.add_edge(1, 2)
G1.add_edge(2, 3)
G1.add_edge(4, 5)
G1.add_edge(5, 6)
G1.add_edge(7, 8)
G1.add_edge(8, 9)


G2 = Graph(7)
G2.add_edge(1, 2)
G2.add_edge(1, 3)
G2.add_edge(2, 4)
G2.add_edge(3, 4)
G2.add_edge(3, 5)
G2.add_edge(4, 6)
G2.add_edge(5, 4)

G3 = Graph(5)
G3.add_edge(0,1)
G3.add_edge(1,2)
G3.add_edge(2,3)
G3.add_edge(3,4)
G3.add_edge(4,0)


# Helper Functions
def graphCopy(G):
    length = G.number_of_nodes()
    G_copy = Graph(length)
    for node1 in G.adj.keys():
        for node2 in G.adjacent_nodes(node1):
            G_copy.add_edge(node1, node2)
    return G_copy


def removeNode(G, node1):
    G.adj.pop(node1)
    for node in G.adj.keys():
        if node1 in G.adj[node]:
            G.adj[node].remove(node1)


def approx1(G):
    #1. start with empty set
    C = set()
    G_copy = graphCopy(G)
    #5 stops if is vertex cover 
    while is_vertex_cover(G, C) == False:
        nodesLength = {}
        #2 find highest degree
        for node in G_copy.adj:
            nodesLength[node] = len(G_copy.adj[node])
        maxLength = max(nodesLength.values())

        for node in G_copy.adj:
            if len(G_copy.adj[node]) == maxLength and node not in C:
                highestDegree = node
                break
        #3 add highest vertex to C
        C.add(highestDegree)
        #4 remove node
        removeNode(G_copy, highestDegree)
    return C




def approx2(G):
    #1 c = set()
    C = set()
    G_copy = graphCopy(G)
    #4 end when is vertex cover
    while is_vertex_cover(G, C) == False:
        #2 random vertex
        randomNode = random.choice(list(G_copy.adj.keys()))
        #3 add random vertex
        C.add(randomNode)
    return C


def approx3(G):
    G_copy = graphCopy(G)
    C = set()
    while is_vertex_cover(G, C) == False:
        node1 = random.choice(list(G_copy.adj.keys()))

        # If node1 has no neighbors, choose a new node
        while len(G_copy.adj[node1]) == 0:
            node1 = random.choice(list(G_copy.adj.keys()))

        node2 = random.choice(G_copy.adj[node1])

        C.add(node1)
        C.add(node2)
        
        removeNode(G_copy, node1)
        removeNode(G_copy, node2)
    return C

size_plot = []
def expirement1a(nodes, max_edges, runs):
    total1 = []
    total2 = []
    total3= []
    total4 = []
    totalAll = []
    G_expirement = Graph(nodes) 
    sum_acc = 0
    sum_aprox1 = 0
    sum_aprox2 = 0
    sum_aprox3 = 0

    for i in range(1, max_edges):
        size_plot.append(i)
        for j in range(i):
            f = random.sample(list(G_expirement.adj.keys()), 2)
            G_expirement.add_edge(f[0], f[1])

        for i in range(runs):
            G_copy1 = graphCopy(G_expirement)
            G_copy2 = graphCopy(G_expirement)
            G_copy3 = graphCopy(G_expirement)
            G_copy4 = graphCopy(G_expirement)

            sum_acc += len(MVC(G_copy1))
            sum_aprox1 += len(approx1(G_copy2))
            sum_aprox2 += len(approx2(G_copy3))
            sum_aprox3 += len(approx3(G_copy4))




        #total1.append(sum_acc)
        #print(total1)
        total2.append(sum_aprox1/sum_acc)
        #print(total2)
        total3.append(sum_aprox2/sum_acc)
        #print(total3)
        total4.append(sum_aprox3/sum_acc)
        #print(total4)
        totalAll.append(total2)
        totalAll.append(total3)
        totalAll.append(total4)
    
    return totalAll

size_plot2 = []
def expirement1b(max_nodes, edges, runs):
    total1 = []
    total2 = []
    total3= []
    total4 = []
    totalAll = []
    sum_acc = 0
    sum_aprox1 = 0
    sum_aprox2 = 0
    sum_aprox3 = 0

    for i in range(5, max_nodes):
        G_expirement = Graph(i) 
        print(size_plot2)

        size_plot2.append(i)
        for j in range(edges):
            f = random.sample(list(G_expirement.adj.keys()), 2)
            G_expirement.add_edge(f[0], f[1])

        for i in range(runs):
            G_copy1 = graphCopy(G_expirement)
            G_copy2 = graphCopy(G_expirement)
            G_copy3 = graphCopy(G_expirement)
            G_copy4 = graphCopy(G_expirement)

            sum_acc += len(MVC(G_copy1))
            sum_aprox1 += len(approx1(G_copy2))
            sum_aprox2 += len(approx2(G_copy3))
            sum_aprox3 += len(approx3(G_copy4))




        total1.append(sum_acc)
        #print(total1)
        total2.append(sum_aprox1/sum_acc)
        #print(total2)
        total3.append(sum_aprox2/sum_acc)
        #print(total3)
        total4.append(sum_aprox3/sum_acc)

        #print(total4)
        totalAll.append(total2)
        totalAll.append(total3)
        totalAll.append(total4)


    
    return totalAll
size_plot3 = []
def expirement1c(nodes, max_edges, runs):
    total1 = []
    total2 = []
    total3= []
    total4 = []
    totalAll = []
    G_expirement = Graph(nodes) 


    for i in range(1, max_edges):
        time1 = 0
        time2 = 0
        time3 = 0
        time4 = 0
        size_plot3.append(i)
        for j in range(i):
            f = random.sample(list(G_expirement.adj.keys()), 2)
            G_expirement.add_edge(f[0], f[1])

        for i in range(runs):
            G_copy1 = graphCopy(G_expirement)
            G_copy2 = graphCopy(G_expirement)
            G_copy3 = graphCopy(G_expirement)

            start1 = timeit.default_timer()
            approx1(G_copy1)
            end1 = timeit.default_timer()
            time1 += end1 - start1


            start2 = timeit.default_timer()
            approx2(G_copy2)
            end2 = timeit.default_timer()
            time2 += end2 - start2
            

            start3 = timeit.default_timer()
            approx3(G_copy3)
            end3 = timeit.default_timer()
            time3 += end3 - start3




        
        #print(total1)
        total1.append(time1/runs)
        #print(total2)
        total2.append(time2/runs)
        #print(total3)
        total3.append(time3/runs)
        #print(total4)
        
        totalAll.append(total1)

        totalAll.append(total2)
        totalAll.append(total3)
    
    return totalAll

size_plot4 = []
def expirement1d(max_nodes, edges, runs):
    total1 = []
    total2 = []
    total3= []
    total4 = []
    totalAll = []
    

    for i in range(5, max_nodes):
        time1 = 0
        time2 = 0
        time3 = 0
        G_expirement = Graph(i) 

        size_plot4.append(i)
        for j in range(edges):
            f = random.sample(list(G_expirement.adj.keys()), 2)
            G_expirement.add_edge(f[0], f[1])

        for i in range(runs):
            G_copy1 = graphCopy(G_expirement)
            G_copy2 = graphCopy(G_expirement)
            G_copy3 = graphCopy(G_expirement)

            start1 = timeit.default_timer()
            approx1(G_copy1)
            end1 = timeit.default_timer()
            time1 += end1 - start1


            start2 = timeit.default_timer()
            approx2(G_copy2)
            end2 = timeit.default_timer()
            time2 += end2 - start2
            

            start3 = timeit.default_timer()
            approx3(G_copy3)
            end3 = timeit.default_timer()
            time3 += end3 - start3





        total2.append(time1/runs)
        #print(total2)
        total3.append(time2/runs)
        #print(total3)
        total4.append(time3/runs)
        #print(total4)
        totalAll.append(total2)
        totalAll.append(total3)
        totalAll.append(total4)


    
    return totalAll
size_plot5 = []
def experiment4_1(n, maxEdges):
    total1 = []
    total2 = []
    total3 = []
    totalAll = []

    for i in range(maxEdges+1):
        size_plot5.append(i)
        Graph = create_random_graph(n, i)
        mVc = len(MVC(Graph))
        mIs = len(MIS(Graph))
        total1.append(mVc)
        total2.append(mIs)
        total3.append(mVc + mIs)
        totalAll.append(total1)
        totalAll.append(total2)
        totalAll.append(total3)
        # print(f"G has {Graph.number_of_nodes()} nodes and {edge} edges")
        # print(f"Number of nodes in G   : {str(Graph.number_of_nodes())}")
        # print(f"Length of MVC          : {str(len(mVc))}")
        # print(f"Length of MIS          : {str(len(mIs))}")
        # print("------------------------------------------------------")
    return totalAll


        



# nodes = 8
# max_edges = 30
# runs = 1000
# totals = expirement1a(8,30,1000)
# plot.plot(size_plot, totals[0], label = "aprox1")
# plot.plot(size_plot, totals[1], label = "aprox2")
# plot.plot(size_plot, totals[2], label = "aprox3")

# plot.ylabel("approx MVC/actual MVC")
# plot.xlabel("edges")
# plot.title("ratio of the size of the approx. MVC vs the actual MVC over increasing edges")
# plot.legend()
# plot.show()
max_nodes = 20
edges = 20
runs = 100
# totals = expirement1b(20,20,100)
# plot.plot(size_plot2, totals[0], label = "aprox1")
# plot.plot(size_plot2, totals[1], label = "aprox2")
# plot.plot(size_plot2, totals[2], label = "aprox3")

# plot.ylabel("approx MVC /actual MVC")
# plot.xlabel("nodes")
# plot.title("ratio of the size of the approx. MVC vs the actual MVC over increasing nodes")
# plot.legend()
# plot.show()

# totals = expirement1c(12,60,1000)
# plot.plot(size_plot3, totals[0], label = "aprox1")
# plot.plot(size_plot3, totals[1], label = "aprox2")
# plot.plot(size_plot3, totals[2], label = "aprox3")


# plot.ylabel("time")
# plot.xlabel("number of edges")
# plot.title("time taken to find approximate MVC vs number of edges")
# plot.legend()
# plot.show()

# totals = expirement1d(30,20,100)
# plot.plot(size_plot4, totals[0], label = "aprox1")
# plot.plot(size_plot4, totals[1], label = "aprox2")
# plot.plot(size_plot4, totals[2], label = "aprox3")

# plot.ylabel("time")
# plot.xlabel("number of nodes")
# plot.title("time taken to find approximate MVC vs number of nodes")
# plot.legend()
# plot.show()

# totals = experiment4_1(10, 45)
# plot.plot(size_plot5, totals[0], label = "MVC")
# plot.plot(size_plot5, totals[1], label = "MIS")

# plot.ylabel("length")
# plot.xlabel("number of edges")
# plot.title("MVC size vs MIS size")
# plot.legend()
# plot.show()

# totals = experiment4_1(10, 45)
# plot.plot(size_plot5, totals[2], label = "MVC")


# plot.ylabel("length")
# plot.xlabel("number of edges")
# plot.title("MVC size vs MIS size")
# plot.legend()
# plot.show()
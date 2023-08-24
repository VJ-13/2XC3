import matplotlib.pyplot as plot
class iXC3Tree:
    def __init__(self):
        self.rootnode = None

    def get_degree(self):
        if self.rootnode == None:
            return 0
        else:
            return self.rootnode.degree

    def tree_height(self):
        if self.rootnode == None:
            return 0
        if self.rootnode.degree == 0:
            return 1
        else:
            f = []
            for child in self.rootnode.kids:
                f.append(self.tree_height2(child))
            return max(f) + 1

    def treeSize(self):
        size = 1
        if self.rootnode == None:
            return 0
        for child in self.rootnode.kids:
            if child != None:
                size += self.treeSize2(child)
        return size

    def tree_height2(self, node):
        if node == None:
            return 0
        if node.degree == 0:
            return 1
        else:
            f = []
            for child in node.kids:
                f.append(self.tree_height2(child))

        return max(f) + 1
    
    def treeSize2(self, node):
        size = 1
        if node == None:
            return 0
        for child in node.kids:
            if child != None:
                size += self.treeSize2(child)
        return size

    def complete(self):
        if self.rootnode is None:
            return True
        else:
            return self.rootnode.complete()

    def insert(self):
        if self.rootnode is None:
            self.rootnode = iXC3Node(0)
        else:
            if self.rootnode.complete():
                self.rootnode.increment_degree()
            self.rootnode.insert()

class iXC3Node:
    def __init__(self, degree):
        self.degree = degree
        self.kids = [None for i in range(degree)]
        self.pred = None
        if self.degree != 0:
            self.full = False
        else:
            self.full = True

    def increment_degree(self):
        self.degree += 1
        self.kids.append(None)
        self.update_full()

    def get_level(self):
        if self.pred is None:
            return 0
        return 1 + self.pred.get_level()
        

    def insert(self):
        for i in range(len(self.kids)):
            child = self.kids[i]
            if child == None:
                if i > 1:
                    degree = i - 1
                else:
                    degree = 0
                self.kids[i] = iXC3Node(degree)
                self.kids[i].pred = self
                self.update_full()
                return
            if not child.complete():
                child.insert()

    def complete(self):
        return self.full

    def update_full(self):
        p = self.full
        for child in self.kids:
            if(child == None or not child.complete()):
                self.full = False
                if(p != self.full and self.pred is not None):
                    self.pred.update_full()
                return
        self.full = True
        if(p != self.full and self.pred is not None):
            self.pred.update_full()







size_plot = []
def expirement_3():
    X = iXC3Tree()

    trees = []
    treesAll = []
    for i in range(1000):
        X.insert()
        
        size_plot.append(X.get_degree())
        trees.append(X.tree_height())
    
    treesAll.append(trees)
        
    return treesAll

def expirement_4():
    X = iXC3Tree()

    trees = []
    treesAll = []
    for i in range(1000):
        X.insert()
        
        size_plot.append(X.get_degree())
        trees.append(X.treeSize())
    
    treesAll.append(trees)
        
    return treesAll


times = expirement_4()

plot.plot(size_plot, times[0], label = "Tree height")

plot.ylabel("Tree height")
plot.xlabel("Tree degree")
plot.title("Expirement 3")
plot.legend()
plot.show()

# plot.plot(size_plot, times[0], label = "Tree degree vs tree size")

# plot.ylabel("Tree size")
# plot.xlabel("Tree degree")
# plot.title("Tree degree vs tree size")
# plot.legend()
# plot.show()
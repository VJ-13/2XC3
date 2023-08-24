import random
import matplotlib.pyplot as plot
import sys
sys.setrecursionlimit(5000)



class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        if self.parent is None:
            return False
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent is None:
            return None
        elif self.is_left_child():
            return self.parent.right
        else:
            return self.parent.left

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        if self.left is None:
            return

        new_root = self.left
        self.left = new_root.right

        if new_root.right is not None:
            new_root.right.parent = self

        new_root.parent = self.parent

        if self.parent is None:
            # self is root, update root
            self.__class__.root = new_root
        elif self.is_left_child():
            self.parent.left = new_root
        else:
            self.parent.right = new_root

        new_root.right = self
        self.parent = new_root

    def rotate_left(self):
        if self.right is None:
            return

        new_root = self.right
        self.right = new_root.left

        if new_root.left is not None:
            new_root.left.parent = self

        new_root.parent = self.parent

        if self.parent is None:
            # self is root, update root
            self.__class__.root = new_root
        elif self.is_left_child():
            self.parent.left = new_root
        else:
            self.parent.right = new_root

        new_root.left = self
        self.parent = new_root



class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        while node.parent is not None and node.parent.is_red():
            grandparent = node.parent.parent
            if grandparent is None or not grandparent.is_red():
                break
            if node.parent == grandparent.left:
                uncle = grandparent.right
                if uncle is not None and uncle.is_red():
                    node.parent.make_black()
                    uncle.make_black()
                    grandparent.make_red()
                    node = grandparent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        node.rotate_left()
                    node.parent.make_black()
                    grandparent.make_red()
                    grandparent.rotate_right()
            else:
                uncle = grandparent.left
                if uncle is not None and uncle.is_red():
                    node.parent.make_black()
                    uncle.make_black()
                    grandparent.make_red()
                    node = grandparent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        node.rotate_right()
                    node.parent.make_black()
                    grandparent.make_red()
                    grandparent.rotate_left()

        self.root.make_black()
                    
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    root = None

    def insert(self, val):
        node = Node(val)
        if (self.root == None):
            self.root = node
            return
        prev = None
        temp = self.root
        while (temp != None):
            if (temp.val > val):
                prev = temp
                temp = temp.left
            elif (temp.val <= val):
                prev = temp
                temp = temp.right
        if (prev.val > val):
            prev.left = node
        else:
            prev.right = node


    def height(self):
        if self.root == None:
            return 0

        q = []
        
        q.append(self.root)
        height = 0
    
        while(True):
            
    
            nodeCount = len(q)
            if nodeCount == 0 :
                return height
        
            height += 1

            while(nodeCount > 0):
                node = q[0]
                q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
    
                nodeCount -= 1 

        


def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L



def experiment1(length, runs, step):
    diffs = 0
    avgdiffs = []
    for j in range(1, length+1, step):
        for _ in range(0, runs):
            bst = BST()
            rbt = RBTree()
            L = create_random_list(length, length)

            for val in L:
                bst.insert(val)
                rbt.insert(val)
            
            bstH = bst.height()
            rbtH = rbt.get_height()
            print("Experiment 1 Running")
            print("bstH: " , bstH , "rbtH:" , rbtH, "size: " , j)

            diff = bstH - rbtH
            diffs += diff


        avgdiffs.append(diffs / (runs))

    avgdiff = 0
    for val in avgdiffs:
        avgdiff += val
    
    avgdiff /= len(avgdiffs)
    print(avgdiff)

def experiment2(length, runs, step, swaps):
    swapSize = []
    avgdiffs = []
    bstHi = []
    rbtHi = []
  
    for numSwap in range(0, swaps, step):
        diffs = 0
        bstT = 0
        rbtT = 0
        swapSize.append(numSwap)
        for _ in range(0, runs): 
            rbt = RBTree()
            bst = BST()
            L = create_near_sorted_list(length, length, numSwap)


            for val in L:
                bst.insert(val)
                rbt.insert(val)

            bstH = bst.height()
            rbtH = rbt.get_height()
            print("Experiment 2 Running")
            # print("bstH: " , bstH , "rbtH:" , rbtH, "size: " , j)

            diff = bstH - rbtH
            diffs += diff
            bstT += bstH
            rbtT += rbtH

        avgdiffs.append(diffs / runs)
        bstHi.append(bstT/runs)
        rbtHi.append(rbtT/runs)

                
    plot.plot(swapSize, avgdiffs, label = "Average Height Differnce")

    plot.plot(swapSize, bstHi, label = "Binary Search Tree Height")

    plot.plot(swapSize, rbtHi, label = "Red Black Tree Height")

    plot.ylabel("Average Height Difference")
    plot.xlabel("Number of Swaps")
    plot.title("Average Height Difference between BSTs and RBTs over number of swaps ")
    plot.legend()
    plot.show()


    

# experiment1(1000, 10, 100)

# experiment2(10000, 100, 100, 10000)






    


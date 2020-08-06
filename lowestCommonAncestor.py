class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''
# recursive solution
def lca(root, v1, v2):
    if min(v1, v2) > root.info:
        # checks if root is smaller than both (if smaller than the min then it must be smaller than the max)
        return lca(root.right, v1, v2)
    elif max(v1, v2) < root.info:
        # checks if root is bigger than both (if bigger than the max then it must be bigger than the min)
        return lca(root.left, v1, v2)
    else:
        # if not smaller than both or bigger than both, its is the LCA
        return root

# non recursive
def lca(root, v1, v2):
    if v1 > v2:
        v1, v2 = v2, v1
    while True:
        if root.info > v2: # current root is out of range, on the right side
            root = root.left # tries to find a more left number
        elif root.info < v1: # current root is out of range, on the left side
            root = root.right # tries to find a more right number
        else:
            return root

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)

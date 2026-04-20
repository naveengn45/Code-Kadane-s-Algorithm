class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Key is greater than root's key
    if root.val < key:
        print(f"Checking right subtree of {root.val}...")
        return search(root.right, key)
   
    # Key is smaller than root's key
    print(f"Checking left subtree of {root.val}...")
    return search(root.left, key)

# --- Let's build the tree ---
#        10
#       /  \
#      5    15
#     / \
#    2   7

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

# --- Test the search ---
target = 10
print(f"Searching for {target}:")
result = search(root, target)

if result:
    print(f"Found node with value: {result.val}")
else:
    print("Value not found in tree.")
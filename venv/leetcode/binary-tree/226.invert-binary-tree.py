class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive answer
def invertTree(root):
    if not root:
        return None
    if root.left:
        invertTree(root.left)
    if root.right:
        invertTree(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp

    # Using a temporary tuple (similar to the original but more explicit)
    # root.left, root.right = (root.right, root.left)
    return root


# Helper function to print the tree (in-order traversal)
def print_tree(node):
    if not node:
        return
    print(node.val, end=' ')
    print_tree(node.left)
    print_tree(node.right)

# Sample binary tree:
#       4
#      / \
#     2   7
#    / \ / \
#   1  3 6  9

# Create the sample tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Original tree (in-order):")
print_tree(root)  # Output: 4 2 1 3 7 6 9

# Invert the tree
inverted_root = invertTree(root)

print("\nInverted tree (in-order):")
print_tree(inverted_root)  # Output: 4 7 9 6 2 3 1
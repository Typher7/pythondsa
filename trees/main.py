class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        if not self.root:
            self.root = BinaryTreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.val:
            if not node.left:
                node.left = BinaryTreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if not node.right:
                node.right = BinaryTreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def search_node(self, current_node, node):
        if not current_node:
            return False

        if current_node.val == node.val:
            return True
    
        elif node.val < current_node.val:
            return self.search_node(current_node.left, node)

        else:
            return self.search_node(current_node.right, node)
                
    
    def inOrder(self, root):
        if not root:
            return 
        
        self.inOrder(root.left)
        print(root.val, end = " --> ")
        self.inOrder(root.right)
 
    
    def preOrder(self, root):
        if not root:
            return 
        
        print(root.val, end = " --> ")
        self.inOrder(root.left)
        self.inOrder(root.right)
 
    
    def postOrder(self, root):
        if not root:
            return 
        
        self.inOrder(root.left)
        self.inOrder(root.right)
        print(root.val, end = " --> ")
 
    

bin_tree=BinaryTree()

nums=[2,1,3,6,4,5]
for i in nums:
    bin_tree.insert_node(i)

#print(bin_tree.preOrder(bin_tree.root))
print(bin_tree.inOrder(bin_tree.root))
#print(bin_tree.postOrder(bin_tree.root))
node=BinaryTreeNode(0)
print(bin_tree.search_node(bin_tree.root, node))


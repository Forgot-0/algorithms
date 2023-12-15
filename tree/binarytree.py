

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f'{self.data} -> ({self.left}, {self.right})'
        
    def __repr__(self) -> str:
        return f'{self.data}'


class Tree:
    def __init__(self, root) -> None:
        self.root = root

    def add_while(self, data) -> None:
        node = Node(data)
        root = self.root
        while True:
            if data < root.data:
                if root.left == None:
                    print(root)
                    root.left = node
                    break
                
                root = root.left

            elif data > root.data:
                if root.right == None:
                    root.right = node
                    break

                root = root.right
            else:
                return 
            
    def add_recursion(self, data) -> None:
        return self._add_recursion(data, self.root)

    def _add_recursion(self, data, node: Node) -> None:
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                return self._add_recursion(data, node.left)
        elif data > node.data:
            if node.right == None:
                node.right = Node(data)
            else:
                return self._add_recursion(data, node.right)

    def search(self, value) -> Node | None:
        return self._search(self.root, value)

    def _search(self, node, value):
        if node == None: return None
        if node.data == value: return node
        return self._search(node.left, value) if value < node.data else self._search(node.right, value)

    # def recursion_show(self, node: Node):
    #     if node == None:
    #         return
    #     self.recursion_show(node.left)
    #     print(node.data)
    #     self.recursion_show(node.right)

    def breadth_first(self):
        ans = []
        nodes = [self.root]
        
        while nodes:
            node = nodes.pop(0)
            ans.append(node)

            if node.left:
                nodes.append(node.left)

            if node.right:
                nodes.append(node.right)
            
                
        return ans
    
    def getMax(self) -> Node:
        return self._getMax(self, self.root)
    
    def _getMax(self, node: Node) -> Node:
        if node == None: return None
        if node.right == None: return node
        return self._getMax(node.right)
    
    def getMin(self) -> Node:
        return self._getMin(self, self.root)
    
    def _getMin(self, node: Node) -> Node:
        if node == None: return None
        if node.left == None: return node
        return self._getMax(node.left)


    def __str__(self) -> str:
        return f'{self.root}'


n1 = Node(5)
tree = Tree(n1)


tree.add_recursion(3)
tree.add_recursion(7)
tree.add_recursion(2)
tree.add_recursion(6)
tree.add_recursion(8)
print(tree.breadth_first())
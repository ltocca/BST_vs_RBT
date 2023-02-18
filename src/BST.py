# Implementazione Alberi Binari di Ricerca (basato sulle slide di Laboratorio di Algoritmi 20/21)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def get(self):  # Getter
        return self.key

    def set(self, key):  # Setter key
        self.key = key

    def get_children(self):
        children = []  # Vettore
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children


class BST:
    def __init__(self):
        self.root = None

    def set_root(self, key):
        self.root = Node(key)

    def insert_node(self, current_node, key):
        if key <= current_node.key:
            if current_node.left:  # si passa al prossimo nodo a sx ricorsivamente
                self.insert_node(current_node.left, key)
            else:
                current_node.left = Node(key)
                current_node.left.parent = current_node
        elif key > current_node.key:
            if current_node.right:
                self.insert_node(current_node, key)
            else:
                current_node.right = Node(key)
                current_node.right.parent = current_node

    def insert(self, key):
        x = self.root
        p = None
        while x is not None:
            p = x
            if key <= x.key:
                x = x.left
            else:
                x = x.right

        if p is None:
            self.set_root(key)
        elif key <= p.key:
            p.left = Node(key)
            p.left.parent = p
        else:
            p.right = Node(key)
            p.right.parent = p

    def node_height(self, node):
        current_level = [node]
        count = 0
        while current_level:
            next_level = list()
            for n in current_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            count += 1
            current_level = next_level
        return count

    def height(self):
        if self.root is None:
            return 0
        return self.node_height(self.root)

    def _t_min(self, x):
        while x.left is not None:
            x = x.left
        return x

    def t_min(self):
        return self._t_min(self.root)

    def _t_max(self, x):
        while x.right is not None:
            x = x.right
        return x

    def t_max(self):
        return self._t_max(self.root)

    def find(self, key):
        return self.find_node(self.root, key)

    def find_node(self, x, k):
        while x is not None and k is not x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def in_order(self):
        nodes = []

        def _in_order(v):
            if v is None:
                print("Empty Tree!")
                return
            if v.left is not None:
                _in_order(v.left)
            nodes.append(v.key)
            if v.right is not None:
                _in_order(v.right)

        _in_order(self.root)
        print(nodes)

    def in_order_rev(self):
        def _in_order_rev(v):
            if v is None:
                print("Empty Tree!")
                return
            if v.right is not None:
                _in_order_rev(v.right)
            print(v.key)
            if v.left is not None:
                _in_order_rev(v.left)

        _in_order_rev(self.root)

    def pre_order(self):
        def _pre_order(v):
            if v is None:
                print("Empty Tree!")
                return
            print(v.key)
            if v.left is not None:
                _pre_order(v.left)
            if v.right is not None:
                _pre_order(v.right)

        _pre_order(self.root)

    def post_order(self):
        def _post_order(v):
            if v is None:
                print("Empty Tree!")
                return
            if v.left is not None:
                _post_order(v.left)
            if v.right is not None:
                _post_order(v.right)
            print(v.key)

        _post_order(self.root)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def tree_delete(self, x):
        z = self.find(x)
        if z is None:
            print("Node is not in the tree!")
            return
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.t_min()
            if y.parent is not z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            z.left.parent = y


def main():
    tree = BST()
    # tree.insert(4)
    # tree.insert(5)
    for x in range(20, 10, -1):
        tree.insert(x)
    print(tree.find(5))
    print(tree.find(2))
    tree.in_order()
    print(tree.height())
    if tree.find(17):
        print("found")
    print(tree.height())


if __name__ == "__main__":
    main()

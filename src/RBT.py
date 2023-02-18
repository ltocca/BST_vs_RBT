BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'  # ricordati che serve per le foglie -> colore padre della radice


class ColouredNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.colour = BLACK

    def set_colour(self, colour):
        self.colour = colour


class RBT:
    def __init__(self):
        self.nil = ColouredNode(None)
        self.root = self.nil

    def set_root(self, key):
        x = ColouredNode(key)
        x.set_colour(BLACK)
        x.parent = self.nil
        self.root = x

    def _t_min(self, x):
        while x.left is not self.nil:
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
        x = self.root
        if x is self.nil:
            return 0
        return self.node_height(x)

    def find(self, k):
        return self.find_node(self.root, k)

    def find_node(self, current_node, key):
        if current_node is self.nil:
            print("Key not found")
            return False
        elif key == current_node.key:
            return current_node
        if key < current_node.key:
            return self.find_node(current_node.left, key)
        else:
            return self.find_node(current_node.right, key)

    def in_order(self):
        nodes = []

        def _in_order(v):
            if self.root is None:
                print("Empty Tree!")
                return
            if v.left is not None and v.left is not self.nil:
                _in_order(v.left)
            nodes.append(str(v.key) + ": " + v.colour)
            if v.right is not None and v.right is not self.nil:
                _in_order(v.right)

        _in_order(self.root)
        print(nodes)

    def in_order_rev(self):
        nodes = []

        def _in_order_rev(v):
            if self.root is None:
                print("Empty Tree!")
                return
            if v.right is not None and v.right is not self.nil:
                _in_order_rev(v.right)
            nodes.append(str(v.key) + ": " + v.colour)
            if v.left is not None and v.left is not self.nil:
                _in_order_rev(v.left)

        _in_order_rev(self.root)
        print(nodes)

    def pre_order(self):
        nodes = []

        def _pre_order(v):
            if self.root is None:
                print("Empty Tree!")
                return
            nodes.append(str(v.key) + ": " + v.colour)
            if v.left is not None and v.left is not self.nil:
                _pre_order(v.left)
            if v.right is not None and v.right is not self.nil:
                _pre_order(v.right)

        _pre_order(self.root)
        print(nodes)

    def post_order(self):
        nodes = []

        def _post_order(v):
            if self.root is self.nil:
                print("Empty Tree!")
                return
            if v.left is not None and v.left is not self.nil:
                _post_order(v.left)
            if v.right is not None and v.right is not self.nil:
                _post_order(v.right)
            nodes.append(str(v.key) + ": " + v.colour)

        _post_order(self.root)
        print(nodes)

    # number of BLACK nodes on any simple path from, but not including, a node x down to a leaf
    def black_height(self, x):
        i = 0
        while x is not self.nil:
            if x.colour is BLACK:
                i += 1
            x = x.left
        return i

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is self.nil:
            self.root = x
        elif y is y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert_fixup(self, z):
        while z.parent.colour is RED:
            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right
                if y.colour is RED:
                    z.parent.colour = BLACK
                    y.colour = BLACK
                    z.parent.parent.colour = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.colour = BLACK
                    z.parent.parent.colour = RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.colour is RED:
                    z.parent.colour = BLACK
                    z.parent.parent.colour = RED
                    y.colour = BLACK
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.colour = BLACK
                    z.parent.parent.colour = RED
                    self.left_rotate(z.parent.parent)
        self.root.colour = BLACK

    def insert(self, key):
        z = ColouredNode(key)
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.colour = RED
        self.insert_fixup(z)

    def rb_transplant(self, u, v):
        if u.parent is self.nil:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_fixup(self, x):
        while x is not self.root and x.colour is BLACK:
            if x is x.parent.left:
                w = x.parent.right
                if w.colour is RED:
                    w.colour = BLACK
                    x.parent.colour = RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.colour is BLACK and w.right.colour is BLACK:
                    w.colour = RED
                    x = x.parent
                else:
                    if w.right.colour is BLACK:
                        w.left.colour = BLACK
                        w.colour = RED
                        self.right_rotate(w)
                        w = x.parent.right
                w.colour = x.parent.colour
                x.parent.colour = BLACK
                w.right.colour = BLACK
                self.left_rotate(x.parent)
                x = self.root
            else:
                w = x.parent.left
                if w.colour is RED:
                    w.colour = BLACK
                    x.parent.colour = RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.colour is BLACK and w.left.colour is BLACK:
                    w.colour = RED
                    x = x.parent
                else:
                    if w.left.colour is BLACK:
                        w.right.colour = BLACK
                        w.colour = RED
                        self.left_rotate(w)
                        w = x.parent.left
                w.colour = x.parent.colour
                x.parent.colour = BLACK
                w.left.colour = BLACK
                self.right_rotate(x.parent)
                x = self.root
        x.colour = BLACK

    def rb_delete(self, key):
        z = self.find_node(self.root, key)
        y = z
        y_original_colour = y.colour
        if z.left is self.nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right is self.nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self._t_min(z.right)
            y_original_colour = y.colour
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.colour = z.colour
        if y_original_colour is BLACK:
            self.delete_fixup(x)


def main():
    t = RBT()
    t.insert(6)
    t.insert(9)
    t.insert(8)
    t.insert(7)
    t.insert(10)

    t.in_order()

    t.rb_delete(8)
    t.pre_order()
    t.post_order()
    #t.in_order_rev()
    print(t.black_height(t.root))


if __name__ == "__main__":
    main()

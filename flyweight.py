class TreeType:
    def __init__(self, name, color):
        # Initialize TreeType with name and color
        self.name = name
        self.color = color

    def draw(self, x, y):
        # Simulate drawing the tree at given coordinates
        print(f"Drawing {self.color} {self.name} tree at ({x}, {y})")

class TreeFactory:
    tree_types = {}

    @staticmethod
    def get_tree_type(name, color):
        # Get or create a tree type from the factory
        if (tree_type := TreeFactory.tree_types.get(name)) is None:
            tree_type = TreeType(name, color)
            TreeFactory.tree_types[name] = tree_type
        return tree_type

class Tree:
    def __init__(self, x, y, tree_type):
        # Initialize Tree with coordinates and a tree type
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        # Draw the tree using its tree type at its coordinates
        self.tree_type.draw(self.x, self.y)

# Usage example
# Create a TreeFactory instance
factory = TreeFactory()

# Create some trees using shared flyweight tree types
tree1 = Tree(1, 2, factory.get_treself.e_type("Pine", "Green"))
tree1.draw()

tree2 = Tree(3, 4, factory.get_tree_type("Pine", "Green"))
tree2.draw()

tree3 = Tree(5, 6, factory.get_tree_type("Maple", "Red"))
tree3.draw()


#
#
# class TreeType:
#     def __init__(self,name ,color):
#         self.name = name
#         self.color = color
#     def draw(self,x,y):
#         print(f"{self.name} {self.color} TREE AT {x} {y}")
#
# class TreeFactory:
#     tree_types = {}
#
#     @staticmethod
#     def get_tree_type():
#         if (tree_types := factory)

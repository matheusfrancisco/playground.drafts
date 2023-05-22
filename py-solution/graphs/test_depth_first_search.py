"""
You're given a Node class that has a name and an array of optional children nodes.
When put together, nodes from  an acyclic tree-like structure.

Implement the depth_first_search method on the node class, 
which takes in an empty array, traverses the tree using the Depth
first search approach (specifically navigation the tree from left to  right),
stores all of the nodes' names in the input array and returns it



"""
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array


def test_depth_search_first():
    """
      graph =  A
            /  | \'
          B    C   D
        /  \'      / \'
      E    F     G   H
          / \'   \'
          I  J     K
    """
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    assert graph.depth_first_search([]) == ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"] # noqa

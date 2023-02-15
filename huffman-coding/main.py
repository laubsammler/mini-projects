from abc import ABC, abstractmethod

class TreeNodeTraits(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def weight(self):
        pass

    def __lt__(self, other):
        return self.weight() < other.weight()

class Leaf(TreeNodeTraits):
    def __init__(self, value, weight):
        self.value = value
        self._weight = weight

    def weight(self):
        return self._weight

    def __str__(self) -> str:
        return "%s" % self.value

    def print(self):
        print(str(self))

    def __lt__(self, other):
        return self.weight() < other.weight()

class Node(TreeNodeTraits):
    def __init__(self, left, right):
        # minimum
        self.left = left
        # second minimum
        self.right = right

    def children(self):
        return (self.left, self.right)

    def weight(self):
        return self.left.weight() + self.right.weight()

    def __str__(self) -> str:
        return "%_%" % (self.left, self.right)

    def print(self):
        print(str(self))
        self.left.print()
        self.right.print()

    def __lt__(self, other):
        return self.weight() < other.weight()


def tree_from_list(occurence_list: list[TreeNodeTraits]) -> Node:
    occurence_list = sorted(occurence_list, reverse=True)

    if len(occurence_list) >= 3:
        left, right, *rest = occurence_list
        new_node = Node(left, right) 
        rest.append(new_node)
        return tree_from_list(rest)
    else:
        # Those are the final two nodes that make up the tree root
        left, right = occurence_list
        return Node(left, right)

def count_occurences(input) -> list[TreeNodeTraits]:
    occurence_count = dict()
    for element in input:
        if element in occurence_count:
            occurence_count.update({element: occurence_count[element] + 1})
        else:
            occurence_count[element] = 0

    result: list[TreeNodeTraits] = []
    for element, occurrence in occurence_count.items():
        new_node = Leaf(element, occurrence)
        result.append(new_node)

    return result

class Tree:
    def __init__(self, input):
        self.occurences = count_occurences(input)
        self.root_node = tree_from_list(self.occurences.copy())

    def to_table(self, work_queue: list[str], result: list[str] = []) -> dict[str, str]:
        pass

def main():
    input = 'aaaabbbcccdde'
    tree = Tree(input)

main()
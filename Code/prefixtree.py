#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        return self.size == 0

    def contains(self, string):
        """Return True if this prefix tree contains the given string.
        time complexity: O(n) where n is the number of node 
        space complexity: O(1)
        """
        
        node = self.root
        for char in string:
            if node.num_children() == 0:
                return False
            if not node.has_child(char):
                return False
            node = node.get_child(char)
        print(f'node: {node.character}')
        return node.is_terminal()

    def insert(self, string):
        """Insert the given string into this prefix tree.
        time complexity: O(n) where n is the number of node 
        space complexity: O(1)
        """
        
        node = self.root
        for char in string:
            if not node.has_child(char):
                node.add_child(char, PrefixTreeNode(char))
            node = node.get_child(char)
        if not node.is_terminal():
            self.size += 1
        node.set_terminal()

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node.
        time complexity: O(n) where n is the number of node 
        space complexity: O(1)
        """
        # Match the empty string
        if len(string) == 0:
            return self.root, 0
        # Start with the root node
        node = self.root
       
        max_depth = 0
        for char in string:
            if not node.has_child(char):
                break
            max_depth += 1
            node = node.get_child(char)
        return node, max_depth

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string.
        time complexity: O(n) where n is the number of node when calling traverse
        space complexity: O(1)
        """
        # Create a list of completions in prefix tree
        completions = []
        root, depth = self._find_node(prefix)
        if depth == len(prefix):
            self._traverse(root, prefix, completions.append)
        return completions

    def strings(self):
        """Return a list of all strings stored in this prefix tree.
        time complexity: O(n) where n is the number of node when calling traverse
        space complexity: O(1)
        """
        # Create a list of all strings in prefix tree
        all_strings = []
        self._traverse(self.root, self.root.character, all_strings.append)
        return all_strings

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function.
        time complexity: O(n) where n is the number of node 
        space complexity: O(1)
        """
        if node.is_terminal():
            visit(prefix)
        for child in node.get_children():
            self._traverse(child, prefix + child.character, visit)

    def delete(self, key):
        """
        Removes all nodes containing letters of the given key to delete.
        O(k + (n * m)), where k is the length of the string
        being deleted, and (n * m) represents the time it takes to check if
        the input string is contained within the trie
        """
         if self.contains(key) is True:  # O(m * n)
            # set the node at the end of key no longer signal end of a node
            last_node, depth = self._find_node(key[-1])  # O(m)
            last_node.terminal = False
            # decrement size of tree
            self.size -= 1
        else:  # key is not actually in the prefix tree
            raise ValueError('Word is not found and cannot be deleted.')


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


if __name__ == '__main__':
    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print('\n' + '='*80 + '\n')
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)

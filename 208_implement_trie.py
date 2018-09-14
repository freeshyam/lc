#!/usr/bin/env python

import unittest

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = ""
        self.d = {}

    def child(self, c):
        try:
            return self.d[c]
        except KeyError:
            return None

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        next_node = None

        for c in word:
            next_node = node.child(c)

            if next_node:
                node = next_node
            else:
                next_node = TrieNode()
                node.d[c] = next_node
                node = next_node

        node.val = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        next_node = None

        for c in word:
            next_node = node.child(c)

            if next_node:
                node = next_node
            else:
                return False

        return word == node.val

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        next_node = None

        for c in prefix:
            next_node = node.child(c)

            if next_node:
                node = next_node
            else:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.t = Trie()

        self.t.insert("abcdefghijk")
        self.t.insert("challenge")
        self.t.insert("bicycle")
        self.t.insert("aardvark")
        self.t.insert("castle")
        self.t.insert("amaze")
        self.t.insert("amazed")

    def test_empty(self):
        self.assertTrue(self.t.search(""))

    def test_positive_exist(self):
        self.assertTrue(self.t.search("abcdefghijk"))
        self.assertTrue(self.t.search("challenge"))
        self.assertTrue(self.t.search("bicycle"))
        self.assertTrue(self.t.search("aardvark"))
        self.assertTrue(self.t.search("castle"))
        self.assertTrue(self.t.search("amaze"))
        self.assertTrue(self.t.search("amazed"))

        self.assertTrue(self.t.startsWith("abcdefghijk"))
        self.assertTrue(self.t.startsWith("challenge"))
        self.assertTrue(self.t.startsWith("bicycle"))
        self.assertTrue(self.t.startsWith("aardvark"))
        self.assertTrue(self.t.startsWith("castle"))
        self.assertTrue(self.t.startsWith("amaze"))
        self.assertTrue(self.t.startsWith("amazed"))
        self.assertTrue(self.t.startsWith("abc"))
        self.assertTrue(self.t.startsWith("challeng"))
        self.assertTrue(self.t.startsWith("bic"))
        self.assertTrue(self.t.startsWith("a"))
        self.assertTrue(self.t.startsWith("amaz"))
        self.assertTrue(self.t.startsWith("ca"))
        self.assertTrue(self.t.startsWith("b"))
        self.assertTrue(self.t.startsWith(""))

    def test_negative_exist(self):
        self.assertFalse(self.t.search("abc"))
        self.assertFalse(self.t.search("challeng"))
        self.assertFalse(self.t.search("bic"))
        self.assertFalse(self.t.search("a"))
        self.assertFalse(self.t.search("amaz"))
        self.assertFalse(self.t.search("pointer"))
        self.assertFalse(self.t.search("cow"))
        self.assertFalse(self.t.search("cherish"))
        self.assertFalse(self.t.search("newspaper"))

        self.assertFalse(self.t.startsWith("aber"))
        self.assertFalse(self.t.startsWith("coll"))
        self.assertFalse(self.t.startsWith("al"))
        self.assertFalse(self.t.startsWith("zebra"))
        self.assertFalse(self.t.startsWith("cali"))
        self.assertFalse(self.t.startsWith("tent"))
        self.assertFalse(self.t.startsWith("trophy"))
        self.assertFalse(self.t.startsWith("rusted"))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

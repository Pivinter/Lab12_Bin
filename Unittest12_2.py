import unittest

from Lab12_2 import Node, load_tree_from_file, save_tree_to_file

class TestNode(unittest.TestCase):

    def test_insert(self):
        tree = Node()
        tree.insert({"last_name": "Ivanov", "first_name": "Ivan", "phone_number": "12345", "birthdate": [1, 1, 2000]})
        tree.insert({"last_name": "Petrov", "first_name": "Petr", "phone_number": "67890", "birthdate": [2, 1, 2000]})
        self.assertIsNotNone(tree.find("12345"))
        self.assertIsNotNone(tree.find("67890"))

    def test_find(self):
        tree = Node()
        tree.insert({"last_name": "Ivanov", "first_name": "Ivan", "phone_number": "12345", "birthdate": [1, 1, 2000]})
        tree.insert({"last_name": "Petrov", "first_name": "Petr", "phone_number": "67890", "birthdate": [2, 1, 2000]})
        self.assertEqual(tree.find("12345"), {"last_name": "Ivanov", "first_name": "Ivan", "phone_number": "12345", "birthdate": [1, 1, 2000]})
        self.assertEqual(tree.find("67890"), {"last_name": "Petrov", "first_name": "Petr", "phone_number": "67890", "birthdate": [2, 1, 2000]})

    def test_remove(self):
        tree = Node()
        tree.insert({"last_name": "Ivanov", "first_name": "Ivan", "phone_number": "12345", "birthdate": [1, 1, 2000]})
        tree.insert({"last_name": "Petrov", "first_name": "Petr", "phone_number": "67890", "birthdate": [2, 1, 2000]})
        self.assertTrue(tree.remove("12345"))

    def test_save_load(self):
        tree = Node()
        tree.insert({"last_name": "Ivanov", "first_name": "Ivan", "phone_number": "12345", "birthdate": [1, 1, 2000]})
        tree.insert({"last_name": "Petrov", "first_name": "Petr", "phone_number": "67890", "birthdate": [2, 1, 2000]})
        save_tree_to_file(tree, "test_tree.txt")
        loaded_tree = load_tree_from_file("test_tree.txt")
        self.assertEqual(tree.find("12345"), loaded_tree.find("12345"))
        self.assertEqual(tree.find("67890"), loaded_tree.find("67890"))
        
if __name__ == '__main__':
    unittest.main()
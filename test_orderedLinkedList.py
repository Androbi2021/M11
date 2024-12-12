import unittest
from ordered_linked_list import OrderedLinkedList

class Test_OrderedLinkedList(unittest.TestCase):
    def setUp(self):
        lst = [1, 12, 48]
        self.ordered_list = OrderedLinkedList(lst)
    
    def test_add_middle(self):
        self.ordered_list.add_middle(24)
        expected_lst = ['1', '12', '24', '48']
        modified_lst = self.ordered_list.to_list()
        self.assertEqual(modified_lst, expected_lst, "Erreur dans la méthode add_middle")

if __name__ == '__main__':
    unittest.main()

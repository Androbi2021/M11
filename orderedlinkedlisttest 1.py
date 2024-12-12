import unittest
from ordered_linked_list import OrderedLinkedList

# Test class Node
class NodeTest(unittest.TestCase):
    def setUp(self):
        self.node1=Node()
        self.node2=Node()
        self.node3=Node()
    
    def test_set_cargo(self):
        self.node1.set_cargo(1)
        self.node2.set_cargo(2)
        self.node3.set_cargo(3)

        self.assertEqual(self.node1.cargo,1)
        self.assertEqual(self.node2.cargo,2)
        self.assertEqual(self.node3.cargo,3)

    def test_set_next(self):
        self.node1.set_next(self.node2)
        self.node3.set_next(self.node1)

        self.assertEqual(self.node1.next,self.node2)
        self.assertEqual(self.node3.next,self.node1)

#Test class OrderedLinkedList
class Test_OrderedLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.list1=[7,2,3,2]
        self.list2=[]
        self.list3=[6,9,7,2,0]

        self.order1=OrderedLinkedList(self.list1)
        self.order2=OrderedLinkedList(self.list2)
        self.order3=OrderedLinkedList(self.list3)
    
    def test_ordre(self):

        self.assertEqual(self.order1.to_list(),['2','2','3','7'])
        self.assertEqual(self.order3.to_list(),['0','2','6','7','9'])
    
    def test_add(self):

        self.order2.add(7)
        self.order2.add(4)
        self.order1.add(1)

        self.assertEqual(self.order2.to_list(),['4','7'])
        self.assertEqual(self.order1.to_list(),['1','2','2','3','7'])

    def test_remove(self):

        self.order1.remove(2)
        self.order3.remove(6)

        self.assertEqual(self.order1.to_list(),['2','3','7'])
        self.assertEqual(self.order3.to_list(),['0','2','7','9'])

    def test_length(self):
            self.assertEqual(self.order3.size(),5)

            self.order3.inc_size()

            self.assertEqual(self.order3.size(),6)

if __name__=="__main__":
    unittest.main()






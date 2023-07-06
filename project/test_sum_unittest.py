#import unittest


#class TestSum(unittest.TestCase):

def test_sum(self):
    self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

def test_sum_tuple(self):
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

#if __name__ == '__main__':
    #unittest.main()


#The orginal test came back as a fail.  That means it would need to go through a debugging stage next 
# and evaluated on how best to fix the problem (assuming it wasn't an 'easy' fix).
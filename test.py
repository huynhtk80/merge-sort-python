import unittest

from main import merge_sort


class testMergeSort(unittest.TestCase):
    def test_sort_simple(self):
        '''test that 463 sorts to 346'''

        array = [4,6,3]
        merge_sort(array)
        self.assertEqual(array, [3,4,6])

    def test_sort_single(self):
        '''test that 5 sorts to 5'''

        array = [5]
        merge_sort(array)
        self.assertEqual(array, [5])

    def test_sort_10digit(self):
        '''test that sorts 1 to 10'''

        array = [5,10,6,1,8,2,4,3,9,7]
        merge_sort(array)
        self.assertEqual(array, [1,2,3,4,5,6,7,8,9,10])

if __name__ == '__main__':
    unittest.main()
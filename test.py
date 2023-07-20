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

if __name__ == '__main__':
    unittest.main()
import unittest

from main import merge_sort


class testMergeSort(unittest.TestCase):
    def test_sort_simple(self):
        '''test that 463 sorts to 346'''

        array = [4,6,3]
        merge_sort(array)
        self.assertEqual(array, [3,4,6])

if __name__ == '__main__':
    unittest.main()
"""
https://docs.python.org/3/library/unittest.html
https://www.datacamp.com/community/tutorials/unit-testing-python

Commands:
- $ python3 -m unittest test_volume_cuboid.py
- $ python3 -m pydoc unittest.TestCase.assertCountEqual


"""
import unittest
from Cuboid import cuboid_volume


class TestCuboid(unittest.TestCase):
    def test_volume(self):
        # add assertion's here
        #   e.g. self.assertEqual(True, False)
        self.assertAlmostEqual(cuboid_volume(2), 8)
        self.assertAlmostEqual(cuboid_volume(1), 1)
        self.assertAlmostEqual(cuboid_volume(0), 0)
        self.assertAlmostEqual(cuboid_volume(5.5), 166.375)
        #self.assertAlmostEqual(cuboid_volume(5.5), 0)

    def test_input_value(self):
        self.assertRaises(TypeError, cuboid_volume, True)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
    #unittest.main()

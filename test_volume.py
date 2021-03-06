import unittest
import volume

class SimpleTest(unittest.TestCase):
    def test_vol(self):
        self.assertEqual(volume.vol(2), 8)
    
    def test_vol0(self):
        self.assertEqual(volume.vol(-2), -8)
    
    def test_vol1(self):
        self.assertEqual(volume.vol('2'), 8)

    def test_vol2(self):
        self.assertEqual(volume.vol(2.5), 15.625)

if __name__ == '__main__':
	unittest.main()
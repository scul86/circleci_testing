import run
import unittest2

class Test_Math(unittest2.TestCase):
    def test_add(self):
        self.assertEqual(run.add(2, 3), 5)


if __name__ == '__main__':
    unittest2.main()
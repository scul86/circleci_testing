import run
import unittest2


class Test_Math(unittest2.TestCase):
    def test_add(self):
        self.assertEqual(run.add(2, 3), 5)
        self.assertNotEqual(run.add(2, 3), 3)

    def test_sub(self):
        self.assertEqual(run.sub(2, 1), 1)

    def test_mult(self):
        self.assertEqual(run.mult(2, 3), 6)
        self.assertNotEqual(run.mult(2, 3), 4)

    def test_div(self):
        self.assertEqual(run.div(4, 2), 2)
        self.assertEqual(run.div(5, 2), 2.5)
        self.assertEqual(run.div(5, 2.5), 2)


if __name__ == '__main__':
    unittest2.main()

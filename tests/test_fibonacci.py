from unittest import TestCase

# Creating Instances
class TestFibonacci(TestCase):
    def test_series(self):
        # Importing Libraries
        from mathco import Fibonacci
        x = Fibonacci()
        self.assertTrue(x.series(5) == [1, 1, 2, 3, 5])

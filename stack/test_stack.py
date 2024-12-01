import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        """Set up a stack for testing."""
        self.stack = Stack(max_length=5)

    def test_push(self):
        """Test the push method."""
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.display(), [10, 20])

    def test_pop(self):
        """Test the pop method."""
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.pop(), 10)
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek(self):
        """Test the peek method."""
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 10)
        with self.assertRaises(IndexError):
            self.stack.pop()
            self.stack.peek()

    def test_is_empty(self):
        """Test the is_empty method."""
        self.assertTrue(self.stack.is_empty())
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())

    def test_size(self):
        """Test the size method."""
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)

    def test_overflow(self):
        """Test stack overflow."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.stack.push(40)
        self.stack.push(50)
        with self.assertRaises(OverflowError):
            self.stack.push(60)

    def test_display(self):
        """Test the display method."""
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.display(), [10, 20, 30])
        self.stack.pop()
        self.assertEqual(self.stack.display(), [10, 20])

if __name__ == "__main__":
    unittest.main()

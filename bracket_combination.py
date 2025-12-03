import math 
import unittest

def BracketCombinations(num):

  # Sanitize input
  try:
    num = int(num)
  except ValueError:
    raise ValueError("Input must be a numeric value")
  
  # Handle negative  
  if num >=0:
    return math.comb(2 * num, num) // (num + 1)
  else:
    raise ValueError("Input must be a non-negative integer")

# keep this function call here 
print(BracketCombinations(input()))

# testing cases 

test_inputs = [0, -1, "A"]

class TestBracketCombinations(unittest.TestCase):

    # Case 1: BaseExceptionGroup(0) -> Success
    def test_zero_input(self):
        result = BracketCombinations(0)
        self.assertEqual(result, 1, "Input 0 should return 1")

    # Case 2: BaseExceptionGroup(-1) -> Failure
    def test_negative_input(self):
        with self.assertRaisesRegex(ValueError, "Failure: Negative input"):
            BracketCombinations(-1)

    # Case 3: BaseExceptionGroup("A") -> Failure
    def test_non_numeric_input(self):
        with self.assertRaisesRegex(ValueError, "Failure: Non-numeric input"):
            BracketCombinations("A")
            
    # Bonus: Validating the example case (3 -> 5)
    def test_example_three(self):
        self.assertEqual(BracketCombinations(3), 5)

if __name__ == '__main__':
    # This runs the tests and gives you a report card
    unittest.main()
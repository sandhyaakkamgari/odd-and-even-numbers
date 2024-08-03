def print_even_odd(numbers):
  """Prints the even and odd numbers from a given list.

  Args:
    numbers: A list of integers.
  """

  even = []
  odd = []

  for num in numbers:
    if num % 2 == 0:
      even.append(num)
    else:
      odd.append(num)

  print("Even numbers:", even)
  print("Odd numbers:", odd)

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
print_even_odd(numbers)
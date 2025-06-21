class MathOperations:
    def add(self, a, b=None, c=None):
        if c is None:
            if b is None:
                return a
            return a + b
        return a + b + c

# Creating an instance of MathOperations
math_ops = MathOperations()

# Calling the overloaded add method
result1 = math_ops.add(2)
result2 = math_ops.add(2, 3)
result3 = math_ops.add(2, 3, 4)

print(result1)  # Output: 2
print(result2)  # Output: 5
print(result3)  # Output: 9

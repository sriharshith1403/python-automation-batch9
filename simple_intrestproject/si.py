from bank.multiply import multiply
from bank.divide import divide

# Input values
p = 10000   # Principal
r = 5       # Rate
t = 2       # Time

# Step 1: Multiply P * R * T
ptr = multiply(p, r, t)

# Step 2: Divide by 100
si = divide(ptr)

# Output
print("Simple Interest:", si)

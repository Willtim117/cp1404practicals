import random

print(random.randint(5, 20))  # line 1
"""5"""

print(random.randrange(3, 10, 2)) # line 2
"""smallest - 3, largest - 9, cannot produce 4"""

print(random.uniform(2.5, 5.5))  # line 3
"""smallest - 2.5, largest 5.5"""

random_number = random.uniform(1,100)
print(random_number)
"""random number between 1 and 100 inclusive"""

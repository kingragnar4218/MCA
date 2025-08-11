import numpy as np

# 1. Array Creation Routines
# np.array()
arr1 = np.array([1, 2, 3, 4])
print("np.array():", arr1)

# np.zeros()
arr2 = np.zeros((3, 3))
print("\nnp.zeros():\n", arr2)

# np.ones()
arr3 = np.ones((2, 4))
print("\nnp.ones():\n", arr3)

# np.empty() (uninitialized array)
arr4 = np.empty((2, 2))
print("\nnp.empty():\n", arr4)

# np.arange()
arr5 = np.arange(0, 10, 2)
print("\nnp.arange():", arr5)

# np.linspace()
arr6 = np.linspace(0, 1, 5)
print("\nnp.linspace():", arr6)

# np.eye() / np.identity()
arr7 = np.eye(3)
print("\nnp.eye():\n", arr7)

# np.diag() - diagonal matrix
arr8 = np.diag([1, 2, 3])
print("\nnp.diag():\n", arr8)

# np.full()
arr9 = np.full((2, 2), 7)
print("\nnp.full():\n", arr9)

# 2. Array Manipulation Functions
# np.reshape()
arr10 = arr1.reshape(2, 2)
print("\nnp.reshape():\n", arr10)

# np.transpose() / .T
arr11 = arr1.reshape(2, 2)
arr12 = arr11.T
print("\nnp.transpose() or .T:\n", arr12)

# np.flatten() / np.ravel()
arr13 = arr11.flatten()
arr14 = arr11.ravel()
print("\nnp.flatten():", arr13)
print("np.ravel():", arr14)

# np.concatenate() / np.stack()
arr15 = np.array([1, 2, 3])
arr16 = np.array([4, 5, 6])
concatenated = np.concatenate((arr15, arr16))
stacked = np.stack((arr15, arr16), axis=0)
print("\nnp.concatenate():", concatenated)
print("np.stack():\n", stacked)

# np.split() / np.hsplit() / np.vsplit()
arr17 = np.arange(12).reshape(3, 4)
split_arr = np.split(arr17, 2, axis=1)
print("\nnp.split():\n", split_arr)

# np.append(), np.insert(), np.delete()
arr18 = np.array([1, 2, 3, 4])
appended = np.append(arr18, [5, 6])
inserted = np.insert(arr18, 2, 99)
deleted = np.delete(arr18, 1)
print("\nnp.append():", appended)
print("np.insert():", inserted)
print("np.delete():", deleted)

# 3. Mathematical and Statistical Functions
# Basic Arithmetic
arr19 = np.array([1, 2, 3])
arr20 = np.array([4, 5, 6])
add = np.add(arr19, arr20)
subtract = np.subtract(arr19, arr20)
multiply = np.multiply(arr19, arr20)
divide = np.divide(arr19, arr20)
power = np.power(arr19, 2)
print("\nBasic Arithmetic:")
print("np.add():", add)
print("np.subtract():", subtract)
print("np.multiply():", multiply)
print("np.divide():", divide)
print("np.power():", power)

# Trigonometric Functions
arr21 = np.array([0, np.pi/2, np.pi])
sin_vals = np.sin(arr21)
cos_vals = np.cos(arr21)
tan_vals = np.tan(arr21)
print("\nTrigonometric Functions:")
print("np.sin():", sin_vals)
print("np.cos():", cos_vals)
print("np.tan():", tan_vals)

# Logarithmic/Exponential Functions
arr22 = np.array([1, 2, 3])
log_vals = np.log(arr22)
exp_vals = np.exp(arr22)
log10_vals = np.log10(arr22)
print("\nLogarithmic/Exponential Functions:")
print("np.log():", log_vals)
print("np.exp():", exp_vals)
print("np.log10():", log10_vals)

# Statistical Functions
arr23 = np.array([1, 2, 3, 4, 5])
mean_val = np.mean(arr23)
median_val = np.median(arr23)
sum_val = np.sum(arr23)
min_val = np.min(arr23)
max_val = np.max(arr23)
std_dev = np.std(arr23)
variance = np.var(arr23)
print("\nStatistical Functions:")
print("np.mean():", mean_val)
print("np.median():", median_val)
print("np.sum():", sum_val)
print("np.min():", min_val)
print("np.max():", max_val)
print("np.std():", std_dev)
print("np.var():", variance)

# Comparison Functions
arr24 = np.array([1, 2, 3])
arr25 = np.array([1, 2, 3])
arr26 = np.array([4, 5, 6])
array_equal = np.array_equal(arr24, arr25)
all_true = np.all([True, True, False])
any_true = np.any([False, False, True])
print("\nComparison Functions:")
print("np.array_equal():", array_equal)
print("np.all():", all_true)
print("np.any():", any_true)

# 4. Random Number Generation
# np.random.rand() and np.random.randn()
rand_uniform = np.random.rand(3, 3)
rand_normal = np.random.randn(3, 3)
print("\nRandom Number Generation:")
print("np.random.rand():\n", rand_uniform)
print("np.random.randn():\n", rand_normal)

# np.random.randint()
rand_int = np.random.randint(0, 10, (2, 2))
print("\nnp.random.randint():\n", rand_int)

# np.random.shuffle() / np.random.permutation()
arr27 = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr27)
arr28 = np.random.permutation([1, 2, 3, 4, 5])
print("\nnp.random.shuffle():", arr27)
print("np.random.permutation():", arr28)

import statistics
import math
import numpy as np
from scipy import stats
data = [10,20,30,40,50]
print("=========    python  basic   libraries   =========")

# 1. stastics library

print("\n1.stastics library")
print("data:",data)
print("mean:",statistics.mean(data))
print("meidan:",statistics.median(data))

# 2. math library

print("\n2.math slibrary")
print("square root of 25:",math.sqrt(25))
print("2 power of 3:",math.pow(2,3))
print("value of pi:",math.pi)
print("sin(90):",math.sin(math.pi/2))
print("cos(60):",math.cos(math.pi/3))

# 3. numpy library

print("\n3.numpy library")
arr = np.array(data)
print("numpy array:",arr)
print("mean:",np.mean(arr))
print("standard deviation:",np.std(arr))
print("squared values:",np.square(arr))

# 4. scipy library

print("\n4 . scipy library")
print("mean:",stats.tmean(arr))
print("standard deviation:",stats.tstd(arr))
print("z-score:",stats.zscore(arr))

print("\nprogram executed succesfully")


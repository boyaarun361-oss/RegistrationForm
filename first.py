

data = [10,20,30,40,50]

#mean
total = 0

for i in data:
    total = total+i

mean = total / len(data)
 
#median 
n=len(data)
if n%2==0:
    median=(data[n//2-1]+data[n//2])/2
else:
    median=data[n//2]


# Mode
mode = "No Mode"

for i in data:
    count = 0
    for j in data:
        if i == j:
            count = count+1
        if count>1:
            mode=i
            break

 

#variance
sum=0
for i in data:
    sum = sum+(i-mean)**2
variance = sum/n
 

#standard deviation
std = variance**0.5
 

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Variance =", variance)
print("Standard Deviation =", std)

# Maximum
maximum = data[0]
for i in data:
    if i > maximum:
        maximum = i

print("Maximun = ",maximum)

#minimum
minimun = data[0]
for i in data:
    if i < minimun:
       minimun = i

print("minimum = ",minimun)


#Range

Range = maximum-minimun
print("Range = ",Range)


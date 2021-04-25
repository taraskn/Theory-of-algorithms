from random import randint
from time import process_time
from matplotlib import pyplot as plt

array = [randint(0,100000) for i in range(100000)]

amount = [50, 100, 500, 1000, 2000, 5000, 10000]

time = []
results = []

for n in amount:
    c = 0
    for i in range(10000):
        start = process_time()
        array[:n].sort()
        stop = process_time()
        time.append(stop - start)
        c += 1
    average = sum(time) / len(time)
    print(f'Time for {n} elements: {average}')
    results.append(average)

x = amount
y = results

plt.plot(x,y)
plt.xlabel('Number of elements')
plt.ylabel('Time')
plt.show()

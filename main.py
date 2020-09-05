import functions
import matplotlib.pyplot as plt
import numpy

with open('test1.txt', 'r') as file:
    data = file.read().replace('\n', '')

startList = data.split()
startArr = list(map(int, startList))

# Make into 2D array
current = []
temp = []
for i in range(len(startArr)):
    temp.append(startArr[i])
    if(i != 0 and len(temp) % 3 == 0):
        current.append(temp)
        temp = []

print("Starting array: ", current)

childStates = []
currentDist = 50

# For plotting
distances = []
iteration = []

loop = 0

while(currentDist != 0):
    print("Current Distance: ", currentDist)
    newChildStates = functions.getChildStates(current)
    for state in newChildStates:
        childStates.append(state)

    childStates.sort(key=functions.comparator)

    if(len(childStates) > 0):
        current = childStates.pop().get("arr")
        currentDist = functions.distance(current)
    else:
        break

    # Make plot data
    if (loop % 1000 == 0): 
        iteration.append(loop)
        distances.append(currentDist)
    loop += 1

print(current)

plt.plot(iteration, distances)
plt.show()

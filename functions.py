import copy
from constants import FINAL_STATE

visited = set()

def getChildStates(current):
    # Find location of blank tile
    x = -1
    y = -1
    for i, row in enumerate(current):
        if -1 in row:
            x = i
            y = row.index(-1)

    newChildStates = []
    if(x - 1 >= 0):
        copy1 = copy.deepcopy(current)
        i = copy1[x-1][y]
        copy1[x-1][y] = -1
        copy1[x][y] = i
        if not haveVisited(copy1):
            dist = distance(copy1)
            child = {
                "arr": copy1,
                "dist": dist
            }
            newChildStates.append(child)

    if(x + 1 <= 2):
        copy2 = copy.deepcopy(current)
        i = copy2[x+1][y]
        copy2[x+1][y] = -1
        copy2[x][y] = i
        if not haveVisited(copy2):
            dist = distance(copy2)
            child = {
                "arr": copy2,
                "dist": dist
            }
            newChildStates.append(child)

    if(y-1 >= 0):
        copy3 = copy.deepcopy(current)
        i = copy3[x][y-1]
        copy3[x][y-1] = -1
        copy3[x][y] = i
        if not haveVisited(copy3):
            dist = distance(copy3)
            child = {
                "arr": copy3,
                "dist": dist
            }
            newChildStates.append(child)

    if(y+1 <= 2):
        copy4 = copy.deepcopy(current)
        i = copy4[x][y+1]
        copy4[x][y+1] = -1
        copy4[x][y] = i
        if not haveVisited(copy4):
            dist = distance(copy4)
            child = {
                "arr": copy4,
                "dist": dist
            }
            newChildStates.append(child)

    print("Got ", len(newChildStates), " child states from ")
    printArr(current)
    return newChildStates

def distance(arr):
    distance = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            final_x = FINAL_STATE.get(arr[i][j]).get('x')
            final_y = FINAL_STATE[(arr[i][j])].get('y')

            temp = abs((i - final_x)*3 + (j - final_y))
            distance += temp

    return distance

# Checks if in map of visited arrays and if not, then adds to map
def haveVisited(arr):
    list_str = ""
    for row in arr:
        for num in row:
            list_str += str(num)

    if list_str in visited:
        return True
    else:
        visited.add(list_str)
        print("Visited: ", len(visited))
        return False

def comparator(e):
    return e.get("dist")

def printArr(arr):
    for i in arr:
        print("| ", end='')
        for j in i:
            if(j != -1): print(j, " ", end='')
            else: print("-  ", end='')
        print("|")

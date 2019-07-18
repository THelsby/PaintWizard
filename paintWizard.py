import math
import operator

# (Price, litres, coverage m2)
cheapoMax = ["CheapoMax", 19.99, 20, 10]
averageJoes = ["AverageJoe", 17.99, 15, 11]
duluxourousPaints = ["Dulquxourous", 25, 10, 20]
allPaints = [cheapoMax, averageJoes, duluxourousPaints]
roomSize = int(input("Enter the size of the room you would like to paint\n"))
leastWaste = []
cheapestOption = []
print(allPaints)
wasted = {}
cost = {}


def calculateLeastWastage():
    for paint in allPaints:
        metersLeftOver = roomSize % paint[2]
        paintWasted = paint[2] - (metersLeftOver * (paint[2] / paint[3]))
        wasted[paint[0]] = paintWasted

    sortedWasted = sorted(wasted.items(), key=operator.itemgetter(1))
    print("Least Wasted")
    print(sortedWasted[0])


def calculateLowestCost():
    for paint in allPaints:
        tubsNeeded = roomSize / paint[3]
        cost[paint[0]] = math.ceil(tubsNeeded) * paint[1]

    sortedCost = sorted(cost.items(), key=operator.itemgetter(1))
    print("Least Cost")
    print(sortedCost[0])


calculateLeastWastage()
calculateLowestCost()

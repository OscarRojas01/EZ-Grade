import math
# The script responsible for calculating slope and creating interval points
# Seperate the handling of 2D & 3D slope calculations?
# Allow for 2D slope calulation and apply a given cross-slope?


def getSlope(point1, point2):
    '''A function that takes a dictionary and touple to find the slope in both x & y directions from one point to another and returns the dictionary updated with the new slopes'''

    distanceX = abs(point2[0] - point1['x'])
    distanceY = abs(point2[1] - point1['y'])
    elevationChange = point2[2] - point1['z']
    slope = {
        'x slope': (elevationChange/distanceX) / 2,
        'y slope': (elevationChange/distanceY) / 2
    }
    return point1 | slope


def applySlope(z, distance, slope):
    return round(z + (distance * slope), 2)

# def getNextPoint():


def createIntervals(point1, point2, stepSize):
    '''A function that creates interval points between a given dictionary and tuple, accounting for slope'''
    intervalPoints = []
    # Establishes how far back to trace through point list for the next elevation in y iteration
    stepBack = math.ceil(abs(point1['x'] - point2[0]) / stepSize) + 1
    for a in range(point1['y'], point2[1] + stepSize, stepSize):
        if a == 0:
            intervalPoints.append((point1['x'], point1['y'], point1['z']))
        elif a > point2[1]:
            prevPointElevation = intervalPoints[len(
                intervalPoints) - stepBack][2]
            point = (intervalPoints[len(intervalPoints) - stepBack][0], point2[1],
                     applySlope(prevPointElevation, (a - stepSize), point1['y slope']))
            intervalPoints.append(point)
        else:
            prevPointElevation = intervalPoints[len(
                intervalPoints) - stepBack][2]
            point = (intervalPoints[len(intervalPoints) - stepBack][0], a,
                     applySlope(prevPointElevation, stepSize, point1['y slope']))
            intervalPoints.append(point)
        for b in range(point1["x"] + stepSize, point2[0] + stepSize, stepSize):
            # Applies slope for each interval step through X-axis range along the current iteration of the Y-axis range
            if b > point2[0]:
                point = (point2[0], a, applySlope(
                    intervalPoints[len(intervalPoints)-1][2], (b - point2[0]), point1['x slope']))
                intervalPoints.append(point)
            else:
                point = (b, a, applySlope(
                    intervalPoints[len(intervalPoints)-1][2], stepSize, point1['x slope']))
                intervalPoints.append(point)
    # displaying list for proof of accuracy
    print(intervalPoints)


# test variables & function application
start = {
    'x': 0,
    'y': 0,
    'z': 0
}
end = (22, 60, 1.25)
start = getSlope(start, end)
createIntervals(start, end, 5)

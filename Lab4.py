import point
import unittest


# Write your functions for each part in the space below.
# Part 1
# design Recipe:
# 1)Purpose is to make a function make a new list that appends the first item of each list into it
# 2) first_element(List:list[int])->list:
# 3) template of function
#     - access to list
#     - take the first value of each list and append to new list
#     - return new list
#     - expected list with every first item in each list
# 4) test case:input = [[1, 2], [3, 4]]
#              result = Lab4.first_element(input)
#              expected = [1, 3]
#              self.assertEqual(expected, result)
# 5)

def first_element(L1: list[list[int]]) -> list:
    newL = []
    emptyL = []
    for item in L1:
        if len(item) > 0:
            newL.append(item)
    for item in newL:
        emptyL.append(item[0])
    return emptyL


# Part 2
# design Recipe:
# 1)Purpose is to make a list that contains the x-coordinates of each point from the input list
# 2)x_coordinates(x-coord:list[point])->list[int]:
# 3) template of function
#     - access the coordinates list
#     - makes list that only adds the x-points
# 4) test case: point1 = point.Point(1, 2)
#               point2 = point.Point(3, 4)
#               point3 = point.Point(5, 6)
#               points = [point1, point2, point3]
#               assert Lab4.x_coordinates(points) == [1, 3, 5]
# 5)



def x_coordinates(points: list[point.Point]) -> list[float]:
    return [point.x for point in points]


# Part 3
# design Recipe:
# 1)Purpose is to
# 2)are_in_positive_quadrant(point:list[point])->list[int]:
# 3) template of function
#     - get both coordinates(x,y)
#     - for loop that grabs each coord in list
#     - checks if both x and y coords are positive
#     - if both are positive then append into positiveL
# 4) test case: point1 = point.Point(1, 21)
#               point2 = point.Point(33, -4)
#               point3 = point.Point(85, 86)
#               pointf = [point1, point2, point3]
#               result = Lab4.are_in_positive_quadrant(pointf)
#               expected = [point1, point3]
#               assert result == expected
# 5)
def are_in_positive_quadrant(point1: list[point]) -> list[int]:
    positiveL = []
    for point in point1:
        if point.x > 0 and point.y > 0:
            positiveL.append(point)
    return positiveL


# Part 4
# design Recipe:
# 1) Purpose is to take the Euclidean distance of two points
# 2) distance(Firstp: Point, Secondp: Point) -> float:
# 3) template of function
#     - get two points
#     - get the difference for both x coordinates
#     - get the difference for both y coordinates
#     - put the two differences of the coordinates into the pythagorean theorem
# 4) test case: point1 = point.Point(2, 4)
#               point2 = point.Point(2, 8)
#               assert Lab4.distance(point1, point2) == 4
# 5)
import math

def distance(Firstp: point.Point, Secondp: point.Point) -> float:
    x_diff = Firstp.x - Secondp.x
    y_diff = Firstp.y - Secondp.y
    return math.sqrt(x_diff ** 2 + y_diff ** 2)

# Part 5
# design Recipe:
# 1) takes two coordinate points and returns the manhattan distance between them
# 2) manhattan_distance(point1: Point, point2: Point) -> float:
# 3) template of function
#     - get two points
#     - get the absolute difference for both x coordinates
#     - get the absolute difference for both y coordinates
#     - adds both y and x coords together and returns the sum
# 4) test case: point1 = point.Point(3, 9)
#               point2 = point.Point(2, 13)
#               assert Lab4.manhattan_distance(point1, point2) == 5
# 5)
def manhattan_distance(point1: point.Point, point2: point.Point) -> float:
    x_aDiff = abs(point1.x - point2.x)
    y_aDiff = abs(point1.y - point2.y)
    sum = x_aDiff + y_aDiff
    return sum

# Part 6
# design Recipe:
# 1) get the distance from (0,0) of each point using either Manhattan or euclidean and put it into a list
# 2) distance_all(List_p:list[point]) -> list:
# 3) template of function
#     - access the list of points
#     - cycle through the list and take each individual point
#     - put both x and y through absolute value
#     - get the sum of the two coordinates and append to a list(this uses the manhattan distance)
# 4) test case: pointL = [point.Point(0, 0), point.Point(1, 0), point.Point(0, 1), point.Point(-1, 0), point.Point(0, -1)]
#               expected_result = [0, 1, 1, 1, 1]
#               assert Lab4.distance_all(pointL) == expected_result
# 5)

def distance_all(List_p:list[point.Point]) -> list[float]:
    sList = []
    for point in List_p:
        x_diff = abs(point.x)
        y_diff = abs(point.y)
        m_distance = x_diff + y_diff
        sList.append(m_distance)
    return sList

points = [point.Point(3, 4), point.Point(5, 12), point.Point(8, 15), point.Point(2, 3)]
result = distance_all(points)
print(result)

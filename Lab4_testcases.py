import point
import Lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1, 2], [3, 4]]
        result = Lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        # write a second test here
        input2 = [[1, 2, 3], [], [], [-8], [5, 6]]
        result = Lab4.first_element(input2)
        expected = [1, -8, 5]
        self.assertEqual(expected, result)


#class TestCases(unittest.TestCase):
# Part 2
    def test_x_coordinates_1(self):
        point1 = point.Point(1, 2)
        point2 = point.Point(3, 4)
        point3 = point.Point(5, 6)
        points = [point1, point2, point3]
        assert Lab4.x_coordinates(points) == [1, 3, 5]

    def test_x_coordinates_2(self):
        point1 = point.Point(-1, 2)
        point2 = point.Point(3.8, -4)
        point3 = point.Point(-5.6, 6)
        points = [point1, point2, point3]
        assert Lab4.x_coordinates(points) == [-1, 3.8, -5.6]
# Part 3
    def test_are_in_positive_quadrant_1(self):
        point1 = point.Point(1, 21)
        point2 = point.Point(33, -4)
        point3 = point.Point(85, 86)
        pointf = [point1, point2, point3]
        result = Lab4.are_in_positive_quadrant(pointf)
        expected = [point1, point3]
        assert result == expected

    def test_are_in_positive_quadrant_2(self):
        point1 = point.Point(1.32, 91)
        point2 = point.Point(33, 0)
        point3 = point.Point(-8.5, 86)
        point4 = point.Point(0,0)
        pointf = [point1, point2, point3, point4]
        result = Lab4.are_in_positive_quadrant(pointf)
        expected = [point1]
        assert result == expected

# Part 4
    def test_distance_1(points):
        point1 = point.Point(2, 4)
        point2 = point.Point(2, 8)
        assert Lab4.distance(point1, point2) == 4

    def test_distance_2(points):
        point1 = point.Point(16, 12)
        point2 = point.Point(20, 9)
        assert Lab4.distance(point1, point2) == 5

    def test_distance_3(points):
        point1 = point.Point(0, 0)
        point2 = point.Point(0, 0)
        assert Lab4.distance(point1, point2) == 0
# Part 5
    def test_manhattan_distance_1(points):
        point1 = point.Point(3, 9)
        point2 = point.Point(2, 13)
        assert Lab4.manhattan_distance(point1, point2) == 5

    def test_manhattan_distance_2(points):
        point1 = point.Point(-1, -2)
        point2 = point.Point(-3, -4)
        assert Lab4.manhattan_distance(point1, point2) == 4

    def test_manhattan_distance_3(points):
        point1 = point.Point(35, -19)
        point2 = point.Point(-13, 52)
        assert Lab4.manhattan_distance(point1, point2) == 119
# Part 6
    def test_distance_all_1(points):
        pointL = [point.Point(0, 0), point.Point(1, 0), point.Point(0, 1), point.Point(-1, 0), point.Point(0, -1)]
        expected_result = [0, 1, 1, 1, 1]
        assert Lab4.distance_all(pointL) == expected_result

    def test_distance_all_2(points):
        pointL = [point.Point(-9, 4), point.Point(.3, 21), point.Point(-6.7, -9.3)]
        expected_result = [13, 21.3, 16]
        assert Lab4.distance_all(pointL) == expected_result

if __name__ == '__main__':
    unittest.main()

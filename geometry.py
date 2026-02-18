from typing import List, Tuple, Union
# The script responsible for calculating slope and creating interval points


def get_slope(point1: dict, point2: Tuple):
    '''A function that takes two points to find the slope, along ONLY the x-axis, from one point to another and adds the slope to the dictionary'''

    distance = abs(point2[0] - point1['x'])
    elevation_change = point2[2] - point1['z']
    slope = round((elevation_change/distance), 4)
    point1.update({'slope': slope})


def apply_slope(z: Union[int, float], distance: Union[int, float], slope: Union[int, float]):
    '''Applies given slope based on starting elevation and distance to next point, returns elevation'''
    return round(z + (distance * slope), 2)


def create_linear_intervals(point1: dict, point2: List[Tuple], step_size: int):
    '''A function that interpolates points between two known points (along the x-axis ONLY) with an unknown slope. Returns a list of points(x,y,z) stored as tuples'''
    interval_points = []
    get_slope(point1, point2)
    for a in range(point1['x'], point2[0] + step_size, step_size):
        if a == point1['x']:
            interval_points.append((point1['x'], point1['y'], point1['z']))
        elif a <= point2[0]:
            prev_point_elevation = interval_points[len(interval_points) - 1][2]
            point = (a, point1['y'], apply_slope(
                prev_point_elevation, step_size, point1['slope']))
            interval_points.append(point)
        else:
            interval_points.append(point2)
    return interval_points


def apply_cross_slope(point_list: List[Tuple], width: int, cross_slope: Union[int, float], step_size: int):
    '''Applies a cross slope to an existing line of points(in x,y,z format) to create a square area of points. Original list is updated'''
    point_list_copy = point_list.copy()
    point_list.clear()
    for point_from_list in enumerate(point_list_copy):
        point_list.append(point_from_list[1])
        for b in range(0, width + step_size, step_size):
            if b == 0:
                continue
            prev_point = point_list[-1]
            if b <= width:
                point = (point_from_list[1][0], b, apply_slope(
                    prev_point[2], step_size, cross_slope))
            else:
                point = (point_from_list[1][0], width, apply_slope(
                    prev_point[2], width - prev_point[1], cross_slope))
            point_list.append(point)


# test variables & function application
start = {
    'x': 0,
    'y': 0,
    'z': 0
}
end = (22, 0, 1)
CROSS_SLOPE = 0.02
interval_point_list = create_linear_intervals(start, end, 5)
print(interval_point_list)
apply_cross_slope(interval_point_list, 22, CROSS_SLOPE, 5)
print(interval_point_list)

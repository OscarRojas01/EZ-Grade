from typing import Union, List, Tuple
# Grade Rod height handling and elevation adjustments for cut/fill


def elevation_to_rod_heights(point_list: List[Tuple], instrument_elevation: float):
    '''A function to convert raw elevations to grade rod readings, returns a new list'''
    rod_points = []
    for point_from_list in enumerate(point_list):
        rod_reading = round(instrument_elevation - point_from_list[1][2], 2)
        point = (point_from_list[1][0], point_from_list[1][1], rod_reading)
        rod_points.append(point)
    return rod_points


def apply_fill(point_list: List[Tuple], fill: Union[int, float]):
    '''A function that raises the elevations of an existing list of points by a given amount, list must be in elevations not rod readings. Returns a new list'''
    fill_points = []
    for point_from_list in enumerate(point_list):
        point = (point_from_list[1][0], point_from_list[1]
                 [1], round(point_from_list[1][2] + fill, 2))
        fill_points.append(point)
    return fill_points


def apply_cut(point_list: List[Tuple], cut: Union[int, float]):
    '''A function that lowers the elevations of an existing list of points by a given amount, list must be in elevations not rod readings. Returns a new list'''
    cut_points = []
    for point_from_list in enumerate(point_list):
        point = (point_from_list[1][0], point_from_list[1]
                 [1], round(point_from_list[1][2] - cut, 2))
        cut_points.append(point)
    return cut_points


# test variables & function application
points = [(0, 0, 901.00), (0, 5, 901.1), (0, 10, 901.2)]
hi = 906.25
print(points)
rod_readings = elevation_to_rod_heights(points, hi)
print(rod_readings)
fill_amount = .33
points_fill = apply_fill(points, fill_amount)
print(points_fill)
fill_rod_readings = elevation_to_rod_heights(points_fill, hi)
print(fill_rod_readings)
cut_amount = .25
points_cut = apply_cut(points, cut_amount)
print(points_cut)
cut_rod_readings = elevation_to_rod_heights(points_cut, hi)
print(cut_rod_readings)

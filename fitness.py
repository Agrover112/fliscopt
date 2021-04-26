
from utils import flights, get_minutes, people


def fitness_function(solution, dest):
    """ Cost function of Flight Scheduling problem

    Args:
        solution (list): List containing the solution to be evaluated
        dest (str): String containing the destination city airport abbreviation

    Returns:
        int: The evaluated cost og the given solution and destination of travel
    """

    total_price = 0
    last_arrival = 0          # 0:00
    first_departure = 1439    # 23:59 for initialization
    flight_id = -1
    for i in range(len(solution) // 2):
        origin = people[i][1]
        flight_id += 1
        going = flights[(origin, dest)][solution[flight_id]]
        flight_id += 1
        returning = flights[(dest, origin)][solution[flight_id]]

        total_price += going[2]
        total_price += returning[2]

        if last_arrival < get_minutes(going[1]):  # Find last arrival
            last_arrival = get_minutes(going[1])
        if first_departure > get_minutes(returning[0]):  # Find first departure
            first_departure = get_minutes(returning[0])

    total_wait = 0
    flight_id = -1
    for i in range(len(solution) // 2):
        origin = people[i][1]
        flight_id += 1
        going = flights[(origin, dest)][solution[flight_id]]
        flight_id += 1
        returning = flights[(dest, origin)][solution[flight_id]]

        # Waiting time for all arrived
        total_wait += last_arrival - get_minutes(going[1])
        # Waiting time for all to depart and reach locatiom
        total_wait += get_minutes(returning[0]) - first_departure

    # 3PM - 10AM
    # 11AM - 3PM
    if last_arrival > first_departure:
        # Penalize if arrival and departure are not on same days
        total_price += 50

    return total_price + total_wait     # The total cost associated


if __name__ == "__main__":
    assert fitness_function(
        [1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3], "FCO") == 5451
    assert fitness_function(
        [1, 3, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3], "FCO") == 5304

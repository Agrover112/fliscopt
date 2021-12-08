import sys
from math import cos, exp, sin, sqrt

from .utils.util import flights, get_minutes, people

# All domains defined with a single-tuple/or without a multiplier have n-dimensional Input Domain
ackley_N2_d = [(-32, 32)]*2
schaffer_N1_d = [(-100, 100)]*2
matyas_d = [(-10, 10)]*2
griewank_d = [(-600, 600)]
sphere_d = [(-5, 5)]
three_hump_camel_d = [(-5, 5)]*2
schwefel_N2_23_d = [(-10, 10)]
brown_d = [(-1, 4)]
rosenbrock_d = [(-5, 10)]
zakharov_d = [(-5, 10)]
domain = {
    'domain': [(0, 9)] * (len(people) * 2),  # 9 times * no.of people * to-from
    'ackley_N2': ackley_N2_d,
    'schaffer_N1': schaffer_N1_d,
    'schwefel_N2_23': schwefel_N2_23_d,
    'matyas': matyas_d,
    'booth': matyas_d,
    'griewank': griewank_d,
    'sphere': sphere_d,
    'three_hump_camel': three_hump_camel_d,
    'brown': brown_d,
    'rosenbrock': rosenbrock_d,
    'zakharov': zakharov_d
}
# Our Problem's fitness function


def fitness_function(solution, dest):
    """ Cost function of Flight Scheduling problem 12D

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
        # Waiting time for all to depart and reach location
        total_wait += get_minutes(returning[0]) - first_departure

    # 3PM - 10AM
    # 11AM - 3PM
    if last_arrival > first_departure:
        # Penalize if arrival and departure are not on same days
        total_price += 50

    return total_price + total_wait     # The total cost associated

# Benchmarks Function


def ackley_N2(x):
    """Ackley test objective function.
         - minimization
       * - Range[-32, 32]`
       * - Global optima  f(x*)=-200    @x1,x2=0,0
    """

    return -200 * exp(-0.02 * sqrt((x[0]**2) + (x[1]**2)))


def matyas(x):
    """
    Ackley test objective function 2D
         - minimization
       * - Range[-10, 10]`
       * - Global optima  f(x*)=0    @x1,x2=0,0
    """
    if x is not None and not None in x and type(x) == list and len(x) == 2:
        return 0.26 * (x[0]**2 + x[1]**2) - 0.48 * x[0] * x[1]
    else:

        if not type(x) == list:
            raise TypeError("X is of type list")
        elif len(x) != 2:
            raise ValueError(
                "Matyas function is defined in 2D space. Your x is of {} dimensions".format(len(x)))
        elif x is None or x[0] is None or x[1] is None or None in x:
            raise ValueError("X is an empty list or contains only None")
        else:
            raise ValueError("X params are wrong")


def booth(x):
    return (x[0] + (2 * x[1]) - 7)**2 + ((2 * x[0]) + x[1] - 5)**2


if sys.version_info[1] < 8:
    import operator
    from functools import reduce
    from math import cos, exp, sin, sqrt

    def griewank(x):
        # Griewank is n dim unimodal f(0,0,0)== 0
        return 1.0/4000.0 * sum(i**2 for i in x) - reduce(operator.mul, (cos(i/sqrt(idx+1.0)) for idx, i in enumerate(x))) + 1
else:
    from math import prod

    def griewank(x):
        # Griewank is n dim unimodal f(0,0,0)== 0
        return 1.0/4000.0 * sum(i**2 for i in x) - prod((cos(i/sqrt(idx+1.0)) for idx, i in enumerate(x))) + 1


def sphere(x):
    # Convex n dimensional unimodal
    return sum(i**2 for i in x)


def schaffer_N1(x):
    # Shaffer N1 is 2 dim unimodal function with a global minima at f(0,0)
    return 0.5 + (sin((x[0] ** 2 + x[1] ** 2) ** 2) ** 2) - 0.5 / (1 + 0.001 * (x[0] ** 2 + x[1] ** 2)) ** 2


def three_hump_camel(x):
    return (2 * x[0]**2) - (1.05 * (x[0] ** 4)) + ((x[0] ** 6) / 6) + x[0] * x[1] + x[1] ** 2


def schwefel(x):
    return sum((i**10 for i in x))


def brown(x):
    return sum((x**2.0)**(y**2.0 + 1.0) + (y**2.0)**(x**2.0 + 1.0) for x, y in zip(x[:-1], x[1:]))


def rosenbrock(x):
    """ This function blatantly copied lol DEAP[1] benchmarks wellllllll
        My implementation was absolutely trash 
        
        References:
        [1]https://github.com/DEAP/deap/blob/d328fe6b68e7528b2d2d990bb2ab1ad1786e6f58/deap/benchmarks/__init__.py#L98
    """
    return sum(100 * (x * x - y)**2 + (1. - x)**2 for x, y in zip(x[:-1], x[1:]))


def zakharov(x):
    p2 = sum(0.5*idx*i for idx, i in enumerate(x))
    return (sum(i**2 for i in x) + p2**2 + p2**4)



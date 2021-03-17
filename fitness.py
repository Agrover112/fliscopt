
from utils import get_minutes , flights , people
def fitness_function(solution,dest):

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
 
    if last_arrival < get_minutes(going[1]): # Find last arrival
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

    total_wait += last_arrival - get_minutes(going[1])    # Waiting time for all arrived
    total_wait += get_minutes(returning[0]) - first_departure  # Waiting time for all to depart and reach locatiom
  
  # 3PM - 10AM
  # 11AM - 3PM
  if last_arrival > first_departure:
    total_price += 50                 # Penalize if arrival and departure are not on same days
  
  return total_price + total_wait     # The total cost associated
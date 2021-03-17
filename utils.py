import time
import random
import math
import sys
import logging
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
people = [('Lisbon', 'LIS'),
          ('Madrid', 'MAD'),
          ('Paris', 'CDG'),
          ('Dublin', 'DUB'),
          ('Brussels', 'BRU'),
          ('London', 'LHR')]
flights = {}

def read_file(fname):
    for line in open('/mnt/d/MINOR PROJECT/final/data/'+fname,'r+'):
        origin, dest, departure, arrival, price = line.split(',')
        flights.setdefault((origin, dest), [])
        flights[(origin, dest)].append((departure, arrival, int(price)))
    return "------File Read-----"

def print_schedule(schedule,dest):
  flight_id = -1
  total_price = 0
  for i in range(len(schedule) // 2):
    name = people[i][0]
    origin = people[i][1]
    flight_id += 1
    going = flights[(origin, dest)][schedule[flight_id]]
    total_price += going[2]
    flight_id += 1
    returning = flights[(dest, origin)][schedule[flight_id]]
    total_price += returning[2]
    print(name, origin, dest, going[0], going[1], going[2], returning[0], returning[1], returning[2])
    print('Total price: ', total_price)

def get_minutes(hour):
  t = time.strptime(hour, '%H:%M')
  minutes = t[3] * 60 + t[4]
  return minutes

def plot_scores(scores,algo_name,save_fig,**kwargs):
  temp=kwargs.get('temp',None)
  plt.xlabel("No.of improvements")
  plt.ylabel("Objecetive f(x) Scores")
  plt.plot(scores)
  if save_fig :
    plt.savefig(os.path.join('/mnt/d/MINOR PROJECT/final/results/'+algo_name+".png")) 
  else:
    plt.show()
  if algo_name =='simulated_annealing':
    plt.xlabel("Temperature")
    plt.ylabel("Objective f(x) Scores")
    plt.plot(scores,temp)
    if save_fig :
      plt.savefig(os.path.join('/mnt/d/MINOR PROJECT/final/results/'+"Scores_V_Temp"+".png")) 
    else: 
          plt.show()

    


if __name__ =='__main__':
        print(os.getcwd())
        assert read_file("flights.txt") =="------File Read-----"
        assert flights !=None
        assert get_minutes("6:13") == 373
        assert get_minutes("00:00") == 0
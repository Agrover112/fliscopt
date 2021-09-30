import os
import time

import matplotlib
import matplotlib.pyplot as plt


import rich

matplotlib.use('TKAgg')
people = [('Lisbon', 'LIS'),
          ('Madrid', 'MAD'),
          ('Paris', 'CDG'),
          ('Dublin', 'DUB'),
          ('Brussels', 'BRU'),
          ('London', 'LHR')]
flights = {}


def read_file(fname) -> str: 
    """ Utility function to read given file
    Args:
        fname (str): File name to be read
    Returns:
        str: String message that file has been read
    """

    for line in open('../data/'+fname, 'r+'):
        origin, dest, departure, arrival, price = line.split(',')
        flights.setdefault((origin, dest), [])
        flights[(origin, dest)].append((departure, arrival, int(price)))
    return "------File Read-----"


def print_schedule(schedule:list, dest:str) -> None:
    """ Generates and prints the flight schedule based on the schedule and destination information.

    Args:
        schedule (list): List containing the flight schedule similar to solutions
        dest (str): The destination, eg 'FCO' for Rome. Refer flights.txt
    """
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
        #pprint(name, origin, dest, going[0], going[1],\
        #      going[2], returning[0], returning[1], returning[2])
        rich.print(name,origin, dest, going[0], going[1],
              going[2], returning[0], returning[1], returning[2])
        rich.print('[bold magenta]Total price: [/bold magenta]', total_price)


def get_minutes(hour:str) -> int:
    """ Get total number of minutes from time in %H:%M .

    Args:
        hour (str): String containing time in 24 hour %H:%M format

    Returns:
        int: Returns total number of minutes
    """
    t = time.strptime(hour, '%H:%M')
    minutes = t[3] * 60 + t[4]
    return minutes


def plot_scores(scores, algo_name, save_fig, **kwargs) -> None:
    """ Plots the respective scores
    Args:
        scores (list): A list containing the scores over number of epochs.Eg.cost over n epochs
        algo_name (str): The name of the algorithm whose scores are being plotted
        save_fig (bool): If True figure is saved , otherwise plotted during run-time.
    """
    temp = kwargs.get('temp', None)
    fname = kwargs.get('fname', 'flight_scheduling')

    if not os.path.exists(os.getcwd() + '/results'):
            os.makedirs(os.getcwd()+ '/results', exist_ok=True)
    if not os.path.exists(os.getcwd() + '/results/plots'):
            os.makedirs(os.getcwd()+ '/results/plots', exist_ok=True)
    if not os.path.exists(os.getcwd() + '/results/plots/'+fname):
            os.makedirs(os.getcwd()+ '/results/plots/'+fname, exist_ok=True)

    if algo_name == 'simulated_annealing' or algo_name=='SimulatedAnnealing':
        plt.xlabel("Temperature")
        plt.ylabel("Objective f(x) Scores")
        plt.plot(temp, scores)
        if save_fig:
            plt.savefig(os.path.join(
                os.getcwd()+'/results/plots/' + fname + '/' + "simulated_annealing" + ".png"))
        else:
            plt.show()
    elif algo_name == 'genetic_algorithm' or algo_name == 'genetic_algorithm_reversed' or algo_name == 'genetic_algorithm_with_reversals'or algo_name =='BaseGA':
        plt.xlabel("No.of Generations")
        plt.ylabel("Objective f(x) Scores")
        plt.plot(scores)
        if save_fig:
            plt.savefig(os.path.join(
                os.getcwd()+'/results/plots/' + fname + '/' + algo_name + ".png"))
        else:
            plt.show()
    else:
        plt.xlabel("No.of improvements")
        plt.ylabel("Objective f(x) Scores")
        plt.plot(scores)
        if save_fig:
            plt.savefig(os.path.join(
                os.getcwd()+'/results/plots/' + fname + '/' + algo_name + ".png"))
        else:
            plt.show()

def play_sound() -> None:  #FIX-NEEDED
    """ Plays a completion sound.
    """
    raise NotImplementedError
  


if __name__ == '__main__':
    print(os.getcwd())
    print_schedule([1,2,3,4,5,6,7,8,9],'FCO')

# Author: Dorian Knight
# Date: December 10th 2024
# Description: Quick script to randomize experiment order

from random import randrange

experiment_order = []

# Makes a list with numbers 1 to 32
experiments = list(range(1, 33))

for i in range(32):
    # Picks a random experiment eg. experiment 16
    index_picked = randrange(0,len(experiments))

     # Add experiment to the ordered experiment list
    experiment_order.append(experiments[index_picked])

    # Removes the picked experiment from the list of unordered experiments
    experiments.remove(experiments[index_picked])

   

print(experiment_order)
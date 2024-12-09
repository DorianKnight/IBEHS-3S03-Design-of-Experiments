# Author: Dorian Knight
# Date: December 9th 2024
# Description: Count to a specified number and measure the time

import time
from random import randrange

# Import experimental data

# Set factors from imported experimental data
target_count = 1000000 # Between 1000000 and 10000000
max_numbers = 5
random_range = 100

master_debug_flag = 0 # Turns on all debug flags - this is the factor I switch on or off
debug_flag = 0        # Happens during the experiment and does impact experiment time
final_debug_flag = 1  # Occurs at the end and doesn't impact experiment time

# Run experiment
current_count = 0
start_time = time.time()

iteration_tracker = 0
while current_count < target_count:
    iteration_tracker += 1

    # Get the numbers which will be added together
    nums_stack = []
    for i in range(max_numbers):
        new_num = randrange(1,random_range)
        nums_stack.append(new_num)

    if debug_flag or master_debug_flag:
        print(f"Iteration tracker: {iteration_tracker} \nFactors set: \nRandom range: 1-{random_range} \nMax numbers used during a single iteration: {max_numbers} \nTarget count: {target_count} \nCurrent count: {current_count}")
        print(f"This is the stack of random numbers generated {nums_stack} \n\n")

    # Add to current count
    current_count += sum(nums_stack)
    '''
        Sum function has an O(n) time complexity
        While having more numbers speeds up the counting speed, there is additional overhead to taking the sum of an array because the time to sum an array increases as the array grows
        I am unsure whether the time lost due to additional computation is significant compared to the time gained due to having an extra number in the sum list.
        Whether I know or not doesn't matter much but this trade-off is important to point out.
    '''

end_time = time.time() # Stop the experiment - target count reached
experiment_time = end_time - start_time

# Print out useful debug information
if final_debug_flag or master_debug_flag:
    print(f"Total number of iterations {iteration_tracker} \
          \nActual count reached: {current_count}\
          \nExperiment target count: {target_count}\
          \nMax numbers per iteration: {max_numbers}\
          \nMax in random range: {random_range}\
          \nDebug flags enabled: {master_debug_flag}\
          \nTotal time taken: {experiment_time}\n\n\n\n")

# Save times to file for data analysis
experimental_data = {"target_count": target_count,              # Factor 1
                     "max_numbers": max_numbers,                # Factor 2
                     "random_range": random_range,              # Factor 3
                     "Master debug flag": master_debug_flag,    # Factor 4
                     "programming language": "Python",          # Factor 5
                     "experiment_time": experiment_time}        # Variable of interest



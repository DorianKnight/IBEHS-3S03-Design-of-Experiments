// Author: Dorian Knight
// Date: December 10th 2024
// Description: Count to a target count and measure time

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int rand_r(unsigned int *seed);

int main()
{
    // Set factors
    int target_count = 50000000; // Either 10000000 or 50000000
    const int max_numbers = 5;  // Either 2 or 5
    int random_range = 100;     // Either 100 or 1000

    int master_debug_flag = 1;  // Turns on all debug flags - this is the factor I switch on or off
    int debug_flag = 0;         // Happens during the experiment and does impact experiment time - for code debug use only
    int final_debug_flag = 1;   // Occurs at the end and doesn't impact experiment time          - for code debug use only and to read time output

    // Run experiment
    int current_count = 0;
    clock_t start_time = clock();

    int iteration_tracker = 0;
    while (current_count < target_count) 
    {
        iteration_tracker++;

        // Get the numbers which will be added together
        int nums_stack[max_numbers];
        for (int i=0; i<max_numbers; i++)
        {
            srand(time(0)+i); // Use time as seed so each time, rand() will call a different number
            int new_num = rand() %random_range + 1;
            nums_stack[i] = new_num;
        }

        if (debug_flag || master_debug_flag)
        {
            printf("Iteration tracker: %d \nFactors set: \nRandom range: 1-%d \nMax numbers used during a single iteration: %d \nTarget count: %d \nCurrent count: %d", iteration_tracker, random_range, max_numbers, target_count, current_count);
            printf("\nThis is the stack of random numbers generated: ");
            for (int i=0; i<max_numbers; i++)
            {
                printf("%d ", nums_stack[i]);
            }
            printf("\n\n");
        }

        // Add to current count
        for (int i=0; i<max_numbers; i++)
        {
            current_count += nums_stack[i];
        }
        /* Summation for loop has O(n) time complexity - same as the python sum function
            Important so that way we can have an apples to apples comparison 
        */
    }

    clock_t end_time = clock();
    double experiment_time = (double)(end_time - start_time)/CLOCKS_PER_SEC;

    if (final_debug_flag || master_debug_flag)
    {
        printf("Total number of iterations: %d\nActual count reached: %d\nExperiment target count: %d\nMax nubers per iteration %d\nMax in random range %d\nDebug flags enabled %d\nTotal time taken %f\n\n\n\n", iteration_tracker, current_count, target_count, max_numbers, random_range, master_debug_flag, experiment_time);
        // printf("Start time %f\nEnd time %f", start_time-(clock_t)0, end_time-(clock_t)0);
    }
}
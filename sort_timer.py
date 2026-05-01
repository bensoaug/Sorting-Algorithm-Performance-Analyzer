# Author: Augustus Benson
# GitHub username: bensoaug
# Date: 04-29-2026
# Description: Times bubble sort and insertion sort on random lists,
# then graphs the results for comparison.

import time
import random
from matplotlib import pyplot


def bubble_time(number_list):
    """
    Sorts a list using bubble sort and returns the elapsed time in seconds.
    """
    start_time = time.perf_counter()

    for pass_num in range(len(number_list) - 1):
        for index in range(len(number_list) - 1 - pass_num):
            if number_list[index] > number_list[index + 1]:
                temp_value = number_list[index]
                number_list[index] = number_list[index + 1]
                number_list[index + 1] = temp_value

    end_time = time.perf_counter()
    return end_time - start_time


def insertion_time(number_list):
    """
    Sorts a list using insertion sort and returns the elapsed time in seconds.
    """
    start_time = time.perf_counter()

    for current_index in range(1, len(number_list)):
        current_value = number_list[current_index]
        position = current_index - 1

        while position >= 0 and number_list[position] > current_value:
            number_list[position + 1] = number_list[position]
            position -= 1

        number_list[position + 1] = current_value

    end_time = time.perf_counter()
    return end_time - start_time


def sort_times_for_random_list(list_length):
    """
    Creates a random list and returns the bubble sort and insertion sort times.
    """
    first_list = []

    for count in range(list_length):
        random_number = random.randint(1, list_length)
        first_list.append(random_number)

    second_list = list(first_list)

    bubble_sort_time = bubble_time(first_list)
    insertion_sort_time = insertion_time(second_list)

    return bubble_sort_time, insertion_sort_time


def compare_sorts():
    """
    Graphs bubble sort and insertion sort times for different list lengths.
    """
    list_lengths = [1000, 2000, 3000, 4000, 5000,
                    6000, 7000, 8000, 9000, 10000]

    bubble_times = []
    insertion_times = []

    for list_length in list_lengths:
        bubble_sort_time, insertion_sort_time = sort_times_for_random_list(list_length)

        bubble_times.append(bubble_sort_time)
        insertion_times.append(insertion_sort_time)

    pyplot.plot(list_lengths, bubble_times, 'ro--', linewidth=2, label='Bubble Sort')
    pyplot.plot(list_lengths, insertion_times, 'go--', linewidth=2, label='Insertion Sort')

    pyplot.xlabel("Length of List")
    pyplot.ylabel("Time in Seconds")
    pyplot.legend(loc='upper left')
    pyplot.show()


def main():
    """
    Runs the sort comparison graph.
    """
    compare_sorts()


if __name__ == "__main__":
    main()

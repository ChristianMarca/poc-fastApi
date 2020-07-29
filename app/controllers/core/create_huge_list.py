import time
from random import random
from math import ceil
import sys


def run_create_huge_list_for_n_seconds(data_slot, sec):
    huge_list = []
    start_time = time.perf_counter()
    iteration_number = 0
    total_time = 0

    while True:
        huge_list.append([8] * ceil(random() * data_slot))
        end_time = time.perf_counter()
        iteration_number += 1
        total_time = end_time - start_time

        if total_time >= sec:
            break

    return {
        "iteration_number": f"Function executed {iteration_number}",
        "time": total_time,
        "used_memory": sys.getsizeof(huge_list)
    }

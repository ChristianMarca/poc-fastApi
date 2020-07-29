import time


def add_plus_one(n, execution_time):
    print('START_RUN')
    start_time = time.perf_counter()
    iteration_number = 0
    total_time = 0

    while True:
        current_number = n + 1
        end_time = time.perf_counter()
        iteration_number += 1
        total_time = end_time - start_time

        if total_time >= execution_time:
            break
    return {"iteration_number": f"Function executed {iteration_number}", "time": total_time}

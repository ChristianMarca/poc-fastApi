import time


def fib(n):
    return 1 if n < 2 else fib(n - 1) + fib(n - 2)


def run_fib_for_n_seconds(max_number, sec):
    print('->>>', max_number, sec)
    start_time = time.perf_counter()
    iteration_number = 0
    total_time = 0

    while True:
        fib(max_number)
        end_time = time.perf_counter()
        iteration_number += 1
        total_time = end_time - start_time

        if total_time >= sec:
            break

    return {"iteration_number": f"Function executed {iteration_number}", "time": total_time}

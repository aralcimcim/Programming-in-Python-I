import argparse
import multiprocessing
import math

# def sum_of_fractions(start:int, end: int) -> float:
#     return sum(1 / k for k in range(start, end))

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-p", "--processes", type=int, default=1)
#     parser.add_argument("-n", "--n", type=int, default=1000)
#     args = parser.parse_args()

#     num_processes = args.processes
#     num_terms = args.n

#     pool = multiprocessing.Pool(processes=num_processes)

#     print(f"Number of processes: {num_processes}")
#     print(f"Number of terms: {num_terms}")

#     list_of_args = []
#     for i in range(num_processes):
#         start = (i * int(num_terms / num_processes)) + 1
#         print(start, i)
#         end = ((i + 1) * int(num_terms / num_processes)) + 1
#         list_of_args.append((start, end))

#     print(f"List of args: {list_of_args}")

#     results = pool.starmap(sum_of_fractions, list_of_args)

#     gamma = -math.log(num_terms) + sum(results)

#     print(f"Euler-Mascheroni constant approximation ({num_terms} terms): {gamma:.9f}")

def sum_of_fractions(start:int, end: int) -> float:
    return sum(1 / k for k in range(start, end))

def main(num_processes: int, num_terms: int):
    pool = multiprocessing.Pool(processes=num_processes)

    list_of_args = []
    for i in range(num_processes):
        start = (i * int(num_terms / num_processes)) + 1
        end = ((i + 1) * int(num_terms / num_processes)) + 1
        list_of_args.append((start, end))

    results = [pool.apply(sum_of_fractions, args) for args in list_of_args]

    gamma = -math.log(num_terms) + sum(results)

    print(f"Euler-Mascheroni constant approximation ({num_terms} terms): {gamma:.9f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--processes", type=int, default=1)
    parser.add_argument("-n", "--n", type=int, default=1000)
    args = parser.parse_args()

    main(args.processes, args.n)


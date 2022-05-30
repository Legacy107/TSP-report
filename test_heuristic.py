from tsp_gen import gen_test
from tsp_greedy_test import tsp_greedy
from tsp_mst_test import tsp_mst
from tsp_dp_test import tsp_dp
import concurrent.futures
import psutil
import time
import os

def run_greedy(filename, number_city, test_number):
    result = tsp_greedy(filename)
    print(f"Completed greedy test {test_number} of n = {number_city}")
    return result

def run_mst(filename, number_city, test_number):
    result = tsp_mst(filename)
    print(f"Completed mst test {test_number} of n = {number_city}")
    return result

def run_dp(filename, number_city, test_number):
    result = tsp_dp(filename)[1]
    print(f"Completed dp test {test_number} of n = {number_city}")
    return result


def main():
    start = 3
    end = 22
    test_size = 100
    batch = psutil.cpu_count(logical=False) // 2

    with open("result_greedy.txt", "a") as file_greedy, open("result_mst.txt", "a") as file_mst, concurrent.futures.ProcessPoolExecutor() as executor:
        for number_city in range(start, end):
            time_greedy = 0.0
            score_greedy = 0.0
            time_mst = 0.0
            score_mst = 0.0

            # split test into batches base on cpu count
            for batch_start in range(0, test_size, batch):
                greedy_futures = []
                mst_futures = []
                dp_futures = []

                for test_number in range(batch_start, min(batch_start + batch, test_size)):
                    filename = f"input_{test_number}.txt"
                    gen_test(number_city, filename)

                    dp_futures.append(executor.submit(run_dp, filename, number_city, test_number))
                    greedy_futures.append(executor.submit(run_greedy, filename, number_city, test_number))
                    mst_futures.append(executor.submit(run_mst, filename, number_city, test_number))

                optimals = [f.result() for f in dp_futures]
                greedy_results = [f.result() for f in greedy_futures]
                mst_results = [f.result() for f in mst_futures]

                time_greedy += sum([result[0] for result in greedy_results])
                score_greedy += sum([(result[1] - optimals[id]) / optimals[id] for id, result in enumerate(greedy_results)])

                time_mst += sum([result[0] for result in mst_results])
                score_mst += sum([(result[1] - optimals[id]) / optimals[id] for id, result in enumerate(mst_results)])

            file_greedy.write(f"{number_city} {time_greedy / float(test_size)} {score_greedy / float(test_size)}\n")
            file_mst.write(f"{number_city} {time_mst / float(test_size)} {score_mst / float(test_size)}\n")
    
    # cleanup
    for number_city in range(test_size):
        os.remove(f"input_{number_city}.txt")

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f"Finished process in {end - start} seconds")

from tsp_gen import gen_test
from tsp_br_test import tsp_br
from tsp_dp_test import tsp_dp
import concurrent.futures
import psutil
import time
import os

def run_br(filename, number_city, test_number):
    runtime = tsp_br(filename)[0]
    print(f"Completed br test {test_number} of n = {number_city}")
    return runtime

def run_dp(filename, number_city, test_number):
    runtime = tsp_dp(filename)[0]
    print(f"Completed dp test {test_number} of n = {number_city}")
    return runtime

def main():
    start = 10
    end = 11
    test_size = 20
    batch = psutil.cpu_count(logical=False) // 2

    with (
        open("result_br.txt", "a") as file_br,
        open("result_dp.txt", "a") as file_dp,
        concurrent.futures.ProcessPoolExecutor() as executor
    ):
        for number_city in range(start, end):
            time_br = 0.0
            time_dp = 0.0

            for batch_start in range(0, test_size, batch):
                br_futures = []
                dp_futures = []

                for test_number in range(batch_start, min(batch_start + batch, test_size)):
                    filename = f"input_{test_number}.txt"
                    gen_test(number_city, filename)

                    br_futures.append(executor.submit(run_br, filename, number_city, test_number))
                    dp_futures.append(executor.submit(run_dp, filename, number_city, test_number))
                
                time_br += sum([f.result() for f in br_futures])
                time_dp += sum([f.result() for f in dp_futures])

            file_br.write(f"{number_city} {time_br / float(test_size)}\n")
            file_dp.write(f"{number_city} {time_dp / float(test_size)}\n")

    for number_city in range(test_size):
        os.remove(f"input_{number_city}.txt")


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f"Finished process in {end - start} seconds")

from tsp_gen import gen_test
from tsp_br_test import tsp_br
from tsp_dp_test import tsp_dp
import threading
import os

start = 3
end = 22
test_size = 100

with open("result_br.txt", "a") as file_br, open("result_dp.txt", "a") as file_dp:
    for i in range(start, end):
        time_br = 0.0
        time_dp = 0.0
        br_threads = []
        dp_threads = []
        for j in range(test_size):
            filename = f"input_{j}.txt"
            gen_test(i, filename)

            def run_br(i, j):
                global time_br
                time_br += tsp_br(filename)[0]
                print(f"Completed br test {j} of n = {i}")
            
            def run_dp(i, j):
                global time_dp
                time_dp += tsp_dp(filename)[0]
                print(f"Completed dp test {j} of n = {i}")

            t_br = threading.Thread(target=run_br, args=(i, j,))
            t_dp = threading.Thread(target=run_dp, args=(i, j,))
            br_threads.append(t_br)
            dp_threads.append(t_dp)

        for t in br_threads:
            t.start()
        for t in br_threads:
            t.join()

        for t in dp_threads:
            t.start()
        for t in dp_threads:
            t.join()

        file_br.write(f"{i} {time_br / float(test_size)}\n")
        file_dp.write(f"{i} {time_dp / float(test_size)}\n")

for i in range(test_size):
    os.remove(f"input_{i}.txt")

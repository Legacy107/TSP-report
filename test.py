from tsp_gen import gen_test
from tsp_br_test import tsp_br
from tsp_dp_test import tsp_dp

with open("result_br.txt", "a") as file_br, open("result_dp.txt", "a") as file_dp:
    for i in range(20, 22):
        time_br = 0.0
        time_dp = 0.0
        for j in range(10):
            gen_test(i)
            # time_br += tsp_br()[0]
            time_dp += tsp_dp()[0]
            print(f"Completed test {j} of n = {i}")

        file_br.write(f"{i} {time_br / 10.0}\n")
        file_dp.write(f"{i} {time_dp / 10.0}\n")

from tsp_gen import gen_test
from tsp_greedy_test import tsp_greedy
from tsp_mst_test import tsp_mst
from tsp_dp_test import tsp_dp

start = 3
end = 4
test_size = 100

with open("result_greedy.txt", "a") as file_greedy, open("result_mst.txt", "a") as file_mst:
    for i in range(start, end):
        time_greedy = 0.0
        score_greedy = 0.0
        time_mst = 0.0
        score_mst = 0.0
        for j in range(test_size):
            gen_test(i, "input.txt")

            optimal = tsp_dp("input.txt")[1]

            greedy = tsp_greedy("input.txt")
            time_greedy += greedy[0]
            score_greedy += (greedy[1] - optimal) / optimal

            mst = tsp_mst("input.txt")
            time_mst += mst[0]
            score_mst += (mst[1] - optimal) / optimal

            print(f"Completed test {j} of n = {i}")

        file_greedy.write(f"{i} {time_greedy / float(test_size)} {score_greedy / float(test_size)}\n")
        file_mst.write(f"{i} {time_mst / float(test_size)} {score_mst / float(test_size)}\n")

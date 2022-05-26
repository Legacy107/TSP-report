from tsp_gen import gen_test
from tsp_greedy_test import tsp_greedy
from tsp_mst_test import tsp_mst
from tsp_dp_test import tsp_dp

with open("result_greedy.txt", "a") as file_greedy, open("result_mst.txt", "a") as file_mst:
    for i in range(3, 22):
        time_greedy = 0.0
        score_greedy = 0.0
        time_mst = 0.0
        score_mst = 0.0
        for j in range(10):
            gen_test(i)

            optimal = tsp_dp()[1]

            greedy = tsp_greedy()
            time_greedy += greedy[0]
            score_greedy += (greedy[1] - optimal) / optimal

            mst = tsp_mst()
            time_mst += mst[0]
            score_mst += (mst[1] - optimal) / optimal

            print(f"Completed test {j} of n = {i}")

        file_greedy.write(f"{i} {time_greedy / 10.0} {score_greedy / 10.0}\n")
        file_mst.write(f"{i} {time_mst / 10.0} {score_mst / 10.0}\n")

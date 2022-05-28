from random import randint

def gen_test(n, filename):
    with open(filename, "w") as file:
        file.write(f"{n}\n")

        for i in range(n):
            for j in range(i + 1, n):
                file.write(f"{i + 1} {j + 1} {randint(2, 50)}\n")

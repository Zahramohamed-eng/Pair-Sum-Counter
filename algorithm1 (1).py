 import time
import random

def count_pairs_naive(arr, L, R):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if L <= arr[i] + arr[j] <= R:
                count += 1
    return count         

def main():
    arr = [random.randint(1, 10000) for _ in range(2000)]
    L, R = 5000, 15000

    start = time.perf_counter()
    naive = count_pairs_naive(arr, L, R)
    t1 = time.perf_counter() - start

    print("Naive Solution")
    print(f"Pairs : {naive}")
    print(f"Time  : {t1:.5f} sec")

if __name__ == "__main__":
    main()



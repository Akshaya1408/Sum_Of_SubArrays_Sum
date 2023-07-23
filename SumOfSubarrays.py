def sum_of_all_subarray_sums(A):
    n = len(A)
    total_sum = 0

    for i in range(n):
        total_sum += A[i] * (i + 1) * (n - i)

    return total_sum

A=list(map(int,input().split()))
print(sum_of_all_subarray_sums(A))
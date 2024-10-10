import sys
import math

if __name__ == "__main__":
    a = sys.stdin.readline().split()
    n, m = int(a[0]), int(a[1])
    arr = sys.stdin.readline().strip().split()
    arr = [int(x) for x in arr]

    between = [[0] * n for _ in range(n)]
    for i in range(n):
        between[i][i] = arr[i]
        for j in range(i+1, n):
            between[i][j] = math.gcd(between[i][j-1], arr[j])
    
    # print(between)

    max_gcd = [[0] * m for _ in range(n)]
    for i in range(n):
        max_gcd[i][0] = between[0][i]
    for i in range(1, n):
        for j in range(1, m):
            for k in range(i):
                if max_gcd[k][j-1] != 0:
                    max_gcd[i][j] = max(max_gcd[i][j], max_gcd[k][j-1] + between[k+1][i])
    
    # print(max_gcd)
    
    print(max_gcd[n-1][m-1])
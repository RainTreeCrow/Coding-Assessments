import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    day = 0
    while n > 0:
        if is_prime(n):
            today = int(n / 3) + 1
        else:
            today = int(n / 2) + 1
        n = n - today
        day = day + 1

    print(day)
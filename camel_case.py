import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    results = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        parts = [part.capitalize() for part in line.split('_')]
        results.append(''.join(parts))
    
    for res in results:
        print(res)
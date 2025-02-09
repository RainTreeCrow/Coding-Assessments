def FirstFactorial(num):
    # code goes here
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# keep this function call here
print(FirstFactorial(input()))
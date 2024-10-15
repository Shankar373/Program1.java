def count_multiples(arr):
    multiples_count = {i: 0 for i in range(1, 10)}
    for num in arr:
        for i in range(1, 10):
            if num % i == 0:
                multiples_count[i] += 1
    return multiples_count
user_input = input("Enter numbers separated by commas: ")
arr = [int(num.strip()) for num in user_input.split(',')]  
result = count_multiples(arr)
print(result)

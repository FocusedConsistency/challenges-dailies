def is_fizz_buzz(arr):
    num_arr = []
    for i, el in enumerate(arr):
        if isinstance(el, int):
            for num in range(len(arr)):
                num_arr.append(el - i + num)
            break
    for i, num in enumerate(num_arr):
        if num % 15 == 0:
            if arr[i] != "FizzBuzz":
                return False
        elif num % 3 == 0:
            if arr[i] != "Fizz":
                return False
        elif num % 5 == 0:
            if arr[i] != "Buzz":
                return False
        
    return True

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_list = [0, 1]  # Initialize with first two Fibonacci numbers
    
    while len(fibonacci_list) < n:
        next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_fibonacci)
    
    return fibonacci_list
# 13.	Write a program to print all prime numbers between 1 and 50.

print("Prime numbers between 1 and 50 are:")

for p in range(2, 51): 
    is_prime = True
    for i in range(2, int(p**0.5) + 1):  # Check divisibility from 2 to sqrt(p)
        if p % i == 0:  # If p is divisible by i, it's not prime
            is_prime = False
            break  # No need to check further, exit the loop
    if is_prime:  # If p is still considered prime
        print(p, end=" ")  # Print the prime number
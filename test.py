n = int(input("Enter a number: "))
is_prime = True
for x in range(2, n):
    if n % x == 0:
        is_prime = False
if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
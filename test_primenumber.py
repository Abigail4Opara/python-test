>>> from prime_number import is_prime

>>> is_prime('five')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/home/bala/unit-test-1/prime_number.py", line 5, in is_prime
for i in range(2,int(math.sqrt(num))+1):
    TypeError: must be real number, not str

>>> is_prime(-10)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/home/bala/unit-test-1/prime_number.py", line 5, in is_prime
for i in range(2,int(math.sqrt(num))+1):
ValueError: math domain error

>>> is_prime(2.5)
True
"""Escribe un archivo fibonacci.py que solicite un número al usuario y genere
secuencia de Fibonacci hasta ese número."""
"""Iteration 1: a = 0, b = 1 a, b = b, a + b => a = 1, b = 1

Iteration 2: a = 1, b = 1 a, b = b, a + b => a = 1, b = 2

Iteration 3: a = 1, b = 2 a, b = b, a + b => a = 2, b = 3

Iteration 4: a = 2, b = 3 a, b = b, a + b => a = 3, b = 5

Iteration 5: a = 3, b = 5 a, b = b, a + b => a = 5, b = 8

So, the first 5 Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8..."""

#F(n) = F(n-1) + F(n-2)
def fibanachi(n):
    #a->F(n-1); b->F(n-2)
    a,b = 0,1
    while a < n:
        #a->F(n-2); b->F(n-1)
        print(a)
        a,b = b, +ab

fibanachi(int(input("Enter a number: ")))
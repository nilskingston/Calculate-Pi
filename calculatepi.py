"""
calculatepi.py
Author: Nils Kingston
Credit: Roger
Assignment:

Write and submit a Python program that computes an approximate value of π by calculating the following sum:

(see: https://github.com/HHS-IntroProgramming/Calculate-Pi/blob/master/README.md)

This sum approaches the true value of π as n approaches ∞.

Your program must ask the user how many terms to use in the estimate of π, how many decimal places, 
then print the estimate using that many decimal places. Exactly like this:

I will estimate pi. How many terms should I use? 100
How many decimal places should I use in the result? 7
The approximate value of pi is 3.1315929


Note: remember that the printed value of pi will be an estimate!

"""
print("I will estimate pi")
terms = int(input("How many terms should I use? "))
decimal = int(input("How many decimal places should I use in the result?" ))

p = 1.0/sum([((-1.0)**k)

print("The approximate value of pi is ")

#!/usr/bin/env python3
import sys
# Lab 16: recursion
# Fibonacci with cache


sys.setrecursionlimit(5000000)

global fib_cache
fib_cache = {}

def main():
	print(fibonacci(0))
	print(fibonacci(100))
	print(fibonacci(101))

def fibonacci(n):
	if n == 0 or n == 1:
		return n
	elif n in fib_cache:
		return fib_cache.get(n)
	else:
		x = fibonacci(n-1) + fibonacci(n-2)
		fib_cache[n] = x
		print("Recursion step")
		return x

main()
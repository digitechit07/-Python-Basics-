'''
Recursion means a function calling
itself to solve a smaller part of the same
problem until it reaches a stopping condition (base case).
'''

def countdown (n):
    if n == 0:
        return 1
    print(n)
    countdown(n-1)
    

countdown(5)
#just a comment
def fib(n):
    sequence = [0] * n
    for i in range(n):
        if i == 0 or i == 1:
            sequence[i] = i
        else:
            sequence[i] = sequence[i-1] + sequence[i-2]
    return sequence



n = 100
fib_sequence = fib(n)
print(fib_sequence)
from sympy import symbols, Eq, solve, core

a = []
b = []
prices = []

with open("data.txt", "r") as f:
    while True:
        a_line = f.readline()
        if not a_line: break

        a.append(list(map(int, a_line.split(": X")[1].split(", Y"))))
        b.append(list(map(int, f.readline().split(": X")[1].split(", Y"))))
        prices.append(list(map(int,f.readline().split(": X=")[1].split(", Y="))))
        f.readline()

A, B = symbols('a b')
answer = 0

for index in range(len(prices)):
    eq1 = Eq(a[index][0] * A + b[index][0] * B, prices[index][0])
    eq2 = Eq(a[index][1] * A + b[index][1] * B, prices[index][1])

    solution = solve((eq1, eq2), (A, B))
    if isinstance(solution[A], core.numbers.Integer) and isinstance(solution[B], core.numbers.Integer):
        answer += (solution[A] * 3 + solution[B])
print(answer)
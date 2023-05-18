# x = 10

# def fnc(x):
#     global x
#     x = x + 2
#     print(x)

# print(x)
# x = 2
# print(x)

# def fnc(a, b=10):
#     c = a + b
#     return c

# result1 = fnc(10)
# print(result1)

# result2 = fnc(2, 5)
# print(result2)

# def fnc(a, *_, **b):
#     print(len(_))
#     sum = 0
#     for _ in b:
#         sum += b[_]
#     return sum

# result = fnc(10, 20, 30, i=1, j=2, k=3, l=4)
# print(result)

# def fnc(n):
#     if n == 3:
#         return 3
#     return fnc(n - 1) + n

# result = fnc(5)
# print(result)

def fnc(x):
    def add_ten():
        return x + 10
    return add_ten

first = fnc(5)

print(first)
print(first())
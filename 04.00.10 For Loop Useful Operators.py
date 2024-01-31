result = 0
debt = 1000
prod = 1
divine = 100
n = 5
for i in range(1, n + 1):
    result += i   # the same as result = result + i
    debt -= i     # the same as debt = debt - i
    prod *= i     # the same as prod = prod * i
    divine /= i   # the same as divine = divine / i
print(result)
print(debt)
print(prod)
print(divine)
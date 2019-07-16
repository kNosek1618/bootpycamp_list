
# INDEX

numbers = [5, 8, 2, 4, 7, 4, 6, 1, 0, 8, 8, 8]
string_list = ["the", "first", "lesson", "in", "my", "live"]

print(numbers.index(1))
print(numbers.index(8))

print(numbers.index(4, 1))
print(numbers.index(8, 2))

# INDEX FROM NUMBER BETWEEN
print(numbers.index(7, 2, 6))

# COUNT

print("\n")
print(numbers.count(8))

# reverse
numbers.reverse()
print(numbers)

# SORT

numbers.sort()
print(numbers)

# JOIN

print("<>".join(str(numbers)))
print("<>".join(string_list))
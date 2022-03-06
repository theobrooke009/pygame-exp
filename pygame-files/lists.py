numbers = [10, 20, 30]

doubled_numbers = list(map(lambda number: number * 2, numbers))

print(doubled_numbers)

doubled_numbers_comp = [number * 2 for number in numbers]

print(doubled_numbers_comp)

numbers = [1, 3, 4, 10]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print(even_numbers)

even_numbers_comp = [number for number in numbers if number % 2 == 0]

print(even_numbers_comp)


even_numbers_doubled = [number * 2 for number in numbers if number % 2 == 0]

print(even_numbers_doubled)

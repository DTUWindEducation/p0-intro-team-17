from functions import greet, goldilocks, square_list, fibonacci_stop, clean_pitch

# Call functions with example inputs
greet("world")

goldilocks(139)
goldilocks(145)
goldilocks(151)

print(square_list([1, 2, 3]))

print(fibonacci_stop(30))

x = [-1, 2, 6, 95]
status = [1, 0, 0, 0]
print(clean_pitch(x, status))

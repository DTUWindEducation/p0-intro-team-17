def greet(name):
    print(f"Hello, {name}!")

def goldilocks(bed_length):
    if bed_length < 140:
        print("Too small!")
    elif bed_length > 150:
        print("Too large!")
    else:
        print("Just right. :)")

def square_list(numbers):
    return [num ** 2 for num in numbers]

def fibonacci_stop(max_value):
    fib_sequence = [1, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib >= max_value:
            break
        fib_sequence.append(next_fib)
    return fib_sequence

def clean_pitch(pitch_angles, status_signals):
    return [-999 if (angle < 0 or angle > 90) and status > 0 else angle for angle, status in zip(pitch_angles, status_signals)]

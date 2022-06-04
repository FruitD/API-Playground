error_string = 'out of bounds or not an integer'

while True:
    try:
        entry = int(input(''))
        break
    except ValueError:
        print(error_string)


def output_what_is_inputted(entry):
    if 10 ^ 5 <= entry <= 0:
        print(error_string)

    else:
        print(entry)


output_what_is_inputted(entry)

# https://www.codechef.com/LP0TO101?order=desc&sortBy=successful_submissions

def get_division_remainder(a, b):
    error_string = 'Error: Out of bounds'
    t = int(input())
    for x in range(t):
        a, b = map(int, input().split())
        print(a % b)

    if 1 <= t <= 1000:
        print(error_string)

    elif 1 <= a <= 10000 | 1 < b <= 10000:
        print(error_string)

    else:
        print('Hi')

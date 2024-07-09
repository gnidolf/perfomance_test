import sys

def get_value(i, n, m):
    return 1 + (i + m - 2) % n


def circular_array_path(n, m):
    i = 1
    while True:
        print(i, end='')
        i = get_value(i, n, m)
        if i == 1:
            break
    print()


if len(sys.argv) < 3:
    print('Недостаточно аргументов')
    sys.exit()
else:
    n, m = int(sys.argv[1]), int(sys.argv[2])

circular_array_path(n, m)

import sys, os


def read_circle(file1):
    with open(file1, 'r') as file:
        x, y = map(int, file.readline().split())
        r = int(file. readline())
    
    return (x, y), r


def read_points(file2):
    points = []
    with open(file2, 'r') as file:
        for line in file:
            x, y = line.split()
            point = (int(x), int(y))
            points.append(point) 
    
    return points


def calculate_pos(circle, radius, point):
    distance = ((point[0] - circle[0])**2 + (point[1] - circle[1])**2)**0.5
    if distance < radius:
        return 1
    elif distance == radius:
        return 0
    else:
        return 2


if len(sys.argv) < 3:
    print('Недостаточно аргументов')
    sys.exit()
elif not os.path.exists(sys.argv[1]) or not os.path.exists(sys.argv[2]):
    print('Файл не сущесвует')
    sys.exit()
else:
    file1, file2 = sys.argv[1], sys.argv[2]

circle, radius = read_circle(file1)
points = read_points(file2)

for point in points:
    position = calculate_pos(circle, radius, point)
    print(position)

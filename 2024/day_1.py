from sys import stdin
from sys import argv


def part_1():
    l, r = [], []
    for i in stdin:
        left, right = map(int, i.split())
        l.append(left)
        r.append(right)

    l.sort()
    r.sort()

    ans = 0
    for i in range(len(l)):
        ans += abs(l[i] - r[i])

    print(ans)


def part_2():
    l = []
    r = {}
    for i in stdin:
        left, right = map(int, i.split())
        l.append(left)

        if right in r:
            r[right] += 1
        else:
            r[right] = 1

    ans = 0
    for num in l:
        if num in r:
            ans += r[num] * num
    print(ans)


if __name__ == '__main__':
    if len(argv) != 2:
        raise IOError(f'Usage: python3 day_1.py [1|2]')

    if argv[1] == '1':
        part_1()
    else:
        part_2()

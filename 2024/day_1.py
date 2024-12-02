from sys import stdin

def part_1(l, r):
    l.sort()
    r.sort()
    ans = 0
    for i in range(len(l)):
        ans += abs(l[i] - r[i])

    print(ans)


def part_2(l, r):
    ans = 0
    for num in l:
        if num in r:
            ans += r[num] * num
    print(ans)


if __name__ == '__main__':
    l, r1, r2 = [], [], {}
    for i in stdin:
        left, right = map(int, i.split())
        l.append(left)
        r1.append(right)
        if right in r2: r2[right] += 1
        else: r2[right] = 1


    part_1(l, r1)
    part_2(l, r2)

from sys import stdin
import re

def part_1(inpoo):
    ans = 0
    for i in range(0, len(inpoo) - 3):
        for j in range(0, len(inpoo) - 3):
            # / direction
            f = inpoo[i + 3][j] + inpoo[i + 2][j + 1] + inpoo[i + 1][j + 2] + inpoo[i][j + 3] 
            # \ direction
            b = inpoo[i][j] + inpoo[i + 1][j + 1] + inpoo[i + 2][j + 2] + inpoo[i + 3][j + 3]


            if f == 'XMAS' or f == 'SAMX': ans += 1
            if b == 'XMAS' or b == 'SAMX': ans += 1

    for row in inpoo:
        ans += len(re.findall('XMAS', row)) + len(re.findall('SAMX', row))


    for i in range(len(inpoo)):
        col = ''
        for j in range(len(inpoo)):
            col += inpoo[j][i]

        ans += len(re.findall('XMAS', col)) + len(re.findall('SAMX', col))
    print(ans)        

def part_2(inpoo):
    ans = 0
    for i in range(0, len(inpoo) - 2):
        for j in range(0, len(inpoo[0]) - 2):

            # / direction
            f = inpoo[i + 2][j] + inpoo[i + 1][j + 1] + inpoo[i][j + 2]
            # \ direction
            b = inpoo[i][j] + inpoo[i + 1][j + 1] + inpoo[i + 2][j + 2]

            if (f == 'MAS' or f == 'SAM') and (b == 'MAS' or b == 'SAM'):
                ans += 1
    print(ans)


if __name__ == '__main__':
    inpoo = [l.split('\n')[0] for l in stdin]
    part_1(inpoo)
    part_2(inpoo)

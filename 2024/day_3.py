from sys import stdin
import re

def calc(muls):
    out = 0
    for i in muls:
        l, r = map(int, re.findall('[0-9]+', i))
        out += l * r
    return out

def part_1(inpoo):
    ans = 0
    for l in inpoo:
        muls = re.findall('mul\([0-9]+,[0-9]+\)', l)
        ans += calc(muls)
    print(ans)

def part_2(inpoo):
    ans = 0
    lastDo = True
    for line in inpoo:
        dont = re.split("don\'t\(\)", line)
        do = re.split("do()", line)
        for i, c_str in enumerate(dont):
            muls = re.findall('mul\([0-9]+,[0-9]+\)', c_str) if i == 0 and lastDo \
                else re.findall('mul\([0-9]+,[0-9]+\)', ''.join(re.split('do\(\)', c_str)[1:]))
            ans += calc(muls)
        lastDo = len(do[-1]) < len(dont[-1])

    print(ans)
        
if __name__ == '__main__':
    inpoo = [l for l in stdin]
    part_1(inpoo)
    part_2(inpoo)

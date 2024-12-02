from sys import stdin

def is_safe(arr):
    inc = [arr[i] - arr[i-1] for i in range(1, len(arr))]
    tracker = set(inc)

    return tracker <= {1,2,3} or tracker <= {-1,-2,-3}
    
def part_1(inpoo):
    ans = 0
    for nums in inpoo:
        if is_safe(nums): ans += 1
    print(ans)

def part_2(inpoo):
    ans = 0
    for nums in inpoo:
        for i in range(len(nums)):
            if is_safe(nums[:i] + nums[i+1:]):
                ans += 1
                break
    print(ans)

if __name__ == '__main__':
    inpoo = []
    for l in stdin:
        inpoo.append([int(x) for x in l.split()])

    part_1(inpoo)
    part_2(inpoo)


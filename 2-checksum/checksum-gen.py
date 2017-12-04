import unittest

def solve_1(matrix):
    nums = []
    for row in matrix:
        if row == []: break
        high = low = row[0]
        for n in row:
            if n > high:
                high = n
            elif n < low:
                low = n
        nums.append(high - low)

    return sum(nums)

def solve_2(matrix):
    nums = []
    for row in matrix:
        if row == []: break
        high = low = row[0]
        for i, n1 in enumerate(row):
            for n2 in row[i:]:
                big = max(n1, n2)
                small = min(n1, n2)
                #print("{} : {} : {}".format(big, small, big % small))
                if big % small == 0 and big != small:
                    nums.append(big / small)
                    break

    return sum(nums)

def main():
    data = open('input.txt','r').readlines()
    str_matrix = [line.split() for line in data]
    matrix = [[int(n) for n in row] for row in str_matrix]
    print("Solution 1: {}".format(solve_1(matrix)))
    print("Solution 2: {}".format(solve_2(matrix)))

if __name__ == '__main__':
    main()

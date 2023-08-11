def isCross(n, i, j):
    if n[i][j] and n[i - 1][j] and n[i + 1][j] and n[i][j - 1] and n[i][j + 1]:
        return True
    return False


def countCross(numbers):
    result = 0
    for i in range(1, len(numbers) - 1):
        for j in range(1, len(numbers[i]) - 1):
            if isCross(numbers, i, j):
                result += 1

    """ 
    Code your program here
    """
    return result


def main():
    numbers = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
               [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

    result = countCross(numbers)
    print(result)


if __name__ == '__main__':
    main()

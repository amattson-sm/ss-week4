from math import ceil


def problem_four(p, r, m):
    # get correct interest rate multiplier and perform calculation
    rate = r / 1200
    return ceil(p * (rate * (1 + rate) ** m) / ((1 + rate) ** m - 1))


if __name__ == '__main__':
    # add numbers
    one = (50 + 50) + (100 - 10)
    print("1.  ", one)

    # misc math
    two = 30 * 6, 6 ^ 6, 6 ** 6, 6 + 6 + 6 + 6 + 6 + 6
    print("2.  ", two)

    # printing
    three = "Hello World"
    print("3a. ", three)
    print("3b. ", three + " : 10")

    # math exercise
    four_a = problem_four(800000, 6, 103)
    four_b = problem_four(200000, 40, 20)
    print("4a. ", (800000, 6, 103), " -> ", four_a)
    print("4a. ", (200000, 40, 20), " -> ", four_b)

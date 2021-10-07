def func():
    print("1.   Hello World")


def func2(name):
    print(f"2.   Hi My name is {name}")


def func3(x, y, z):
    if z:
        return x
    return y


def func4(x, y):
    return x * y


def is_even(x):
    return x % 2 == 0


def is_greater(x, y):
    return x > y


def arbitrary_sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total


def arbitrary_evens(*nums):
    my_list = []
    for num in nums:
        if num % 2 == 0:
            my_list.append(num)
    return my_list


def weird_cases(string):
    new_string = ""
    capital = False
    for char in string:
        if capital:
            new_string += char.upper()
        else:
            new_string += char.lower()
        capital = not capital
    return new_string


def operators(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return min(x, y)
    return max(x, y)


def same_letter(s1, s2):
    if s1[0].lower() == s2[0].lower():
        return True
    return False


def flip_over_seven(x):
    return 7 - (-2 * (7 - x))


def first_and_fourth(x):
    return x[0].upper() + x[1:3] + x[3].upper() + x[4:]


if __name__ == "__main__":
    # print in a function
    func()

    # dynamic func
    func2("Google")

    # conditional func
    print("3a. ", func3("True", "False", True))
    print("3b. ", func3("True", "False", False))

    # product func
    print("4.  ", func4(60, 50))

    # test func
    print("5.  ", is_even(5))

    # first is greater func
    print("6a. ", is_greater(5, 4))
    print("6b. ", is_greater(6, 6))

    # sum arbitrary num of vals
    print("7a. ", arbitrary_sum(2, 5))
    print("7b. ", arbitrary_sum(2, 5, 6, 10, -20, 5003))

    # arbitrary evens
    print("8.  ", arbitrary_evens(2, 4, 6, 7, 7, 8, 8))

    # weird cases
    print("9.  ", weird_cases("Hello World"))

    # lesser or greater on %
    print("10a.", operators(5, 6))
    print("10b.", operators(8, 10))

    # starting with same letter
    print("11a.", same_letter("Apple", "aba"))  # True
    print("11b.", same_letter("ba", "ab"))  # False

    # flip over 7 and double
    print("12a.", flip_over_seven(8))  # 5
    print("12b.", flip_over_seven(1))  # 19

    # capitalize first and fourth
    print("13a.", first_and_fourth("aaaaaaaaa"))
    print("13b.", first_and_fourth("hello world"))

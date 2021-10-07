def print_divisible(start, end):
    nums = ""
    for x in range(start, end + 1):
        if x % 5 == 0 and x % 7 == 0:
            nums += str(x) + ", "
    print(nums)


def c_to_f(celsius):
    return (9 * celsius / 5) + 32


if __name__ == "__main__":
    # divisible by 7 and 5
    print_divisible(1500, 2700)

    # C to F
    print(c_to_f(60))
    print(c_to_f(45))

    # guess a number
    answer = 5
    while True:
        if input("Enter a guess: ") == str(answer):
            print("Well guessed!")
            break
        print("Incorrect guess.")

    # create a pattern
    for a in range(-4, 5):
        output = ""
        for i in range(5, abs(a), -1):
            output += "*"
        print(output)

    # reverse a word
    print("Reversed version:", input("Enter a word to reverse: ")[::-1])

    # count even and odd
    sample_nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    even = 0
    odd = 0
    for item in sample_nums:
        if item % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Input:", sample_nums)
    print("Odd:", odd)
    print("Even:", even)

    # print data and type
    datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
    for item in datalist:
        print("Item:", item, " Datatype:", type(item))

    # 0 to 6, skip 3 and 6
    output = ""
    for num in range(0, 7):
        if num == 3 or num == 6:
            continue
        output += str(num) + " "
    print(output)

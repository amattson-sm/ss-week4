def get_class(bmi):
    if bmi < 18.5:
        return "under"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "over"
    return "obese"


def get_input():
    print("input data:")
    try:
        count = int(input())
        cases = []
        for i in range(0, count):
            new_case = input().strip().split()
            assert len(new_case) == 2
            w = float(new_case[0])
            h = float(new_case[1])
            cases.append(w / (h**2))
        return cases
    except ValueError:
        print("Cannot parse user input.")
        exit(1)
    except AssertionError:
        print("Incorrect input length or type.")


if __name__ == '__main__':
    # user input
    bmi_cases = get_input()

    # run input
    answer = ""
    for case in bmi_cases:
        answer += get_class(case) + ' '
    print(answer)

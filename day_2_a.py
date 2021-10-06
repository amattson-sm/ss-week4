import re


def is_palindrome(x):
    new_x = re.sub(r'[^a-zA-Z]', '', x).lower()
    if new_x == new_x[::-1]:
        return 'Y'
    return 'N'


if __name__ == '__main__':
    # selective letter
    print("Hello World"[8])

    # selective phrase
    print("thinker"[2:5])

    # "hello"[1] = 'e', "Sammy"[2:] = "mmy"
    print(set("Mississippi"))

    # test palindromes
    print(is_palindrome("Amore, roma"))
    print(is_palindrome("No 'x' in Nixon"))
    print(is_palindrome("words 'n stuff"))

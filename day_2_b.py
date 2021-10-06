def sevens_not_fives(begin, end):
    output = ""
    for x in range(begin, end + 1):
        if x % 7 == 0 and x % 5 != 0:
            output += str(x)
            output += ", "
    return output


def factorial(f):
    mul = f
    for x in range(1, f):
        mul *= x
    return mul


def integral_dict(n):
    new_dict = {}
    for x in range(1, n + 1):
        new_dict[x] = x**2
    print(new_dict)


def list_and_tuple(s):
    new_items = s.split(',')
    print(new_items)
    print(tuple(new_items))


class StringClass:
    x = ""

    def get_string(self):
        self.x = input("Input a value for the string class: ")

    def print_string(self):
        print(self.x)


if __name__ == '__main__':
    # print list
    print([1, 1.5, "word"])

    # grab sublist value
    print([1, 1, [1, 2]][2][1])

    # lst[1:] skips first val
    print(['a', 'b', 'c'][1:])

    # dictionary
    my_dict = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5}
    print(my_dict)

    # value of d[k1][1] is 2
    print({'k1': [1, 2, 3]}['k1'][1])

    # list as tuple
    print(tuple([1, [2, 3]]))

    # mississippi to set
    my_set = set("Mississippi")
    print(my_set)

    # add x to set
    my_set.add('X')
    print(my_set)

    # output of a set from a list
    print(set([1, 1, 2, 3]))

    # numbers in range
    print(sevens_not_fives(2000, 3200))

    # factorials
    print(factorial(4))
    print(factorial(8))

    # create and print dict of squares
    integral_dict(8)

    # list and tuple from input
    list_and_tuple("12,24,50,03294")

    # test class
    st = StringClass()
    st.get_string()
    st.print_string()

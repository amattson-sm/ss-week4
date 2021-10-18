if __name__ == "__main__":
    # accounting routine 1
    increase = lambda q, p: q * p + (10 if q * p < 100 else 0)
    routine = lambda data: (data[0], increase(data[2], data[3]))
    sample_data = [[34587, "Learning Python, Mark Lutz", 4, 40.95],
                   [98762, "Programming Python, Mark Lutz", 5, 56.80],
                   [77226, "Head First Python, Paul Barry", 3, 32.95],
                   [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]]
    print(list(map(routine, sample_data)))

    # accounting routine 2
    routine2 = lambda data: (data[0], increase(data[1][1], data[1][2]))
    sample_data2 = [[34587, ("Learning Python, Mark Lutz", 4, 40.95)],
                    [98762, ("Programming Python, Mark Lutz", 5, 56.800)],
                    [77226, ("Head First Python, Paul Barry", 3, 32.95)],
                    [88112, ("Einführung in Python3, Bernd Klein", 3, 24.99)]]
    print(list(map(routine2, sample_data2)))

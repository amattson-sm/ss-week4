def test_crowded(x):
    if len(x) > 3:
        print("It's getting crowded in here...")


def test_crowded_2(x):
    if len(x) > 3:
        print("It's getting crowded in here...")
    else:
        print("The room is not very crowded.")


def test_crowded_3(x):
    if len(x) > 5:
        print("There's a mob in the room.")
    elif len(x) > 2:
        print("It's getting crowded in here...")
    else:
        print("The room is not very crowded.")


if __name__ == "__main__":
    # Three is a Crowd part 1
    print("Part 1")
    crowd = ["me", "you", "him", "them"]
    test_crowded(crowd)
    crowd.pop()
    crowd.remove("me")
    test_crowded(crowd)

    # Three is a Crowd part 2
    print("Part 2")
    crowd.append("bob")
    crowd.append("joe")
    test_crowded_2(crowd)
    crowd.pop()
    test_crowded_2(crowd)

    # Three is a crowd part 3
    print("Part 3")
    crowd.append("jane")
    crowd.append("moe")
    crowd.append("bean")
    test_crowded_3(crowd)
    crowd.pop()
    crowd.pop()
    test_crowded_3(crowd)
    crowd.pop()
    crowd.pop()
    test_crowded_3(crowd)

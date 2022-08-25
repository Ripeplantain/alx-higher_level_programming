#!/usr/bin/python3

if __name__ == "__main__":
    """Sum all the arguements"""
    import sys

    sum = 0
    count = len(sys.argv) - 1
    if count == 0:
        print("0")
    else:
        for i in range(count):
            sum = sum + int(sys.argv[i +1])
        print("{}".format(sum))

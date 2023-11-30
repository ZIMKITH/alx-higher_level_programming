#!/usr/bin/python3
# 3-infinite_add.py

"""Print result of addition of all arguments"""

if __name__ == "__main__":
    import sys
    total = 0
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print("{}".format(total))

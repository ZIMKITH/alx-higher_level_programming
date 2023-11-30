#!/usr/bin/python3
# 4-hidden_discovery.py

"""Print all names defined by compiled module hidden_4.pyc"""

if __name__ == "__main__":
    import hidden_4

    for name in dir(hidden_4):
        if not name.startswith("__"):
            print(name)

#!/usr/bin/python3
'''Determines if all the boxes can be opened'''


def canUnlockAll(boxes):
    '''Define canUnlockAll'''
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    i = [False] * n
    i[0] = True
    j = [0]

    while j:
        box = j.pop()
        for key in boxes[box]:
            if 0 <= key < n and not i[key]:
                j.append(key)
                i[key] = True

    return all(i)

if __name__ == "__main__":
    main()

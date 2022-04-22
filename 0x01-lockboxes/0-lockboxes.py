#!/usr/bin/python3
'''
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
  - There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
'''


def canUnlockAll(boxes):
    '''
    Function to determine if all boxes are opened
    '''
    if type(boxes) != list or len(boxes) < 1:
        return False
    if len(boxes) == 1 and type(boxes[0]) == list:
        return True
    for box in boxes:
        if type(box) != list:
            return False
        for number in box:
            if not isinstance(number, int):
                return False
    boxesOpened = 0
    boxesLength = len(boxes)
    keySet = set()
    keySet.update(boxes[0])
    for round in range(1, boxesLength):
        '''The loop must be done maximum n times'''
        for idx in range(1, boxesLength):
            '''Each box will be checked per round'''
            for key in keySet:
                if key == idx:
                    '''If key is the number of the box,
                    add new keys'''
                    keySet.update(boxes[idx])
                    break
            if len(keySet) == boxesLength - 1:
                '''If keySet has all the keys, return true'''
                return True
    return False

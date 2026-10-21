"""Exercise 03: reproduce and fix a defect."""


def distance(position: int, goal: int) -> int:
    result = abs(position - goal)
    assert result >= 0, "Khoảng cách không thể là số âm"
    return result

print(distance(1, 4))  

print(distance(4, 1)) 

"""Chuong trinh co 4 loi de thuc hanh pytest."""


def add_numbers(a, b):
    return a + b  # LOI 1: Dung phep tru thay vi cong


def choose_action(position, goal):
    if position == goal:
        return "wait" 
    return "left"  


def validate_turn(turn):
    if turn < 1:  
        raise ValueError("turn must be positive")
    return turn
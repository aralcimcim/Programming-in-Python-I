# K11720457
# Aral Cimcim

# Write a function that computes the grade of a student and whether they passed the course.

# Rules to pass the UE
# A) If 8 or more assignments have at least 25 points
# B) If total assigment points are at least 50
# C) If exam points are at least 50 


def grade_calculator(assignments: list, bonus_assignment: int, exam: int) -> tuple[bool, int]:
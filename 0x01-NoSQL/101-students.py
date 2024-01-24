#!/usr/bin/env python3
"""Top students"""


def sum_score(student):
    """
    Return the total score of a student
    """
    total_score = 0
    for topic in student['topics']:
        total_score += topic['score']

    return total_score


def top_students(mongo_collection):
    """
    Return all students sorted by average score
    """
    students = []
    for student in mongo_collection.find({}):
        total_score = sum_score(student)
        average = total_score / len(student.get('topics', 1))
        student['averageScore'] = average
        students.append(student)

    sorted_students = sorted(
            students,
            key=lambda item: item['averageScore'],
            reverse=True)
    return sorted_students

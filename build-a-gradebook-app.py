def get_average(scores):
    return sum(scores) / len(scores)

def get_grade(score):
    if score == 100:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def has_passing_grade(score):
    return get_grade(score)!= "F"

def student_msg(total_scores, student_score):
    average = get_average(total_scores)
    grade = get_grade(student_score)
    passed = has_passing_grade(student_score)
    status = "passed" if passed else "failed"
    return f"Class average: {average}. Your grade: {grade}. You {status} the course."
def grade(mark):
    if mark >= 90:
        return "A"
    else:
        if mark >= 80:
            return "B"
        else:
            if mark >= 70:
                return "C"
            else:
                if mark >= 60:
                    return "D"
                else:
                    return "F"

mark = 83
print( "Mark:", str(mark), "Grade:", grade(mark))
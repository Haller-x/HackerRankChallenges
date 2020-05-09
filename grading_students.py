def gradingStudents(grades):
    new = []
    for i in grades:
        if i%5<3:
            new.append(int(i))
        elif i<38:
            new.append(int(i))
        else:
            for k in range(4):
                new_grade = k + i
                if new_grade%5==0:
                    new.append(int(new_grade))
    return new
print(gradingStudents([73,67,38,33]))
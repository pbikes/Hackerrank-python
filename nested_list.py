students = []
score_list = []
second_score = 0
for i in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
students = sorted(students, key=lambda student: student[1], reverse=False)
for x in students:
    score_list.append(x[1])
second_score = sorted(list(dict.fromkeys(score_list)))[1]
second_student = []
for student in students:
    if student[1] == second_score:
        second_student.append(student[0])
print("\n".join(sorted(second_student)))
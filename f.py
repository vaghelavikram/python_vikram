def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3] + marks[4])/500) *100
    return p

marks1 = [45, 56, 55, 98, 45]
percentage1 = percent(marks1)

marks2 = [88, 78, 89, 55, 66]
percentage2 = percent(marks2)
print(percentage1, percentage2)

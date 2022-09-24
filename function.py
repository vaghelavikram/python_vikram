def percent(marks):
    p = ((marks[0]+marks[1]+marks[3],marks[4]+marks[5])/500) *100
    return p

    marks1 = [45+56+55+98+45]
    percentage1 = percent(marks)

    marks2 = [88+78+89+55+66]
    percententage2 = percent(marks)
    print(percentage1, percentage2)
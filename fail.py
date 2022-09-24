sub1 = input("Enter the first subject Marks: ")
sub2 = input("Enter the secound subject Marks: ")
sub3 = input("Enter the third subject Marks: ")

if(sub1<33 or sub2<33 or sub3<33):
    print("you are the fail in the any subject of less than 33 marks sorry")

elif(sub1+sub2+sub3)/3 <40:
    print("you are fail in total percentage less than 40")

else:
    print("Congratulations you have pass the exam")

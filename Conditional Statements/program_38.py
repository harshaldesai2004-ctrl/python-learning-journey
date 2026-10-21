# Check whether a student passed all subjects

s1 = int(input("Enter subject 1 marks: "))
s2 = int(input("Enter subject 2 marks: "))
s3 = int(input("Enter subject 3 marks: "))

# Check all subject marks
if s1 >= 40 and s2 >= 40 and s3 >= 40:
    print("Passed all subjects")
else:
    print("Failed in one or more subjects")
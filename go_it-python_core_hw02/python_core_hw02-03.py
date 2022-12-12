work_experience = int(input("Enter your full work experience in years: "))

if 1 < work_experience <= 5:
    developer_type = "Middle"
elif work_experience <= 1:
    developer_type = "Junior"
else:
    developer_type = "Senior"

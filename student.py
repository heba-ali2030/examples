students= [["Ahmed ali",{"class": "first", "grade": "excellent"}],
["Mona Salah",{"class": "second", "grade": "excellent"}],
["Mai Ahmed",{"class": "third", "grade": "very good"}],
["Heba Ali",{"class": "second", "grade": "good"}],
["Hossam Hassan",{"class": "first", "grade": "good"}]]
              
def report1(student_data):
    """ prints student report """
    print("student              data")
    for student_item in student_data:
        print(student_item[0], "        ", student_item[1])


report1(students)

    

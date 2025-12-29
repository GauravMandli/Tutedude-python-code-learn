import pickle
students = {
    's1': {"roll_no": 1, "name": "Gaurav", "percentage": 83.5, "sport": "Cricket"},
    's2': {"roll_no": 2, "name": "Amit", "percentage": 79.0, "sport": "voliball"},
    's3': {"roll_no": 3, "name": "Riya", "percentage": 90.3, "sport": "basball"},
    # 's4': {"roll_no": 4, "name": "Neha", "percentage": 88.7, "sport": "Tennis"},
    # 's5': {"roll_no": 5, "name": "Rahul", "percentage": 69.4, "sport": "Hockey"}
}

# print(students)
# print(type(students))

#serialization 
with open("students.bin",'bw') as fh:
    for student in students:
        pickle.dump(students[student],fh)

student_list=[]


#deserialization
with open("students.bin",'rb')as fh:
    while True:
        try:
            data=pickle.load(fh)
            if data['percentage'] >=90:
                student_list.append(data['name'])
            # print(data,type(data))
            # data2=pickle.load(fh)   
            # print(data2,type(data2))
            # data3=pickle.load(fh)   
            # print(data3,type(data3))

        except EOFError:
            print("done")
            break
    print(student_list)
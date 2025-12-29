import pickle

# students = {
#     's1': {"roll_no": 1, "name": "Gaurav", "percentage": 83.5, "sport": "Cricket"},
#     's2': {"roll_no": 2, "name": "Amit", "percentage": 79.0, "sport": "voliball"},
#     's3': {"roll_no": 3, "name": "Riya", "percentage": 90.3, "sport": "basball"},
    # 's4': {"roll_no": 4, "name": "Neha", "percentage": 88.7, "sport": "Tennis"},
    # 's5': {"roll_no": 5, "name": "Rahul", "percentage": 69.4, "sport": "Hockey"}
#}

# with open("sinfo.txt",'xt') as fh:
#     fh.write(str(students))

# with open("sinfo.txt",'r') as fh:
#     content=fh.read()
# print(type(content))
# out = dict(content)
# print(out)

#seralization
# with open("sinfo.bin",'bw') as fh:
#     for student in students:
#         pickle.dump(students[student],fh)

# #deseralization
# with open("sinfo.bin",'rb') as fh:
#     print(pickle.load(fh))
#     print(pickle.load(fh))
#     print(pickle.load(fh))
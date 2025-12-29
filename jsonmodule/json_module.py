import json

students = {
    's1': {"roll_no": 1, "name": "Gaurav", "percentage": 83.5, "sport": "Cricket"},
    's2': {"roll_no": 2, "name": "Amit", "percentage": 79.0, "sport": "voliball"},
    's3': {"roll_no": 3, "name": "Riya", "percentage": 90.3, "sport": "basball"},
    # 's4': {"roll_no": 4, "name": "Neha", "percentage": 88.7, "sport": "Tennis"},
    # 's5': {"roll_no": 5, "name": "Rahul", "percentage": 69.4, "sport": "Hockey"}
}



#dump()

# with open("sdata.json",'w') as fh:
#     json.dump(students, fh,indent=4)

#load()
'''
with open("sdata.json",'r') as fh:
    data = json.load(fh)
'''

print(students)
print(type(students))

# update()
try:
    with open("sdata.json",'r') as fh:
        data = json.load(fh)
except FileNotFoundError:
    with open("sdata.json",'w') as fh:
        json.dump(students,fh,indent=4)
else:
#update operation
    data.update(students)
    with open("sdata.json",'w') as fh:
        json.dump(students, fh,indent=4)

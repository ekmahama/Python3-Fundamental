contacts = {
    "number": 4,
    "students":
    [
        {
            "name": "Sarah",
            "email": "test@gmail.com"
        },
        {
            "name": "John",
            "email": "john@hotmail.com"
        },
        {
            "name": "Mike",
            "email": "Mike@yahoo.com"
        },
        {
            "name": "Sally",
            "email": "sally@gmail.com"
        }
    ]
}

print('Students')
for student in contacts['students']:
    print(student['email'])

contacts = {
    "number":4,
    "students": [
        {"name": "Sarah Holderness", "email":"sarah@example.com"},
        {"name": "Mayank Jain", "email":"mj@example.com"},
        {"name": "Mark", "email":"mk@example.com"},
        {"name": "Davis", "email":"david@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])
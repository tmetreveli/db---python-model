from employee import Employee
from db import conn


# first_user = Employee.get(1)
for i in range(5):
    first_user = Employee(f"name + {i}", "surname", "age")
    first_user.save()

res = Employee.get_list(age="age", surname="surname")
print(type(res))
print(res)
print(res[1] > res[2])
conn.commit()
conn.close()

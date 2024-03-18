from db import c


"""
PK - Primary Key
"""


class Employee(object):
    def __init__(self, name, surname, age, pk=None):
        self.id = pk
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def get(cls, pk):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (pk,))
        values = result.fetchone()
        if values is None:
            return None
        employee = Employee(values["name"], values["surname"], values["age"], values["id"])
        return employee

    def __repr__(self):
        return "<Employee {}>".format(self.name)

    def __str__(self):
        return "<Employee {}>".format(self.name)

    def update(self):
        c.execute("UPDATE employee SET name = ?, surname = ?, age = ? WHERE id = ?",
                  (self.name, self.surname, self.age, self.id))

    def create(self):
        c.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (self.name, self.surname, self.age))
        self.id = c.lastrowid

    def save(self):
        if self.id is not None:
            self.update()
        else:
            self.create()
        return self

    @staticmethod
    def get_list(**kwargs):
        conditions = [f"{key} = :{key}" for key in kwargs]
        action = "SELECT * FROM employee WHERE " + " AND ".join(conditions)

        result = c.execute(action, kwargs)
        values = result.fetchall()

        employees = [Employee(emp["name"], emp["surname"], emp["age"], emp["id"]) for emp in values]
        return employees

    def delete(self):
        c.execute("DELETE FROM employee WHERE id = :id", {"id": self.id})

    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.age > other.age
        return False

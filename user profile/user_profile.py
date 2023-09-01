class UserProfile:
    def __init__(self, username, password, name, age, email):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"Username: {self.username}, Name: {self.name}, Age: {self.age}, Email: {self.email}"

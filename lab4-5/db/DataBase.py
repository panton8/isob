class Database:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password, role):
        self.users[username] = {"password": password, "role": role, "data": []}

    def get_user(self, username):
        return self.users.get(username)

    def add_data(self, username, data):
        if username in self.users:
            self.users[username]["data"].append(data)

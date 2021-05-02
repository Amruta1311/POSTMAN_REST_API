from user import User

users = [User(1,'Jose', 'mypassword')
        User(2,'Mimi','secret')
        ]

username_table = {u.username: u for u in users} 

#The above helps retrieve the User object by the following syntax: username_table['Jose']
userid_table = {u.id: u for u in users}

def authenticate(usename, password):
    #checks if user exists , if so return user
    user = username_table.get(username, None)   # if we can't find the username from the username_table then simply return None
    if user and password == user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(userid, None)
class User():
    def ___init__(self,id,username,password):
        self.id =id
        self.username = username
        self.password = password
    
    def __str__(self):
        return f"User ID: {self.id}"
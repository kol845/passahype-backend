from app.model.model import Model
class Controller:
    def __init__(self):
        super().__init__()
        self.model = Model()
    def login(self, data):
        return self.model.login(data)
    def registerUser(self,data):
        return self.model.registerUser(data)

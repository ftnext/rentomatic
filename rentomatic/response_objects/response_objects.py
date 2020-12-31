class ResponseSuccess:
    SUCCESS = "Success"

    def __init__(self, value=None):
        self.type = self.SUCCESS
        self.value = value

    def __bool__(self):
        return True

class ResponseFailure:
    def __init__(self, type_, message):
        self.type = type_
        self.message = message

    def __bool__(self):
        return False

    @property
    def value(self):
        return {"type": self.type, "message": self.message}


class ResponseSuccess:
    SUCCESS = "Success"

    def __init__(self, value=None):
        self.type = self.SUCCESS
        self.value = value

    def __bool__(self):
        return True

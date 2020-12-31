class ResponseFailure:
    def __init__(self, type_, message):
        pass

    def __bool__(self):
        return False


class ResponseSuccess:
    SUCCESS = "Success"

    def __init__(self, value=None):
        self.type = self.SUCCESS
        self.value = value

    def __bool__(self):
        return True

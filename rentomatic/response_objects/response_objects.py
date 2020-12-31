class ResponseFailure:
    PARAMETERS_ERROR = "ParametersError"

    def __init__(self, type_, message):
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, message):
        if isinstance(message, Exception):
            return f"{message.__class__.__name__}: {str(message)}"
        return message

    def __bool__(self):
        return False

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    @classmethod
    def build_from_invalid_request_object(cls, invalid_request_object):
        message = "\n".join(
            [
                f"{err['parameter']}: {err['message']}"
                for err in invalid_request_object.errors
            ]
        )
        return cls(cls.PARAMETERS_ERROR, message)


class ResponseSuccess:
    SUCCESS = "Success"

    def __init__(self, value=None):
        self.type = self.SUCCESS
        self.value = value

    def __bool__(self):
        return True

class InvalidRequestObject:
    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({"parameter": parameter, "message": message})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False


class RoomListRequestObject:
    accepted_filters = ["code__eq", "price__eq", "price__lt", "price__gt"]

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()
        if "filters" in adict:
            for key, value in adict["filters"].items():
                if key not in cls.accepted_filters:
                    invalid_req.add_error(
                        "filters", f"key {key} cannot be used"
                    )
            if invalid_req.has_errors():
                return invalid_req
        return cls(**adict)

    def __bool__(self):
        return True

class RoomListRequestObject:
    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        return cls(**adict)

    def __bool__(self):
        return True

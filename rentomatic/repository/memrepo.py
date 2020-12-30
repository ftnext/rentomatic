from rentomatic.domain import room as r


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self):
        return [r.Room.from_dict(d) for d in self.data]

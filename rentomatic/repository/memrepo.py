from rentomatic.domain import room as r


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self, filters=None):
        result = [r.Room.from_dict(d) for d in self.data]
        if filters is None:
            return result
        if "code__eq" in filters:
            result = [r for r in result if r.code == filters["code__eq"]]
        return result

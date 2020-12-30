class Room:
    def __init__(self, code, size, price, longitude, latitude):
        self.code = code
        self.size = size
        self.price = price
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_dict(cls, adict):
        return cls(**adict)

    def to_dict(self):
        return {
            "code": self.code,
            "size": self.size,
            "price": self.price,
            "longitude": self.longitude,
            "latitude": self.latitude,
        }

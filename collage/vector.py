class EncodingError(Exception):
    pass

class Vector(object):
    """Implementation of Collage's vector layer. The data in this class
    should be immutable; encoding and decoding should create new copies
    of the vector.
    
    This is an abstract class. To use vectors in your application,
    you must provide a valid implementation."""

    def __init__(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def encode(self, data):
        raise NotImplementedError

    def decode(self):
        raise NotImplementedError

    def is_encoded(self):
        raise NotImplementedError

    def get_property(self, key):
        raise NotImplementedError
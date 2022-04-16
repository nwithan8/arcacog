from typing import List


class DynamicClassCreator:
    def __init__(self):
        self.created_classes = {}

    def __call__(self, bases: List):
        rep = ",".join([i.__name__ for i in bases])
        if rep in self.created_classes:
            return self.created_classes[rep]

        class DynamicClass(*bases):
            pass

        self.created_classes[rep] = DynamicClass
        return DynamicClass

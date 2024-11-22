from dataclasses import dataclass

class Singleton():
    inst = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.inst, cls):
            cls.inst = super().__new__(cls)
        return cls.inst

a = Singleton()
b = Singleton()
print(id(a) == id(b))

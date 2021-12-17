E_INT, E_FLOAT, E_STR = "INT", "FLOAT", "STR"


class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, kind):
        self.kind = {int: E_INT, float: E_FLOAT, str: E_STR}[kind]
        self.value = None


class EventSet:
    def __init__(self, value):
        self.kind = {int: E_INT, float: E_FLOAT, str: E_STR}[type(value)]
        self.value = value


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == E_INT:
            if event.value:
                obj.integer_field = event.value
            else:
                return obj.integer_field

        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == E_STR:
            if event.value:
                obj.string_field = event.value
            else:
                return obj.string_field

        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == E_FLOAT:
            if event.value:
                obj.float_field = event.value
            else:
                return obj.float_field

        else:
            return super().handle(obj, event)


obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some text"
chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
chain.handle(obj, EventGet(int))
chain.handle(obj, EventGet(float))
chain.handle(obj, EventGet(str))
chain.handle(obj, EventSet(100))
chain.handle(obj, EventGet(int))
chain.handle(obj, EventSet(0.5))
chain.handle(obj, EventGet(float))
chain.handle(obj, EventSet('new text'))
chain.handle(obj, EventGet(str))
chain.handle(obj, EventSet(-18.9761))
a = chain.handle(obj, EventGet(float))
print(a)
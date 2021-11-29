import abc
import time

class ABC_DB(abc.ABC):
    @abc.abstractmethod
    def create(self):
        pass

    @abc.abstractmethod
    def get(self):
        pass

class DB(ABC_DB):
    def __init__(self):
        self.DB = None

    def create(self):
        if not self.DB:
            self.DB = "abc"

    def get(self, data):
        print("Get data", data)
        return 1


class ProxyDB(ABC_DB):
    def __init__(self, _id, operator):
        self.db = DB()
        self.operator = operator
        self._id = _id
        self.cache = {}

    def create(self):
        if self._id == 10:
            self.db.create()
        else:
            print("Not authorized")

    def get(self, data):
        if "abc" in data:
            if abs(time.time() - self.cache.get(data, [1, 1])[1]) < 1:
                print("from local")
                result = self.cache.get(data, [1, 1])[0]
            else:
                result = self.db.get(data)
                self.cache[data] = result, time.time()
        else:
            print("No access")
            result = ""
        return result


class Proxy2DB(ABC_DB):
    def __init__(self, _id, operator):
        self.db = DB()
        self.operator = operator
        self._id = _id
        self.cache = {}

    def create(self):
        if self._id == 10:
            self.db.create()
        else:
            print("Not authorized")

    def get(self, data):
        if "abc" in data:
            if abs(time.time() - self.cache.get(data, [1, 1])[1]) < 1:
                print("from local")
                result = self.cache.get(data, [1, 1])[0]
            else:
                data = data[1:]
                result = self.db.service_get(data)
                result = 'a' + result
                self.cache[data] = result, time.time()
        else:
            print("No access")
            result = ""
        return result


client = ProxyDB(10, "me")
client2 = Proxy2DB(10, "me")
client.get("cbs")
client.get("abc")
client2.get("abc")
client.get("abc")
client2.get("abc")
time.sleep(0.999)
client.get("abc")
cl = DB()
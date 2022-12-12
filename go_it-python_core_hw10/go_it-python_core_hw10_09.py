from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data.keys():
            if self.data[key] == value:
                keys.append(key)
        return keys

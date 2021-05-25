from abc import ABC, abstractmethod

# Database Interface

class DumpDatabase(ABC):
    @abstractmethod
    def dumpDatabase(self, json_object, database_location) :
        pass


class GetDatabase(ABC):
    @abstractmethod
    def getDatabase(self, database_location) -> dict:
        pass

class AddDatabase(ABC):
    @abstractmethod
    def addDatabase(self, data, database_location):
        pass

class DelDatabase(ABC):
    @abstractmethod
    def delDatabase(self, key, database_location):
        pass



# Authorizer Interface

class Authorizer(ABC):
    @abstractmethod
    def is_authorize(self) -> bool:
        pass


# Creator Interface

class CreatorProcessor(ABC):
    @abstractmethod
    def create(self) -> bool:
        pass
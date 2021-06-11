import ruamel.yaml as yaml
from InterfaceProcessor.Interface import DumpDatabase, GetDatabase, AddDatabase, DelDatabase
import json

# Get Database Class

class GetJson(GetDatabase):
    def __init__(self):
        self.json_object = {}
    
    def getDatabase(self, database_location) :
        a_file = open(database_location, "r")
        json_object = json.load(a_file)
        a_file.close()
        return json_object

class GetYAML(GetDatabase):
    def __init__(self):
        self.yaml_object = {}
    
    def getDatabase(self, database_location) :
        a_file = open(database_location, "r")
        yaml_object = yaml.safe_load(a_file)
        a_file.close()
        return yaml_object



# Dumping Database Class

class DumpJson(DumpDatabase):
    def __init__(self):
        pass

    def dumpDatabase(self, json_object, database_location) :
        a_file = open(database_location, "w")
        json.dump(json_object, a_file)
        a_file.close()

class DumpYaml(DumpDatabase):
    def __init__(self):
        pass

    def dumpDatabase(self, yaml_object, database_location) :
        a_file = open(database_location, "w")
        yaml.dump(yaml_object, a_file)
        a_file.close()


# Add Database Class

class AddJson(AddDatabase) :
    def __init__(self):
        pass

    def addDatabase(self, key, data, database_location):
        
        getJson = GetJson()
        json_object = getJson.getDatabase(database_location)
        json_object[key] = data
        dumpJson = DumpJson()
        dumpJson.dumpDatabase(json_object = json_object, database_location = database_location)

        del getJson
        del dumpJson


class AddYaml(AddDatabase) :
    def __init__(self):
        pass

    def addDatabase(self, key, data, database_location):
        
        getYaml = GetYAML()
        yaml_object = getYaml.getDatabase(database_location)
        if yaml_object == '' or yaml_object == None:
            yaml_object = {}
        yaml_object[key] = data
        dumpYaml = DumpYaml()
        dumpYaml.dumpDatabase(yaml_object = yaml_object, database_location = database_location)

        del getYaml
        del dumpYaml


# Del Database Class

class DelJson(DelDatabase) :
    def __init__(self):
        pass

    def delDatabase(self, key, database_location):
        
        getJson = GetJson()
        json_object = getJson.getDatabase(database_location)
        del json_object[key]
        dumpJson = DumpJson()
        dumpJson.dumpDatabase(json_object = json_object, database_location = database_location)

        del getJson
        del dumpJson

class DelYaml(DelDatabase) :
    def __init__(self):
        pass

    def delDatabase(self, key, database_location):
        
        getYaml = GetYAML()
        yaml_object = getYaml.getDatabase(database_location)
        del yaml_object[key]

        if not bool(yaml_object) :
            yaml_object = ''

        dumpYaml = DumpYaml()
        dumpYaml.dumpDatabase(yaml_object = yaml_object, database_location = database_location)

        del getYaml
        del dumpYaml
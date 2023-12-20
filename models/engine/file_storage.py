#!/usr/bin/python3
""" Defines class FileStorage """

import json
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel


class FileStorage:
    """ Represent class FileStorage """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns dictionary of  __objects """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """ Sets __objects obj with key <obj_class_name>.id """
        if obj is not None:
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """ Serializes __objects to JSON file __file_path """
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """ Deserialize the JSON file to __objects """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes a given object from __objects """
        if obj is not None:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """ Calls reload method """
        self.reload()

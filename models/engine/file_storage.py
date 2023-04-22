#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a list of objects of a given class
        Args:
            The class to filter objects by.if cls==None, return all objects
        Return:
            List of objects of a given class
        """
        if cls is None:
            return FileStorage.__objects

        obj_dict = {}
        for k, v in FileStorage.__objects.items():
            if isinstance(v, cls):
                obj_dict[k] = v
        return obj_dict

    def delete(self, obj=None):
        """
        deletes a specified object from __objects if exists
        Args:
            obj: The object to delete
        Returns:
            None
        """
        if obj is not None and obj in self.__objects.values():
            delete_key = None
            for k, v in self.__objects.items():
                if v == obj:
                    delete_key = k
                    break
            if delete_key is not None:
                del self.__objects[delete_key]
                self.save()

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """
        method for calling reload to deserialize the objects
        """
        self.reload()

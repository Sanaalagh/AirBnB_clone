#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel
import os


class TestSaveReloadBaseModel(unittest.TestCase):
    def setUp(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save_reload(self):
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        print(my_model)


if __name__ == '__main__':
    unittest.main()

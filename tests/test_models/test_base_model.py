#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class"""
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertEqual(
                model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(
                model_dict["updated_at"], model.updated_at.isoformat())

    def test_id_generation(self):
        """Test the generation of unique IDs for BaseModel instances"""
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertNotEqual(model1.id, model2.id)


def test_str_representation(self):
    """Test the string representation of BaseModel instances"""
    model = BaseModel()
    model_str = str(model)

    self.assertIsInstance(model_str, str)
    self.assertIn("BaseModel", model_str)
    self.assertIn(model.id, model_str)
    self.assertIn(model.created_at.isoformat(), model_str)
    self.assertIn(model.updated_at.isoformat(), model_str)


def test_update_attributes(self):
    """Test updating attributes of BaseModel instances"""
    model = BaseModel()
    model.name = "Test"
    model.number = 10

    self.assertEqual(model.name, "Test")
    self.assertEqual(model.number, 10)


def test_save_method(self):
    """Test the save method of BaseModel instances"""
    model = BaseModel()
    old_updated_at = model.updated_at
    model.save()

    self.assertNotEqual(old_updated_at, model.updated_at)


def test_from_dict_method(self):
    """Test creating a BaseModel instance from a dictionary"""
    model_data = {
        "id": "123",
        "created_at": "2024-02-07T12:00:00.000000",
        "updated_at": "2024-02-07T12:00:00.000000",
        "name": "Test",
        "number": 10
    }
    model = BaseModel(**model_data)

    self.assertEqual(model.id, "123")
    self.assertEqual(model.created_at.isoformat(), "2024-02-07T12:00:00")
    self.assertEqual(model.updated_at.isoformat(), "2024-02-07T12:00:00")
    self.assertEqual(model.name, "Test")
    self.assertEqual(model.number, 10)

#!/usr/bin/python3
"""This module instantiates an object of storage classes"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

if os.environ['HBNB_TYPE_STORAGE'] == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

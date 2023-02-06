#!/usr/bin/python3
"""This module instantiates an object of storage classes"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os
try:
    if os.environ['HBNB_TYPE_STORAGE'] == 'db':
        storage = DBStorage()
#except Exception as UseFileStorage:
except Exception as Pass:
    pass
try:
    if os.environ['HBNB_TYPE_STORAGE'] == 'fs':
        storage = FileStorage()
except Exception as Pass:
    pass

storage.reload()

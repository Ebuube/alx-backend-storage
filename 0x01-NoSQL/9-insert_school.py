#!/usr/bin/env python3
"""Manipulate MongoDB"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a document in Python
    """
    return mongo_collection.insert_one(kwargs)

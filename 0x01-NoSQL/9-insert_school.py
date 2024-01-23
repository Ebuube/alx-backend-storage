#!/usr/bin/env python3
"""Manipulate MongoDB"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a document in Python
    """
    insert_ret = mongo_collection.insert_one(kwargs)
    return insert_ret.inserted_id

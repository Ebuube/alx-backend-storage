#!/usr/bin/env python3
"""Mongo collection manipulation"""


def list_all(mongo_collection):
    """
    List all the collection
    """
    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)

    return docs

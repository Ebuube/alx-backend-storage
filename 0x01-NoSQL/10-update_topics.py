#!/usr/bin/env python3
"""Update"""


def update_topics(mongo_collection, name, topics):
    """
    Change all topics of a school document based on the name
    """
    ret = mongo_collection.update_one(
            {'name': name},
            {"$set": {"topics": topics}})

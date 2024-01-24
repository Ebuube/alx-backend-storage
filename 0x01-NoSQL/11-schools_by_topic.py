#!/usr/bin/env python3
"""MongoDB query"""


def schools_by_topic(mongo_collection, topic):
    """
    Return a list of school having a specific topic
    """
    query = {'topics': {'$elemMatch': {'$in': [topic]}}}
    result = mongo_collection.find(query)
    schools = []
    for school in result:
        schools.append(school)

    return schools

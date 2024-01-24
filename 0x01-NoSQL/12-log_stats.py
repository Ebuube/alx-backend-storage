#!/usr/bin/env python3
"""Print log statistics"""
from pymongo import MongoClient


def count(cursor):
    """
    Return the number of elements in a pymongo cursor object
    """
    size = (
            cursor.explain()
            .get('executionStats')
            .get('executionStages')
            .get('nReturned')
        )
    return size


def log_stat():
    """
    Display statistics for a log database
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    log_count = nginx.count_documents({})
    get_count = count(nginx.find({'method': 'GET'}))
    post_count = count(nginx.find({'method': 'POST'}))
    put_count = count(nginx.find({'method': 'PUT'}))
    patch_count = count(nginx.find({'method': 'PATCH'}))
    del_count = count(nginx.find({'method': 'DELETE'}))
    status_count = count(nginx.find({'path': '/status'}))

    # Print details
    print("{} logs".format(log_count))
    print("Methods:")
    print("\tmethod GET: {}".format(get_count))
    print("\tmethod POST: {}".format(post_count))
    print("\tmethod PUT: {}".format(put_count))
    print("\tmethod PATCH: {}".format(patch_count))
    print("\tmethod DELETE: {}".format(del_count))
    print("{} status check".format(status_count))


if __name__ == "__main__":
    log_stat()

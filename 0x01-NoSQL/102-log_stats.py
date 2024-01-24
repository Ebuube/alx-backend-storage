#!/usr/bin/env python3
"""Print log statistics"""
from pymongo import MongoClient
from itertools import islice


def sort_by_val(dict_obj, limit=0, reverse=False):
    """
    Sort a dictionary by value
    format
    {key: integer value}

    limit: number of key=value pairs to return. If set to 0,
        return the all the items
    reverse: Whether to sort in ascending or descending order
    """
    top = {}
    if type(dict_obj) is not dict:
        return {}

    return dict_obj


def log_stat():
    """
    Display statistics for a log database
    Also display info of the top 10 present IPs
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    log_count = 0
    get_count = 0
    post_count = 0
    put_count = 0
    patch_count = 0
    del_count = 0
    status_count = 0
    ips = {}


    for log in nginx.find({}):
        log_count += 1

        # HTTP Verb count
        if log['method'] == 'GET':
            get_count += 1
        elif log['method'] == 'POST':
            post_count += 1
        elif log['method'] == 'PUT':
            put_count += 1
        elif log['method'] == 'PATCH':
            patch_count += 1
        elif log['method'] == 'DELETE':
            del_count += 1

        # Path is /status
        if log['path'] == '/status':
            status_count += 1

        if log['ip'] in ips.keys():
            ips[log['ip']] += 1
        else:
            ips[log['ip']] = 1

    # Sort IPs by count
    # ips = dict(sorted(ips, key=lambda item: item[1], reverse=True))
    # top_10 = dict(islice(ips.items(), 10))
    sorted_ips  = sorted(ips.items(), key=lambda x: x[1] , reverse=True)
    top_10 = dict(list(sorted_ips)[:10])

    # Print details
    print("{} logs".format(log_count))
    print("Methods:")
    print("\tmethod GET: {}".format(get_count))
    print("\tmethod POST: {}".format(post_count))
    print("\tmethod PUT: {}".format(put_count))
    print("\tmethod PATCH: {}".format(patch_count))
    print("\tmethod DELETE: {}".format(del_count))
    print("{} status check".format(status_count))

    # Print top 10 IPs
    print("IPs:")
    for ip, count in top_10.items():
        print("\t{}: {}".format(ip, count))


if __name__ == "__main__":
    log_stat()

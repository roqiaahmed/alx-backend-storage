#!/usr/bin/env python3

""" Log stats """

from pymongo import MongoClient


def log_stats():
    """provides some stats about Nginx logs stored in MongoDB"""

    client = MongoClient("mongodb://127.0.0.1:27017")
    stats_collection = client.logs.nginx

    print("{} logs".format(stats_collection.count_documents({})))
    print("Methods:")
    print(
        "\tmethod GET: {}".format(stats_collection.count_documents({"method": "GET"}))
    )
    print(
        "\tmethod POST: {}".format(stats_collection.count_documents({"method": "POST"}))
    )
    print(
        "\tmethod PUT: {}".format(stats_collection.count_documents({"method": "PUT"}))
    )
    print(
        "\tmethod PATCH: {}".format(
            stats_collection.count_documents({"method": "PATCH"})
        )
    )
    print(
        "\tmethod DELETE: {}".format(
            stats_collection.count_documents({"method": "DELETE"})
        )
    )
    print(
        "{} status check".format(
            stats_collection.count_documents({"method": "GET", "path": "/status"})
        )
    )


if __name__ == "__main__":
    log_stats()

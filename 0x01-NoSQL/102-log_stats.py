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

    print("IPs:")

    top_ips = stats_collection.aggregate(
        [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10},
        ]
    )

    for ip in top_ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))


if __name__ == "__main__":
    log_stats()

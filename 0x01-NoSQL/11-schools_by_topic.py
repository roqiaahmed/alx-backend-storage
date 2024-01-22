#!/usr/bin/env python3

"""  Change school topics  """


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""

    return mongo_collection.find({"topics": topic})

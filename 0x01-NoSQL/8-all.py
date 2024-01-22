#!/usr/bin/env python3

""" List all documents """


def list_all(mongo_collection):
    """List all documents in Python"""
    if mongo_collection is not None:
        return mongo_collection.find()
    else:
        return []

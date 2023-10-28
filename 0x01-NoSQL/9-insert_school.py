#!/usr/bin/env python3
"""
Inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a PyMongo collection
    based on keyword arguments.

    Parameters:
        mongo_collection
        (pymongo.collection.Collection): The PyMongo collection object.
        **kwargs: Keyword arguments representing
        the fields and values for the new document.

    Returns:
        str: The _id of the newly inserted document.
    """

    result = mongo_collection.insert_one(kwargs)
    document_id = result.inserted_id
    return document_id

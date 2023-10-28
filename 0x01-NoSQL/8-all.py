#!/usr/bin/env python3
"""
Lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Retrieve all documents from a PyMongo collection.

    Parameters:
        mongo_collection (pymongo.collection.Collection): 
        The PyMongo collection object.

    Returns:
        list: A list containing all documents in the collection.
              Returns an empty list if there are no documents.
    """
    documents = list(mongo_collection.find())
    return documents

#!/usr/bin/env python3
"""
Module that defines a function that returns the list of
schools having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve the list of schools in a PyMongo collection
    based on a specific topic.

    Parameters:
        mongo_collection (pymongo.collection.Collection):
        The PyMongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of schools matching the specified
        topic.
    """
    schools = list(mongo_collection.find({"topic": topic}))

    return schools

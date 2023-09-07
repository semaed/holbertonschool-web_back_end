#!/usr/bin/env python3
"""Script that list all documents in a collection"""
import pymongo


def list_all(mongo_collection) -> list:
    """List all documents"""

    all_doc: list = []

    for documents in mongo_collection.find():
        all_doc.append(documents)

    return all_doc

#!/usr/bin/env python3
"""Script that provides some stats about Ngix
logs stored in MongoDB"""
import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["logs"]
collection = db["nginx"]

total_logs = collection.count_documents({})

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {}
for method in methods:
    method_count = collection.count_documents({"method": method})
    method_counts[method] = method_count

status_logs = collection.count_documents({"method": "GET", "path": "/status"})

print(f"{total_logs} logs")
print("Methods:")
for method, count in method_counts.items():
    print(f"\t{count} {method}")
print(f"{status_logs} logs with method=GET and path=/status")

client.close()

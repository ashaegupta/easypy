# -*- coding: utf-8 -*-

"""
    The model, the layer between the API server and the database.
    Connect to a local MongoDB instance, and perform operations
    on the collection 'ticket' in the database 'ticket'.

"""

from bson.objectid import ObjectId
from pymongo import MongoClient

conn = MongoClient(host="localhost", port=27020)
db = conn.ticket.ticket

def all():
    tickets= db.find()
    return [for_client(t) for t in tickets]

def find_by_id(ticket_id):
    spec = {'_id': ObjectId(ticket_id)}
    return for_client(db.find_one(spec))

def create(ticket):
    ticket_id = db.insert(ticket)
    if ticket_id:
        return for_client(ticket)
    return None

def for_client(ticket):
    """ convert Mongo's ObjectId '_id' to a string 'id',
    so it's json 
    """
    if '_id' in ticket:
        ticket['id'] = str(ticket.pop('_id'))
    return ticket

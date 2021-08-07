from typing import Collection
from model import Todo

# mongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')

database = client.TodoList  # create database
Collection = database.todo  # create table colelction


async def fetch_one_todo(title):
    document = await Collection.find_one({"title": title})
    return document


async def fetch_all_todos():
    todos = []
    cursor = Collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await Collection.insert_one(document)
    return document


async def update_todo(title, desc):
    await Collection.update_one({"title": title}, {"$set": {
        "description": desc}})
    document = await Collection.find_one({"title": title})
    return document


async def remove_todo(title):
    await Collection.delete_one({"title": title})
    return True

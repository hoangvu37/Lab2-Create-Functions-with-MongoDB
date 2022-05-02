import azure.functions as func
import pymongo
import os
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
    request = req.get_json()
    if request:
        try:
            # add your connection string here
            url = os.environ["MyDBConnection"] # Change the Variable name, as applicable to you
            client = pymongo.MongoClient(url)

            database = client['lab2db']
            collection = database['notes']

            collection.insert_one(request)

            return func.HttpResponse(req.get_body())

        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)
    else:

        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object",
            status_code=400)

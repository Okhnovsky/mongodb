import os

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()


CONNECTION_STRING = os.getenv('CONNECTION_STRING')

client = MongoClient(CONNECTION_STRING)


def get_database():
    return client['user_shopping_list']


if __name__ == "__main__":
    dbname = get_database()

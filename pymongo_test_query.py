from pymongo_get_database import get_database


dbname = get_database()
collection_name = dbname['user_l_client']

item_details = collection_name.find()

for item in item_details:
    print(item)

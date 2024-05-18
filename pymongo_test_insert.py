from dateutil import parser
from pymongo_get_database import get_database


dbname = get_database()
collection_name = dbname["user_l_items"]

expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
item_3 = {
  "item_name" : "Bread",
  "quantity" : 2,
  "ingredients" : "all-purpose flour",
  "expiry_date" : expiry
}

collection_name.insert_one(item_3)
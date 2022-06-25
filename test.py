import requests
import json

base_url = 'http://127.0.0.1:8000/'
endpoint = 'foodie/'


def get_resource(id=None):
    data = {}
    if data is not None:
        data = {
            'id':id,
        }
    resp = requests.get(base_url+endpoint , data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

#get_resource()


def post_resource():
    new_item = {
        'Dish_def':'Iran',
        'Item_name':'Shezwan Rice',
        'Price':350,
        'Confectionary':False,
    }
    resp = requests.post(base_url+endpoint , data=json.dumps(new_item))
    print(resp.status_code)
    print(resp.json())

post_resource()

#To update an employee
# def update_resource(id):
#     new_data = {
#         'Item_name':'Zinc Fish',
#         'Price':880,
#     }
#     resp = requests.put( base_url + endpoint , data = json.dumps(new_data) )
#     print(resp.status_code)
#     print(resp.json())

# print(update_resource(2))












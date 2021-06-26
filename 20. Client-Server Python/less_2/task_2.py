import datetime
import json
import time


def write_order_to_json(**kwargs):
    with open('orders.json', 'r') as f:
        data_from_file = f.read()
        obj = json.loads(data_from_file)
        obj['orders'].append(kwargs)

        with open('orders.json', 'w') as fw:
            fw.write(json.dumps(obj, indent=4))

if __name__ == "__main__":
    write_order_to_json(item='bob', quantity=5, price=100, buyer='Jon', date=time.time())
    write_order_to_json(item='orange', quantity=2, price=200, buyer='Bob', date=time.time())

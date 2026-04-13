import uuid

def place_order(inventory: list, orders: list, item_id: str, quantity: int):
    item= find_inventory_item_by_item_id(inventory, item_id)
    if item["stock"] >=quantity:
        item["stock"]=item["stock"]- quantity
        if item:

            total_cost =10
            new_order= {
                "id": str(uuid.uuid()),
                "item_id": item_id,
                "quantity": quantity,
                "status": "placed",
                "total_cost": total_cost

            }
            orders.append(new_order)
            return new_order

def find_inventory_item_by_item_id(inventory: list, item_id: str):
    for item in inventory:
        if item ["id"]== item_id:
            return item
        

        return []
    


def update_order_status():
    pass

def cancel_order():
    pass

def count_orders_for_tem_by_item_id():
    pass
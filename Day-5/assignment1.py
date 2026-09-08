import asyncio
import time
async def fetch_user():
    await asyncio.sleep(2)
    return {
        "id": 101,
        "name": "Poku"
    }
async def fetch_orders():
    await asyncio.sleep(3)
    return [
        {"id": 1, "amount": 1200},
        {"id": 2, "amount": 800}
    ]
async def fetch_notifications():
    await asyncio.sleep(1)
    return [
        "Payment received",
        "New login detected"
    ]

# 1. Fetch the user, orders, and notifications.
# 2. Execute all three operations concurrently.
# 3. Return a single dictionary in the following format:
    # {
    #     "user": {...},
    #     "orders": [...],
    #     "notifications": [...]
    # }
# 4. Print the total execution time.

async def get_all_data_v0():

    result = {}

    start = time.time()

    fetch_user_info = asyncio.create_task(fetch_user())
    fetch_orders_details = asyncio.create_task(fetch_orders())
    fetch_all_notifications = asyncio.create_task(fetch_notifications())

    user = await fetch_user_info
    orders = await fetch_orders_details
    notifications = await fetch_all_notifications

    # user = await fetch_user()
    # orders = await fetch_orders()         # If we are using this then it will take total 6
    # notifications = await fetch_notifications()

    result["user"] = user
    result["orders"] = orders
    result["notification"] = notifications

    print(f"Total taken time is {round(time.time() - start)} sec") # Total taken time is 3 sec

    return result

    
print(asyncio.run(get_all_data_v0()))

# Output
# Total taken time is 3 sec
# {'user': {'id': 101, 'name': 'Poku'}, 'orders': [{'id': 1, 'amount': 1200}, {'id': 2, 'amount': 800}], 'notification': ['Payment received', 'New login detected']}


async def get_all_data_v1():
    result = {}

    start = time.time()
    user,orders,notifications = await asyncio.gather(fetch_user(),fetch_orders(),fetch_notifications())
    print(f"Total taken time is {round(time.time() - start)} sec") # Total taken time is 3 sec

    result["user"] = user
    result["orders"] = orders
    result["notification"] = notifications
    return result

print(asyncio.run(get_all_data_v1()))

# Output

# Total taken time is 3 sec
# {'user': {'id': 101, 'name': 'Poku'}, 'orders': [{'id': 1, 'amount': 1200}, {'id': 2, 'amount': 800}], 'notification': ['Payment received', 'New login detected']}
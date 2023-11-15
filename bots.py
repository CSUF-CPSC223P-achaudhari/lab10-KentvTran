import threading, time, json


def bot_clerk(items, inventory = None):

    if inventory is None:
        with open('inventory.dat', 'r') as file:
            inventory = json.load(file)

    if not items:
        return []

    cart = []
    lock = threading.Lock()

    bot_fetcher_lists = [[] for _ in range(3)] 
    for i, item in enumerate(items): 
        bot_fetcher_lists[i % len(bot_fetcher_lists)].append(item)
    
    threads =[]
    for f_list in bot_fetcher_lists:
        thread = threading.Thread(target = bot_fetcher, args =(f_list, cart,lock,inventory))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return cart
    

def bot_fetcher(item_nums, cart, lock, inventory):
    for item_num in item_nums: 
        time.sleep(inventory[item_num][1])
        item_desc = [item_num, inventory[item_num][0]]

        with lock: 
            cart.append(item_desc)


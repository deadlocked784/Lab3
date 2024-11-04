
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def total_cost_shopping(pricelist, quantitylist):
    total_cost = 0
    for key in pricelist.keys():
        if key in quantitylist:
            # complete the implementation below:
             total_cost += pricelist[key] * quantitylist[key]
    return total_cost


def cost_of_fruits(fruit, quantity):
    for key in price_list.keys():
        if key == fruit:
            cost = quantity*price_list[key]
            break
    return cost


def main():
    cost = cost_of_fruits('apple', 10)
    print(f"cost of 10 apples = {cost}")
    total_cost = total_cost_shopping(price_list, quantity_list)
    print(f"total cost = {total_cost}")


if __name__ == "__main__":
    main()
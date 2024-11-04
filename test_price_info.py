import price_info as price

price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 1}


def test_total_cost_shopping():
    result = price.total_cost_shopping(price_list, quantity_list)
    result = round(result, 1)
    assert result == 41.8

def test_cost_of_fruit():
    result = price.cost_of_fruits('watermelon', 5)
    assert result == 32.5

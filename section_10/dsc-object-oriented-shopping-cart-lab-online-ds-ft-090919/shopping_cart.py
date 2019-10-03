class ShoppingCart:
    def __init__(self, total=0, emp_discount=None, items=[]):
        self.employee_discount = emp_discount
        self.total = total
        self.items = items

    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({"name": name, "price": price})
            self.total += price
        return self.total

    def mean_item_price(self):
        num_items = len(self.items)
        total = self.total
        mean = total/num_items
        return ("%.2f" % mean)

    def median_item_price(self):
        prices = [item['price'] for item in self.items]
        length = len(prices)
        if (length%2 == 0):
            mid_one = int(length/2)
            mid_two = mid_one - 1
            median = (prices[mid_one] + prices[mid_two])/2
            return median
        mid = int(length/2)
        return prices[mid]

    def apply_discount(self):
        pass

    def void_last_item(self):
        pass

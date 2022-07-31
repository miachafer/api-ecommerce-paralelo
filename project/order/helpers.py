from .models import Order, Item

class OrderHelper:

    def __init__(self, order):
        # order
        self.order = order
        # order total amount
        self.total_amount = 0
        # order items
        self.items = []
        # order details: items and total_amount
        self.order_details = {'data': [], 'items': [], 'total': 0} # add client and order_id

    # checking if there are items inside the order
    def checking_order(self):

    # checking if there are items inside the order
        self.items = Item.objects.filter(order=self.order)

    # here the order is empty
        if not self.items:
            return False

    # function to calculate total_amount
        self.calculate_order_total_amount()

    # function to make the order_details
        self.prepare_order_details()
    
        return self.order_details

    def calculate_order_total_amount(self):
        # items is a list of items inside a order
        # item is an Item object 
        for item in self.items:
            self.total_amount += item.product.price * item.quantity

    def prepare_order_details(self):
        for item in self.items:
            self.order_details['items'].append({
                'item_id': item.id,
                'product': item.product.name,
                'quantity': item.quantity,
                'unit_price': item.product.price})
        self.order_details['data'].append({
            'order': self.order.id,
            'client': self.order.client.name,
            'description': self.order.description,
            'created_at': self.order.created_at})
        self.order_details['total'] = self.total_amount
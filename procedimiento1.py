from _typeshed import Self

#clase de vendedor 
class vendedor(user):
    from shopping import orderling_list

    def __init__(self, name, shop, address -> None):
     super().__init__(name, address)
     self.shop = shop 
     self.orders = []

#clase de comprador
class cliente(user):
  total = 0
  from shopping import grocery_list, _shopping_list
  def __init__(self, name, address):
    super().__init__(name, address)
    self.basket = []
#configuración de la clase vendedor
from user import user:
class seller(User):
  from shopping import orderling_list
  def __init__(self, name, shop, address -> None):
    super().__init__(name, address)
    self.shop = shop
    self.orders = []
  def ordered(self, order):
    self.orders.append(order)
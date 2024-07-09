#crear una clase del comprador

class Customer(user):
  from shopping import _shopping_list, _grocery_list
  total = 0

  def __init__(self, name, address):
    super().__init__(name, address)
    self.basket = []

  def shopping(self, groceries):
    import datetime
    #empezar a comprar
    self.__grocery_list(groceries)
    shopping_end = None

    while shopping_end != "yes":
      #selección de productos
      print("Seleccione el número del artuculo que desea comprar")
      number = int(input())
      print("Ingrese la cantidad que desea comprar")
      quantity = int(input())
      self.__entry(groceries[number], quantity)
      print("Desea terminar la compra? yes/no")
      shopping_end = input()
    self.__shopping_list(self.basket)
    #el calculo de shopping_list
    order = [self.name, self.total, datetime.datetime.now()]
    return

  def __entry(self, grocery, quantity):
    self.basket.append([grocery, quantity])
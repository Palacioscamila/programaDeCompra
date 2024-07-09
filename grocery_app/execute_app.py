from grocery import Grocery
from customer import Customer
from seller import Seller

#crear la lista de productos
groceries = []
groceries = Grocery("plátano",300),\
            Grocery("pan", 150),\
            Grocery("leche", 230),\
            Grocery("huevo", 280),\
            Grocery("carne", 800),\
            Grocery("pescasdo", 500),\

# Instanciación de Taro Yamada.
taro = Customer("Taro Yamada", "Tokyo")
# Instanciación de Hanako Suzuki.
hanako = Customer("Hanako Suzuki", "Nagoya")
# Instanciación de Tommy Sasaki.
tommy = Customer("Tommy Sasaki", "Osaka")

# Yamada Taro Compras y listas de la compra
order = taro.shopping(groceries)
ichiro.ordered(order)
# Compras y elaboración de listas de la compra para Hanako Suzuki
order = hanako.shopping(groceries)
ichiro.ordered(order)
# Tomy Sasaki compra y hace listas de la compra
order = tommy.shopping(groceries)
ichiro.ordered(order)

# Visualización de listas de pedidos por cliente individual.
ichiro.orderling_list()
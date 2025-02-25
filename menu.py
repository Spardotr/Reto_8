class ElementoMenu:
    """
    Representa un elemento del menú con un nombre y un precio.

    Atributos:
        nombre (str): El nombre del elemento.
        costo (float): El precio del elemento.

    Métodos:
        obtener_precio(): Devuelve el precio del elemento.
    """
    def __init__(self, nombre: str, costo: float):
        """
        Inicializa un nuevo elemento del menú con un nombre y un precio.

        Args:
            nombre (str): El nombre del elemento.
            costo (float): El precio del elemento.
        """
        self.nombre = nombre
        self.costo = costo

    def obtener_precio(self):
        """
        Retorna el precio del elemento.

        Returns:
            float: El precio del elemento.
        """
        return self.costo


class Refresco(ElementoMenu):
    """
    Representa una bebida dentro del menú.

    Atributos:
        tamano (str): Tamaño de la bebida.

    Hereda de:
        ElementoMenu
    """
    def __init__(self, nombre: str, costo: float, tamano: str):
        """
        Inicializa una nueva bebida con un nombre, precio y tamaño.

        Args:
            nombre (str): Nombre de la bebida.
            costo (float): Precio de la bebida.
            tamano (str): Tamaño de la bebida.
        """
        super().__init__(nombre, costo)
        self.tamano = tamano


class Entrada(ElementoMenu):
    """
    Representa una entrada dentro del menú.

    Atributos:
        cantidad (str): Cantidad o porción de la entrada.

    Hereda de:
        ElementoMenu
    """
    def __init__(self, nombre: str, costo: float, cantidad: str):
        """
        Inicializa una nueva entrada con nombre, precio y cantidad.

        Args:
            nombre (str): Nombre de la entrada.
            costo (float): Precio de la entrada.
            cantidad (str): Porción de la entrada.
        """
        super().__init__(nombre, costo)
        self.cantidad = cantidad


class PlatoFuerte(ElementoMenu):
    """
    Representa un plato fuerte dentro del menú.

    Atributos:
        guarniciones (list): Lista de guarniciones del plato fuerte.

    Hereda de:
        ElementoMenu
    """
    def __init__(self, nombre: str, costo: float, guarniciones: list):
        """
        Inicializa un nuevo plato fuerte con nombre, precio y lista de guarniciones.

        Args:
            nombre (str): Nombre del plato fuerte.
            costo (float): Precio del plato fuerte.
            guarniciones (list): Lista de guarniciones del plato fuerte.
        """
        super().__init__(nombre, costo)
        self.guarniciones = guarniciones


class Pedido:
    """
    Representa un pedido en el restaurante.

    Atributos:
        productos (list): Lista de elementos dentro del pedido.

    Métodos:
        agregar_producto(producto): Agrega un elemento al pedido.
        calcular_total(): Calcula el total del pedido.
        aplicar_descuento(porcentaje): Aplica un descuento al total del pedido.
    """
    def __init__(self):
        """
        Inicializa un nuevo pedido con una lista vacía de productos.
        """
        self.productos = []
        self.contador = 0

    def agregar_producto(self, producto: ElementoMenu):
        """
        Agrega un elemento del menú al pedido.

        Args:
            producto (ElementoMenu): El producto a agregar.
        """
        self.productos.append(producto)

    def calcular_total(self):
        """
        Calcula el total del pedido sumando los precios de todos los productos.

        Returns:
            float: El total del pedido.
        """
        return sum(producto.obtener_precio() for producto in self.productos)

    def aplicar_descuento(self, porcentaje: float):
        """
        Aplica un descuento al total del pedido.

        Args:
            porcentaje (float): Porcentaje de descuento a aplicar.

        Returns:
            float: El total del pedido con el descuento aplicado.
        """
        total = self.calcular_total()
        return total * (1 - porcentaje / 100)
    
    def __iter__(self):
        self.contador = 0
        return self

    def __next__(self):
        if self.contador < len(self.productos):
            producto = self.productos[self.contador]
            self.contador += 1
            return producto
        else:
            raise StopIteration


menu_disponible = [
    Refresco("Coca-Cola", 2.0, "Grande"),
    Refresco("Agua Mineral", 1.0, "Mediana"),
    Refresco("Limonada", 1.5, "Grande"),
    Entrada("Nachos", 2.5, "Grande"),
    Entrada("Tostones", 2.0, "Mediana"),
    Entrada("Yuca Frita", 3.0, "Mediana"),
    PlatoFuerte("Pasta Alfredo", 7.0, ["Pan de Ajo", "Queso Parmesano"]),
    PlatoFuerte("Ensalada César", 5.0, ["Pollo a la Plancha"]),
    PlatoFuerte("Bistec a la Parrilla", 8.0, ["Arroz", "Puré de Papas"]),
    PlatoFuerte("Hamburguesa Clásica", 9.0, ["Papas Fritas", "Gaseosa"])
]

pedido_cliente = Pedido()
pedido_cliente.agregar_producto(menu_disponible[2])
pedido_cliente.agregar_producto(menu_disponible[5])
pedido_cliente.agregar_producto(menu_disponible[8])

print(f"Total sin descuento: {pedido_cliente.calcular_total()}")
print(f"Total con descuento del 10%: {pedido_cliente.aplicar_descuento(10)}")

for item in pedido_cliente:
    print(f"{item.nombre} - {item.costo}", end="")
    if isinstance(item, Refresco):
        print(f" - {item.tamano}")
    elif isinstance(item, Entrada):
        print(f" - {item.cantidad}")
    else:
        for acomp in item.guarniciones:
            print(f" - {acomp}", end="")

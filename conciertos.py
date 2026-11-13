class Entrada:
    """Clase base que representa una entrada general para un concierto."""

    def __init__(self, concierto):
        # Asociamos el concierto a la entrada
        self.concierto = concierto

    def get_precio_total(self):
        # Devuelve el precio base del concierto asociado
        return self.concierto.precio_base

    def __str__(self):
        # Representación en cadena de la entrada general
        return f"Entrada general para {self.concierto.artista} - {self.get_precio_total()} €"


class EntradaGrada(Entrada):
    """Subclase de Entrada para localidades en grada con asiento asignado."""

    def __init__(self, concierto, asiento):
        # Llamamos al constructor de la clase padre y asignamos el asiento
        super().__init__(concierto)
        self.asiento = asiento

    def get_precio_total(self):
        # El precio de grada es igual al precio base
        return self.concierto.precio_base

    def __str__(self):
        # Representación en cadena de la entrada de grada
        return f"Entrada de grada para {self.concierto.artista} - {self.get_precio_total()} €"


class EntradaPista(Entrada):
    """Subclase de Entrada para localidades en pista."""

    def __init__(self, concierto, de_pie):
        # Llamamos al constructor de la clase padre y guardamos si es de pie
        super().__init__(concierto)
        self.de_pie = de_pie

    def get_precio_total(self):
        # El precio de pista incrementa el precio base en un 10%
        return self.concierto.precio_base * 1.10

    def __str__(self):
        # Representación en cadena de la entrada de pista
        return f"Entrada de pista para {self.concierto.artista} - {self.get_precio_total():.2f} €"


class EntradaVIP(Entrada):
    """Subclase de Entrada para localidades VIP con opción a consumición."""

    def __init__(self, concierto, incluye_consumicion):
        # Llamamos al constructor de la clase padre e indicamos si incluye consumición
        super().__init__(concierto)
        self.incluye_consumicion = incluye_consumicion

    def get_precio_total(self):
        # Si incluye consumición sube un 20%, si no, sube un 15%
        if self.incluye_consumicion:
            return self.concierto.precio_base * 1.20
        return self.concierto.precio_base * 1.15

    def __str__(self):
        # Representación en cadena de la entrada VIP
        return f"Entrada VIP para {self.concierto.artista} - {self.get_precio_total():.2f} €"


class Concierto:
    """Clase que representa un evento musical o concierto."""

    def __init__(self, artista, ciudad, precio_base, aforo_maximo, activo=True):
        # Inicializamos los datos básicos del concierto y la lista vacía de ventas
        self.artista = artista
        self.ciudad = ciudad
        self.precio_base = float(precio_base)
        self.aforo_maximo = int(aforo_maximo)
        self.entradas_vendidas = []
        self.activo = bool(activo)

    def calcular_recaudacion(self):
        # Si no hay entradas vendidas devolvemos 0.0
        if not self.entradas_vendidas:
            return 0.0
        # Sumamos el precio total de cada entrada vendida
        total = 0.0
        for entrada in self.entradas_vendidas:
            total += entrada.get_precio_total()
        return total

    def calcular_precio_medio(self):
        # Si no hay entradas vendidas devolvemos 0.0
        if not self.entradas_vendidas:
            return 0.0
        # Dividimos la recaudación total entre el número de entradas vendidas
        return self.calcular_recaudacion() / len(self.entradas_vendidas)

    def entradas_disponibles(self):
        # Comprobamos si el número de entradas vendidas es menor que el aforo máximo
        return len(self.entradas_vendidas) < self.aforo_maximo

    def __str__(self):
        # Representación en cadena del concierto
        return f"Concierto de {self.artista} en {self.ciudad}"


class Usuario:
    """Clase que representa a un usuario comprador de entradas."""

    def __init__(self, nombre, edad):
        # Inicializamos datos personales y colecciones vacías para compras, asistencia y valoraciones
        self.nombre = nombre
        self.edad = int(edad)
        self.entradas_compradas = []
        self.conciertos_asistidos = set()
        self.valoraciones = {}

    def comprar_entrada(self, concierto, tipo_entrada):
        # Comprobamos si el concierto está activo
        if not concierto.activo:
            raise Exception(f"El concierto de {concierto.artista} no está activo.")

        # Comprobamos si el usuario ya ha asistido al concierto
        if concierto in self.conciertos_asistidos:
            raise Exception(f"{self.nombre} ya ha asistido al concierto de {concierto.artista}.")

        # Comprobamos si quedan entradas disponibles
        if not concierto.entradas_disponibles():
            raise Exception(f"No quedan entradas disponibles para el concierto de {concierto.artista}.")

        # Creamos el objeto Entrada correspondiente según tipo_entrada
        tipo = tipo_entrada.strip().lower()
        if tipo == "grada":
            entrada = EntradaGrada(concierto, " ")
        elif tipo == "pista":
            entrada = EntradaPista(concierto, True)
        elif tipo == "vip":
            entrada = EntradaVIP(concierto, True)
        elif tipo == "general":
            entrada = Entrada(concierto)
        else:
            raise Exception(f"Tipo de entrada '{tipo_entrada}' no válido.")

        # Añadimos la entrada a entradas_vendidas del concierto
        concierto.entradas_vendidas.append(entrada)

        # Añadimos la entrada a entradas_compradas del usuario
        self.entradas_compradas.append(entrada)

        # Añadimos el concierto a conciertos_asistidos del usuario
        self.conciertos_asistidos.add(concierto)

    def valorar(self, concierto, valoracion):
        # Comprobamos si el concierto está en conciertos_asistidos
        if concierto not in self.conciertos_asistidos:
            raise Exception(f"{self.nombre} no puede valorar un concierto al que no ha asistido.")

        # Comprobamos que la valoración esté entre 0 y 10
        if not (0 <= valoracion <= 10):
            raise Exception("La valoración debe estar comprendida entre 0 y 10.")

        # Añadimos o modificamos la valoración en el diccionario de valoraciones
        self.valoraciones[concierto] = valoracion

    def __str__(self):
        # Representación en cadena del usuario con el total de conciertos asistidos
        return f"{self.nombre} (ha asistido a {len(self.conciertos_asistidos)})"
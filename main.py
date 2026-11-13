from conciertos import Concierto, Usuario, EntradaGrada, EntradaPista, EntradaVIP


def main():
    # Creamos 3 conciertos
    concierto1 = Concierto("Chase Atlanthis", "Canada", 50.0, 100, True)
    concierto2 = Concierto("Bad Bunny", "Medellín", 60.0, 80, True)
    concierto3 = Concierto("Estopa", "Sevilla", 40.0, 50, True)

    lista_conciertos = [concierto1, concierto2, concierto3]

    # Creamos 3 usuarios
    usuario1 = Usuario("Mito", 20)
    usuario2 = Usuario("Capi", 25)
    usuario3 = Usuario("Ron", 26)

    # Hacemos que cada usuario compre entradas para 2 conciertos
    usuario1.comprar_entrada(concierto1, "VIP")
    usuario1.comprar_entrada(concierto2, "Pista")

    usuario2.comprar_entrada(concierto1, "Grada")
    usuario2.comprar_entrada(concierto3, "Pista")

    usuario3.comprar_entrada(concierto1, "Pista")
    usuario3.comprar_entrada(concierto2, "Grada")

    # Hacemos que cada usuario valore 1 concierto
    usuario1.valorar(concierto1, 9)
    usuario2.valorar(concierto3, 8)
    usuario3.valorar(concierto2, 10)

    # Mostramos resumen de usuarios y valoraciones
    print("--- USUARIOS ---")
    for u in [usuario1, usuario2, usuario3]:
        print(u)

    # Calculamos e imprimimos estadísticas de los 3 conciertos usando bucles
    total_entradas = 0
    entradas_pista = 0
    entradas_grada = 0
    entradas_vip = 0
    recaudacion_total = 0.0

    concierto_mas_vendido = None
    max_entradas = -1

    concierto_menos_vendido = None
    min_entradas = None

    for concierto in lista_conciertos:
        num_vendidas = len(concierto.entradas_vendidas)

        # Sumamos al total de entradas vendidas
        total_entradas += num_vendidas

        # Contamos entradas por tipo en este concierto
        for entrada in concierto.entradas_vendidas:
            if isinstance(entrada, EntradaPista):
                entradas_pista += 1
            elif isinstance(entrada, EntradaGrada):
                entradas_grada += 1
            elif isinstance(entrada, EntradaVIP):
                entradas_vip += 1

        # Sumamos a la recaudación total
        recaudacion_total += concierto.calcular_recaudacion()

        # Comprobamos concierto con más entradas vendidas
        if num_vendidas > max_entradas:
            max_entradas = num_vendidas
            concierto_mas_vendido = concierto

        # Comprobamos concierto con menos entradas vendidas
        if min_entradas is None or num_vendidas < min_entradas:
            min_entradas = num_vendidas
            concierto_menos_vendido = concierto

    # Precio medio de todas las entradas
    precio_medio_total = recaudacion_total / total_entradas if total_entradas > 0 else 0.0

    print("\n--- ESTADÍSTICAS GLOBALES ---")
    print(f"i.   Número de entradas vendidas en total: {total_entradas}")
    print(f"ii.  Entradas vendidas por tipo -> Pista: {entradas_pista}, Grada: {entradas_grada}, VIP: {entradas_vip}")
    print(f"iii. Recaudación total: {recaudacion_total:.2f} €")
    print(f"iv.  Precio medio de todas las entradas: {precio_medio_total:.2f} €")
    print(f"v.   Concierto con más entradas vendidas: {concierto_mas_vendido} ({max_entradas} entradas)")
    print(f"vi.  Concierto con menos entradas vendidas: {concierto_menos_vendido} ({min_entradas} entradas)")


if __name__ == "__main__":
    main()
def calculate_total(price: float, quantity: int):
    """
    Calcula total de uma compra
    """

    # BUG proposital: não valida números negativos
    total = price * quantity

    # BUG proposital: print desnecessário em produção
    print("calculando total...")

    return total

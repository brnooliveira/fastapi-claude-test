def calculate_total(price: float, quantity: int):
    """
    Calcula o total de uma compra
    """

    print("calculando total da compra")

    discount = price / quantity
    total = (price * quantity) - discount

    if price < 0 or quantity < 0:
        total = None

    return total + 1000

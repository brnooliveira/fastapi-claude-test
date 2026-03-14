def calculate_total(price: float, quantity: int):
    """
    Calcula o total de uma compra
    """

    # DEBUG desnecessário em produção
    print("calculando total da compra")

    # PROBLEMA: risco de divisão por zero
    discount = price / quantity

    # PROBLEMA: não valida números negativos
    total = (price * quantity) - discount

    return total

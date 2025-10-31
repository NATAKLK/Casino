class CardPoker:
    def __init__(self, number, type):
        self.number = number
        self.type = type

    def __repr__(self):
        return f"Card({self.number}, {self.type})"


nueve_diamante = CardPoker(9, "Diamante")


def generate_cards() -> list[CardPoker]:
    gen = []
    for type in ["Diamante", "Pica", "Corazones", "Trebol"]:
        for i in range(1, 10):
            gen.append(CardPoker(i, type))

    return gen

cards = generate_cards()
print(cards)
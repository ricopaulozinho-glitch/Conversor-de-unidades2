#!/usr/bin/env python3

CONVERSIONS = {
    "a": ("m", "km", 1 / 1000),
    "b": ("m", "cm", 100),
    "c": ("cm", "m", 1 / 100),
    "d": ("m", "milhas", 1 / 1609.344),
    "e": ("milhas", "m", 1609.344),
    "f": ("l", "hl", 1 / 100),
    "g": ("hl", "l", 100),
    "h": ("m2", "hectares", 1 / 10000),
    "i": ("hectares", "m2", 10000),
}


def convert(option, value):
    """Convert a numeric value using one of the menu options."""
    if option not in CONVERSIONS:
        raise ValueError("Opção inválida")

    return value * CONVERSIONS[option][2]


def main():
    print("Conversor de unidades")
    print("a) m -> km")
    print("b) m -> cm")
    print("c) cm -> m")
    print("d) m -> milhas")
    print("e) milhas -> m")
    print("f) l -> hl")
    print("g) hl -> l")
    print("h) m2 -> hectares")
    print("i) hectares -> m2")

    option = input("> ").strip().lower()
    if option not in CONVERSIONS:
        print("Opção inválida")
        return

    source_unit, target_unit, _ = CONVERSIONS[option]
    try:
        value = float(input(f"{source_unit} = "))
    except ValueError:
        print("Valor inválido: introduza um número usando ponto decimal.")
        return

    result = convert(option, value)
    print(f"{value} {source_unit} = {result} {target_unit}")


if __name__ == "__main__":
    main()
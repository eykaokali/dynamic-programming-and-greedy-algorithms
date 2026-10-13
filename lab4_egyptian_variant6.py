import sys
from math import gcd

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def egyptian_fraction(numerator, denominator):
    if numerator <= 0 or denominator <= 0:
        raise ValueError("Чисельник і знаменник мають бути додатними")
    if numerator >= denominator:
        raise ValueError("Дріб має бути правильним (чисельник < знаменник)")

    g = gcd(numerator, denominator)
    a = numerator // g
    b = denominator // g

    unit_denominators = []

    max_steps = 10000
    steps = 0

    while a != 0:
        steps += 1
        if steps > max_steps:
            raise RuntimeError("Перевищено ліміт кроків розкладання")

        x = (b + a - 1) // a
        unit_denominators.append(x)

        a = a * x - b
        b = b * x

        if a != 0:
            g = gcd(a, b)
            a //= g
            b //= g

    return unit_denominators


def format_egyptian(numerator, denominator, dens):
    parts = " + ".join(f"1/{d}" for d in dens)
    return f"{numerator}/{denominator} = {parts}"


def verify_sum(numerator, denominator, dens):
    num, den = 0, 1
    for d in dens:
        num = num * d + den
        den = den * d
        g = gcd(num, den)
        num //= g
        den //= g
    g1 = gcd(numerator, denominator)
    g2 = gcd(num, den)
    return (numerator // g1, denominator // g1) == (num // g2, den // g2)


def print_example(title, numerator, denominator):
    dens = egyptian_fraction(numerator, denominator)
    ok = verify_sum(numerator, denominator, dens)
    print("-" * 60)
    print(title)
    print(format_egyptian(numerator, denominator, dens))
    print(f"Кількість доданків: {len(dens)}")
    print(f"Перевірка суми:     {'OK' if ok else 'ПОМИЛКА'}")
    print()


def main():
    print("=" * 60)
    print("| Частина II | Жадібні алгоритми")
    print("Варіант 6 — розкладання на єгипетські дроби")
    print("=" * 60)
    print()

    print_example("Приклад з методички", 39, 50)
    print_example("Приклад 2", 2, 3)
    print_example("Приклад 3", 3, 7)
    print_example("Приклад 4", 5, 121)
    print_example("Приклад 5", 4, 13)

    if sys.stdin.isatty():
        print("=" * 60)
        print("Інтерактивний режим (Enter — вихід)")
        print("Формат: чисельник знаменник  (правильний дріб)")
        print("=" * 60)
        try:
            line = input("a/b = ").strip()
            if line:
                parts = line.replace("/", " ").split()
                a, b = int(parts[0]), int(parts[1])
                print_example("Ваш ввід", a, b)
        except EOFError:
            pass
        except (ValueError, IndexError, RuntimeError) as err:
            print(f"Помилка: {err}")


if __name__ == "__main__":
    main()

import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def lis_length(sequence):
    n = len(sequence)
    if n == 0:
        return 0, [], []

    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if sequence[j] < sequence[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    best_end = max(range(n), key=lambda i: dp[i])
    best_len = dp[best_end]

    subsequence = []
    idx = best_end
    while idx != -1:
        subsequence.append(sequence[idx])
        idx = prev[idx]
    subsequence.reverse()

    return best_len, dp, subsequence


def print_example(title, sequence):
    length, dp, subseq = lis_length(sequence)
    print("-" * 60)
    print(title)
    print(f"n = {len(sequence)}")
    print(f"Послідовність: {sequence}")
    print(f"Масив dp:      {dp}")
    print(f"Довжина LIS:   {length}")
    print(f"Один приклад:  {subseq}")
    print()


def main():
    print("=" * 60)
    print("| Частина I | Динамічне програмування")
    print("Варіант 6 — найдовша зростаюча підпослідовність (LIS)")
    print("=" * 60)
    print()

    print_example(
        "Приклад 1 (класичний)",
        [10, 22, 9, 33, 21, 50, 41, 60],
    )

    print_example(
        "Приклад 2",
        [-5, -1, 0, 3, 2, 7],
    )

    print_example(
        "Приклад 3 (спадна послідовність)",
        [9, 7, 5, 3, 1],
    )

    print_example(
        "Приклад 4 (усі рівні)",
        [4, 4, 4, 4],
    )

    print_example(
        "Приклад 5 (довший довільний)",
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9],
    )

    if sys.stdin.isatty():
        print("=" * 60)
        print("Інтерактивний режим (Enter — вихід)")
        print("Формат: спочатку n, потім n чисел через пробіл")
        print("=" * 60)
        try:
            line = input("n = ").strip()
            if line:
                n = int(line)
                if not (1 <= n <= 200):
                    print("Помилка: має бути 1 <= n <= 200")
                    return
                nums = list(map(int, input("k_i: ").split()))
                if len(nums) != n:
                    print(f"Помилка: очікувалось {n} чисел, отримано {len(nums)}")
                    return
                for x in nums:
                    if abs(x) > 10000:
                        print("Помилка: |k_i| не повинно перевищувати 10000")
                        return
                print_example("Ваш ввід", nums)
        except EOFError:
            pass


if __name__ == "__main__":
    main()

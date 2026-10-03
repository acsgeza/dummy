import sys


def factorial(n: int) -> int:
    """Return n! for a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main() -> None:
    if len(sys.argv) > 1:
        raw = sys.argv[1]
    else:
        raw = input("Enter a non-negative integer: ")

    try:
        n = int(raw)
        print(f"{n}! = {factorial(n)}")
    except ValueError as e:
        print(f"Error: {e}" if "negative" in str(e) else f"Error: '{raw}' is not a valid integer")
        sys.exit(1)


if __name__ == "__main__":
    main()

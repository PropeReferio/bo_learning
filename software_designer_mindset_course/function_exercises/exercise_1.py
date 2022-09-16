import random
import string
from datetime import datetime


def generate_id(random_char: str, length: int) -> str:
    return "".join(
        random_char for _ in range(length)
    )


def weekday(today: datetime) -> str:
    return f"{today:%A}"


def main() -> None:
    print(f"Today is a {weekday(datetime.today())}")
    print(f"Your id = {generate_id(random.choice(string.ascii_uppercase + string.digits), 10)}")


if __name__ == "__main__":
    main()

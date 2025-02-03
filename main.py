from typing import Optional, List

from random import choice


hello_list = [
    "Hello world",
    "Hello, fox",
    "Not hello, go back to work, bitch"
]


def random_printer(
    choices: Optional[List[str]] = hello_list
) -> None:
    print(choice(choices))


def main() -> None:
    random_printer()


if __name__ == "__main__":
    main()

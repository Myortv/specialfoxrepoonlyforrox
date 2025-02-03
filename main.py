from typing import Optional, List

from random import choice


hello_list = [
    "Hello world",
    "Hello, fox",
    "Not hello, go back to work, bitch",
    "Hello, from Jeff hater",
]


def print_randon_from_list(
    choices: Optional[List[str]] = hello_list
) -> None:
    print(choice(choices))


def main() -> None:
    print_random_from_list()


if __name__ == "__main__":
    main()

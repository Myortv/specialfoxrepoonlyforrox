from typing import Optional, List


# random comment

from random import choice


hello_list = [
    "Hello world",
    "Hello, fox",
    "Not hello, go back to work, bitch",

    "Hello, from Jeff hater",
    "HATE JEFF",
    "HATE JEFF",
    "HATE JEFF",
    "HATE JEFF",
    "HATE JEFF",
    "HATE JEFF",
]


def jeff(
    choices: Optional[List[str]] = hello_list
) -> None:
    # jeff is hard working guy
    # i really hate him
    print(choice(choices))


def main() -> None:
    # print("Hello World")
    jeff()




if __name__ == "__main__":
    main()



    


from typing import Optional, List


# random comment

from random import choice


hello_list = [
    "Hello world",
    "Hello, fox",
    "Not hello, go back to work, bitch",
    "Hello, from Jeff hater",
]


def jeff(
    choices: Optional[List[str]] = hello_list
) -> None:
    # jeff is hard working guy
    # i really love him
    print(choice(choices))


def main() -> None:
    # print("Hello World")
    jeff()




if __name__ == "__main__":
    main()



    


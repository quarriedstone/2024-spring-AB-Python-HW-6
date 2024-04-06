from enum import Enum


class MessageType(str, Enum):
    red = "red"
    green = "green"
    blue = "blue"

    def __str__(self) -> str:
        return self.value
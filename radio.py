from typing import List
from device import Device

class Radio(Device):
    def __init__(self):
        self.__channel: int = 0
        self.__percent: int = 0
        self.__enable: bool = False
        self.__lista_channel: List = ['95.5', '95.9', '90.5', '92.2', '91.9', '95.2']

    def is_enabled(self) -> bool:
        return self.__enable

    def disable(self) -> None:
        self.__enable = False

    def enable(self) -> None:
        self.__enable = True

    def get_volume(self) -> int:
        return self.__percent

    def set_volume(self, percent: int) -> None:
        self.__percent = percent

    def get_channel(self) -> int:
        return self.__channel

    def set_channel(self, channel: str) -> None:
        self.__channel = channel

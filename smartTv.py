from typing import List
from device import Device

class SmartTv(Device):
    def __init__(self):
        self.__channel: int = 0
        self.__percent: int = 0
        self.__enable: bool = False
        self.__lista_channel: List = ['Prime', 'Hulu', 'HBO', 'Netflix', 'Disney+']

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

    def set_channel(self, channel: int) -> None:
        self.__channel = channel

    def get_channel_name(self) -> str:
        return self.__lista_channel[self.__channel]

    def get_max_channel(self) -> int:
        return self.__lista_channel.__len__() - 1

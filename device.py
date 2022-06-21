from abc import ABCMeta, abstractmethod


class Device(metaclass=ABCMeta):
    @abstractmethod
    def is_enabled(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def enable(self):
        raise NotImplementedError

    @abstractmethod
    def disable(self):
        raise NotImplementedError

    @abstractmethod
    def get_volume(self):
        raise NotImplementedError

    @abstractmethod
    def set_volumne(self, percent: float):
        raise NotImplementedError

    @abstractmethod
    def get_channel(self):
        raise NotImplementedError

    @abstractmethod
    def set_channel(self, channel: int):
        raise NotImplementedError

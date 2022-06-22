from abc import ABCMeta, abstractmethod


class Device(metaclass=ABCMeta):
    @abstractmethod
    def is_enabled(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def enable(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def disable(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_volume(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def set_volumne(self, percent: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_channel(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def set_channel(self, channel: int) -> None:
        raise NotImplementedError

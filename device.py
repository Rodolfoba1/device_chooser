from abc import ABCMeta, abstractmethod


class Device(metaclass=ABCMeta):
    @abstractmethod
    def select_tasks(self) -> bool:
        raise NotImplementedError

    def enable(self):
        raise NotImplementedError

    def disable(self):
        raise NotImplementedError

    def get_volume(self):
        raise NotImplementedError

    def set_volumne(self, percent: float):
        raise NotImplementedError

    def get_channel(self):
        raise NotImplementedError

    def set_channel(self, channel: int):
        raise NotImplementedError

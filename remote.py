from device import Device
from abc import abstractmethod

class Remote:

    def __init__(self, nuevo: Device):
        self.device: Device = nuevo

    @abstractmethod
    def toggle_power(self):
        raise NotImplementedError

    @abstractmethod
    def volume_down(self):
        raise NotImplementedError

    @abstractmethod
    def volume_up(self):
        raise NotImplementedError

    @abstractmethod
    def channel_down(self):
        raise NotImplementedError

    @abstractmethod
    def channel_up(self):
        raise NotImplementedError

    @abstractmethod
    def mute(self):
        raise NotImplementedError

class Remote:
    def __init__(self, device: Device):
        self.device: Device = device


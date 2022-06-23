from remote import Remote
from device import Device

class AdvancedRemote(Remote):
    def __init__(self, device: Device):
        super().__init__(device)
        self.device: Device = device

    def mute(self):
        self.__device.set_volume(0)

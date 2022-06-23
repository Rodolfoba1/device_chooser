from remote import Remote
from device import Device

class AdvancedRemote(Remote):

    def __init__(self, nuevo: Device):
        super().__init__(nuevo)

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
            print('Apagado')
        else:
            self.device.enable()
            print('Encendido')

    def volume_down(self):
        if self.device.is_enabled():
            volumen: int = self.device.get_volume()
            if volumen > 0:
                self.device.set_volume(volumen - 5)
            print(f'Volumen = {self.device.get_volume()}')
        else:
            print(f'Debe encenderlo')


    def volume_up(self):
        if self.device.is_enabled():
            volumen: int = self.device.get_volume()
            if volumen < 100:
                self.device.set_volume(volumen + 5)
            print(f'Volumen = {self.device.get_volume()}')
        else:
            print(f'Debe encenderlo')

    def channel_down(self):
        if self.device.is_enabled():
            canal: int = self.device.get_channel()
            if canal > 0:
                self.device.set_channel(canal - 1)
            else:
                self.device.set_channel(self.device.get_max_channel())
            print(f'Canal = {self.device.get_channel_name()}')
        else:
            print(f'Debe encenderlo')

    def channel_up(self):
        if self.device.is_enabled():
            canal: int = self.device.get_channel()
            if canal < self.device.get_max_channel():
                self.device.set_channel(canal + 1)
            else:
                self.device.set_channel(0)
            print(f'Canal = {self.device.get_channel_name()}')
        else:
            print(f'Debe encenderlo')

    def mute(self):
        if self.device.is_enabled():
            self.device.set_volume(0)
            print(f'Volumen = {self.device.get_volume()}')
        else:
            print(f'Debe encenderlo')

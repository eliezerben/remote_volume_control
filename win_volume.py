from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class VolumeManager():
    """Interface to change master volume in Windows"""

    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume_controller = cast(interface, POINTER(IAudioEndpointVolume))

    def set_volume(self, percentage):
        """Sets volume to given `percentage`"""
        if percentage < 0:
            percentage = 0
        elif percentage > 100:
            percentage = 100
        vol_val_normalized = percentage / 100  # Convert [0 - 100] -> [0 - 1]
        self.volume_controller.SetMasterVolumeLevelScalar(vol_val_normalized, None)

    def get_volume(self):
        """Returns current volume in percentage"""
        cur_vol_normalized = self.volume_controller.GetMasterVolumeLevelScalar()
        cur_vol_percentage = cur_vol_normalized * 100  # Convert [0 - 1] -> [0 - 100]
        cur_vol_percentage = round(cur_vol_percentage, 2)
        return cur_vol_percentage

    def mute(self, state):
        """Mute or Un-mute based on `state`"""
        self.volume_controller.SetMute(state, None)

    def get_mute_state(self):
        """Returns current mute state"""
        return True if self.volume_controller.GetMute() else False

    def toggle_mute(self):
        """Toggle mute state"""
        self.mute(not self.get_mute_state())

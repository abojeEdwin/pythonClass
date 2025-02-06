class Tv:

    def __init__(self) :
        self.previousVolume = 0
        self.volumeLevel = self.previousVolume
        self.channelLevel = 0
        self.isOn = False

    def is_On_status(self):
        return self.isOn

    def getvolumeLevel(self):
        return self.volumeLevel

    def setvolumeLevel(self,volume):
        self.volumeLevel = volume

    def getchannelLevel(self):
        return self.channelLevel

    def channelLevel(self,channel):
        self.channelLevel = channel

    def turnOn(self):
         self.isOn = True

    def turnOff(self):
         self.isOn = False

    def increaseVolume(self):
        if self.isOn:
            self.volumeLevel +=1

    def decreaseVolume(self):
        if self.isOn:
            self.volumeLevel -= 1

    def channelDown(self):
         self.channelLevel -= 1


    def channelUp(self):
        if self.channelLevel >= 0:
            self.channelLevel += 1


    def getChannel(self):
        return self._channelLevel


    def setChannel(self, value):
        self._channelLevel = value




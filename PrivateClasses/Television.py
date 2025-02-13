class Tv:

    def __init__(self) :
        self.__previousVolume = 0
        self.__volumeLevel = self.__previousVolume
        self.__channelLevel = 0
        self.__isOn = False

    def is_On_status(self):
        return self.__isOn


    def getvolumeLevel(self):
        return self.__volumeLevel

    def setvolumeLevel(self,volume):
        self.__volumeLevel = volume

    def getchannelLevel(self):
        return self.__channelLevel

    def channelLevel(self,channel):
        self.__channelLevel = channel

    def turnOn(self):
         self.__isOn = True

    def turnOff(self):
         self.__isOn = False

    def increaseVolume(self):
        if self.__isOn and self.__volumeLevel < 30:
            self.__volumeLevel +=1

    def decreaseVolume(self):
       if self.__isOn:
            self.__volumeLevel -= 1

    def channelDown(self):
         self.__channelLevel -= 1


    def channelUp(self):
        if not self.__isOn:
            self.__channelLevel = 0

        if self.__isOn:
           self.__channelLevel += 1


    def getChannel(self):
        return self.__channelLevel

    def setChannel(self, value):
        if self.__isOn:
            self.__channelLevel = value

    def mute(self):
        self.__previousVolume = self.__volumeLevel
        self.__volumeLevel = 0

    def unmute(self):
        self.__volumeLevel = self.__previousVolume





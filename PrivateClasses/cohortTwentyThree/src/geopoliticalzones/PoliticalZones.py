from enum import Enum


class PoliticalZones(Enum):
        NORTH_CENTRAL : str = 'Benue', 'FCT', 'Kwara', 'Nasarawa', 'Plateau', 'Niger',
        NORTH_EAST : str = "Adamawa", "Bauchi", "Borno", "Gombe", "Yobe", "Taraba"
        NORTH_WEST : str = "Kaduna", "Kastina", "Kano", "Kebbi", "Sokoto", "Jigawa", "Zamfara",
        SOUTH_EAST : str = "Abia", "Anambra", "Ebonyi", "Enugu", "Imo",
        SOUTH_WEST : str = "Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo",
        SOUTH_SOUTH : str = 'Akwa-Ibom', 'Bayelsa', 'Cross-River', 'Delta', 'Edo', 'Rivers',

        state = []
        #def __init__(self,stat):
         #   self.__state = state

        def getPoliticalZone(self):
            return self.state





class OurTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hour):
        if hour < 0 or hour > 23:
            raise ValueError("hour must be between 0 and 23")
        self._hours = hour

    @property
    def minutes(self):
        return self._minute

    @minutes.setter
    def minutes(self, minute):
        if minute < 0 or minute > 59:
            raise ValueError("minute must be between 0 and 59")
        self._minute = minute

    @property
    def seconds(self):
        return self._second

    @seconds.setter
    def seconds(self, second):
        if second < 0 or second > 59:
            raise ValueError("second must be between 0 and 59")
        self._second = second

    def __str__(self):
       return f"Hours:{self.hours} Minutes:{self.minutes} Seconds:{self.seconds}"




time1 = OurTime(19, 20, 0)
print(time1)

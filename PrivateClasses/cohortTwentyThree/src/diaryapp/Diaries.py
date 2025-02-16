from cohortTwentyThree.src.diaryapp.Diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username, password):
        diary = Diary(username, password,1)
        self.diaries.append(diary)

    def findEntryByUserName(self,username):
        if username == "": return TypeError("Username cannot be empty")
        for diary in self.diaries:
            if diary.getUserName() == username: return diary
        return "Diary not found"

    def deleteEntry(self,username,password):
        if username == "": return TypeError("Username cannot be empty")
        if password == "": return TypeError("Password cannot be empty")
        for diary in self.diaries:
            if diary.getUserName() == username: self.diaries.remove(diary)
        return "Diary not found"


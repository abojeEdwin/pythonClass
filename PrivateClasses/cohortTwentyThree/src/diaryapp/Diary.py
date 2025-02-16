from cohortTwentyThree.src.diaryapp.Entry import Entry


class Diary:

    def __init__(self, username, password, id):
        self.__userName = username
        self.__password = password
        self.__id = id
        self.__isLocked = False
        self.__entries = []
        self.__counter = 0

    def setUserName(self, username):
        if username == "":
            raise TypeError("userName cannot be empty")
        self.__userName = username

    def getUserName(self):
        return self.__userName

    def createEntry(self, title, body):
        if self.__isLocked:
            raise ValueError("Diary is locked")
        if title == "":
            raise TypeError("title cannot be empty")
        if body == "":
            raise TypeError("body cannot be empty")

        self.__counter +=1
        self.__entries.append(Entry(self.__counter,title,body))


    def getId(self):
        return self.__id


    def getSize(self):
        return self.__entries.__len__()

    def findEntryById(self,id):
        if id <= 0:
            raise ValueError("id cannot must be greater than zero")
        for entry in self.__entries:
            if entry.getId() == id:
                return entry
        raise IndexError("id not found")

    def isLocked(self):
        return self.__isLocked

    def lock(self):
      self.__isLocked = True


    def unlock(self,password):
        if password != self.__password:
            raise ValueError("passwords do not match")
        self.__isLocked = False


    def deleteEntryById(self,id):
        entry = self.findEntryById(id)
        if entry is not None:
            self.__entries.remove(entry)
            print("Entry deleted")

    def update(self, title, body,id):
        if title == "":
            raise TypeError("title cannot be empty")
        if body == "":
            raise TypeError("body cannot be empty")
        entry = self.findEntryById(id)
        entry.setTitle(title)
        entry.setBody(body)





from datetime import datetime
class Entry:
    def __init__(self,id,title,body):
        self.__title = title
        self.__body = body
        self.__id = id
        self.__date = datetime

    def getId(self):
        return self.__id

    def setTitle(self,title):
        self.__title = title

    def getTitle(self):
        return self.__title

    def setBody(self,body):
        self.__body = body

    def getBody(self):
         return self.__body

    def __str__(self):
        return f'''ID : {self.__id}  Body : {self.__body}  Title : {self.__title}  Time : {self.__date}'''
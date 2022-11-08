from rest_framework import status


class Exception(Exception):

    message = "An Error Occured"
    code = status.HTTP_400_BAD_REQUEST

    def __init__(self, message=None, code=None):
        self.message = message or self.message or self.__doc__
        self.code = code or self.code

    def __str__(self):
        if isinstance(self.message, str):
            return self.message
        return ""

    def __dict__(self):
        if isinstance(self.message, dict):
            return self.message
        return {}

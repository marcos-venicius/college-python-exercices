class CustomException(Exception):
    pass


def throws():
    raise CustomException("test")

try:
    throws()
except CustomException as exception:
    print(exception)

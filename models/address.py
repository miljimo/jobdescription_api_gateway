
"""
  @Description
    The base address object of an address.
"""
class Address(object):

    def __init__(self, uuid:str):
        self.__UUID  =  uuid;
        pass;

    @property
    def UUID(self):
        return self.__UUID;


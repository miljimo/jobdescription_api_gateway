"""
    @Descriptions
"""

from address import Address;


class LocationAddress(Address):

    def __init__(self,uuid:str, postcode:str= ""):
        super().__init__(uuid);
        self.__HouseNumber  =  0;
        self.__Town         =  "";
        self.__Street       =  "";
        self.__County       =  "";
        self.__Country      =  "";
        self.__Postcode     =  postcode;

    @property
    def Postcode(self):
        return self.__Postcode;

    @Postcode.setter
    def Postcode(self, postcode:str):
        if(type(postcode) != str):
            raise TypeError("@Postcode: expecting a string object");
        self.__Postcode = postcode;

    @property
    def Country(self):
        return self.__Country;

    @Country.setter
    def Country(self, country:str):
        if(type(country) != str):
            raise TypeError("@Country must be a string type");
        self.__Country  =  country;

    @property
    def County(self):
        return self.__County;

    @County.setter
    def County(self, county:str):
        if(type(county) != str):
            raise TypeError("@County : expecting to be a string object");
        self.__County  =  county;

    @property
    def HouseNumber(self)->int:
        return self.__HouseNumber;

    @HouseNumber.setter
    def HouseNumber(self, number:int):
        if(type(number)  != int):
            raise TypeError("@HouseNumber: must be a numberical value");
        self.__HouseNumber  =  number;

    @property
    def Street(self):
        return self.__Street;
    
    @Street.setter
    def Street(self, street:str):
        if(type(street) != str):
            raise TypeError("@Street: must be a string object");
        self.__Street  =  street;


    def __repr__(self):
        return "LocationAddress(uuid={0},Postcode={1})".format(self.UUID,
                                                              self.Postcode);
        
if(__name__=="__main__"):
    address = LocationAddress(uuid="12343222", postcode="TW13 4TP");
    print(address);


    





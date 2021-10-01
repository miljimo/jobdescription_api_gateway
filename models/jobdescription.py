from datetime import datetime;
from models.locationaddress import LocationAddress;

class CleaningJobDescription(object):

    def __init__(self, uuid:str, 
                       description:str = "", 
                       address:LocationAddress= None,
                       email:str= "", 
                       phonenumber:str= "",
                       jobdate:datetime= datetime.now()):

        self.__UUID            =  uuid;
        self.__Description     =  description
        self.__Email           =  email;
        self.__Address         =  address
        self.__PhoneNumber     =  phonenumber;
        self.__DateTime        =  jobdate
        self.__CreateDateTime  =  datetime.now();
    
    @property
    def UUID(self):
        return self.__UUID;

    @property
    def CreateDateTime(self):
        return self.__CreateDateTime;

    @CreateDateTime.setter
    def CreateDateTime(self, datet:datetime):
        if(isinstance(datet, datetime)):
            self.__CreateDateTime = datet;
            
    @property
    def DateTime(self):
        return self.__DateTime;
    
    @DateTime.setter
    def DateTime(self, jdate:datetime):
        if(isinstance(jdate, datetime) is not True):
            raise TypeError("@Expecting a datetime object");
        self.__DateTime   =  jdate;
        
    @property
    def PhoneNumber(self):
        return self.__PhoneNumber;

    @PhoneNumber.setter
    def PhoneNumber(self, phoneNumber:str):
        if(type(phoneNumber) != str):
            raise TypeError("@PhoneNumber: expecting a string parameter");
        self.__PhoneNumber = phoneNumber;        

    @property
    def Address(self):
         return self.__Address;

    @Address.setter
    def Address(self, address:LocationAddress):
        if(isinstance(address, LocationAddress) is not True):
           raise TypeError("@Location: expecting a LocationAddress object");
        self.__Address  =  address;
        
    @property
    def Email(self):
        return self.__Email;
    
    @Email.setter
    def Email(self, email:str):
        if(type(email) != str):
            raise TypeError("@Email must be a string");
        self.__Email =  email;

    @property
    def Description(self):
        return self.__Description;

    @Description.setter
    def Description(self, desc:str):
        if(type(desc) != str):
            raise TypeError("@Description : must be a type of string");
        self.__Description =  desc;
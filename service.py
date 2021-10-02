from connector  import PostgresConnector, Option;
from procedure import Procedure
from queryresult import QueryResult


class Service(object):
    def __init__(self, option:Option):  
        self.__dbConn  =  PostgresConnector(option)       

    def serve(self, procedure : Procedure)->QueryResult:       
        try:
            self.__dbConn.connect();
            if(self.__dbConn.is_closed):
                raise ValueError("unable to connect to database server");  
            return  self.__dbConn.call_procedure(procedure); 
        except Exception as err:
            raise err;
        finally:
            if(self.__dbConn is not None) and (self.__dbConn.is_closed is not True):
                self.__dbConn.close();
            pass;



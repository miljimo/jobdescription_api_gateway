import unittest
import os
import sys
from postgres_service_gateway.connectors.connector    import PostgresConnector, Option
from postgres_service_gateway.connectors.queryresult  import QueryResult
from postgres_service_gateway.connectors.procedure    import Procedure;
from helpers.environment import Environment


class ConnectorTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.__dbConn = None;

    def setUp(self) -> None:
        Rolename = Environment.get("DB_USERNAME","testuser")
        Password = Environment.get("DB_PASSWORD","testpassword")
        Host     = Environment.get("DB_HOST_ADDRESS","localhost")
        Port     = Environment.get("DB_PORT",5432)
        DBName   = Environment.get("DB_NAME","testdb")
        

        option   = Option(dbname=DBName,
                        rolename= Rolename,
                        host = Host,
                        port = Port,
                        password= Password)      

        try:        
            self.__dbConn = PostgresConnector(option);
            self.__dbConn.connect()
            self.assertEqual(self.__dbConn.status, True);
        except Exception as err:
            if(self.__dbConn != None):
                if(self.__dbConn.is_closed is not True):
                    self.__dbConn.close();                
        super().setUp()

    def tearDown(self) -> None:
        if(self.__dbConn != None):
            if(self.__dbConn.is_closed is not True):
                self.__dbConn.close();
        return super().tearDown()   

    def test_PostgresConnected(self):
        Rolename = Environment.get("DB_USERNAME","testuser")
        Password = Environment.get("DB_PASSWORD","testpassword")
        Host     = Environment.get("DB_HOST_ADDRESS","localhost")
        Port     = Environment.get("DB_PORT",5432)
        DBName   = Environment.get("DB_NAME","testdb")
        
        option   = Option(dbname=DBName,
                        rolename= Rolename,
                        host = Host,
                        port = Port,
                        password= Password)

        psqlConn  = None

        try:        
            psqlConn = PostgresConnector(option);
            expected = True
            psqlConn.connect()           
            self.assertEqual(psqlConn.status, True)
        except Exception as err:
            raise err        
        finally:            
            if(psqlConn != None):
                psqlConn.close();
                pass;

    def testA_CallProcedureToCreateARecord(self):            
       proc = Procedure("locationaddressviewproc");
       proc.arg("pid", Procedure.STRING, "4" );
       proc.arg("ownerID", Procedure.STRING, "WideOpened" );
       proc.arg("postcode", Procedure.STRING, "NE13 6LD" );
       proc.arg("houseNumber", Procedure.STRING, "38" );
       proc.arg("street", Procedure.STRING, "Havannah");
       proc.arg("town", Procedure.STRING, "WideOpen");
       proc.arg("cstate", Procedure.STRING, "Havannah");
       proc.arg("country", Procedure.STRING, "United Kindown" );     
       query:QueryResult =  self.__dbConn.call_procedure(proc)

if __name__ =="__main__":
    unittest.main()

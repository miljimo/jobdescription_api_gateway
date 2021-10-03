import unittest
import os
import sys
from connector    import PostgresConnector, Option
from queryresult  import QueryResult
from procedure    import Procedure;


class ConnectorTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.__dbConn = None;

    def setUp(self) -> None:
        Rolename = "testuser"
        Password = "testpassword"
        Host     = "localhost"
        Port     = 5432
        DBName   = "testdb"
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
        Rolename = "testuser"
        Password = "testpassword"
        Host     = "localhost"
        Port     = 5432
        DBName   = "testdb"
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

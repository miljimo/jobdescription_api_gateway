import unittest
from queryresult import QueryResult;
from service import Service;
from connector import Option
from procedure import Procedure


class TestService(unittest.TestCase):


    def test_ServiceCall(self):
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
        service  =  Service(option)
        # Create procedure to called.
        proc = Procedure("locationaddressviewproc");
        proc.arg("pid",         Procedure.STRING, "101" );
        proc.arg("ownerID",     Procedure.STRING, "WideOpened" );
        proc.arg("postcode",    Procedure.STRING, "NE13 6LD" );
        proc.arg("houseNumber", Procedure.STRING, "38" );
        proc.arg("street",      Procedure.STRING, "Havannah");
        proc.arg("town",        Procedure.STRING, "WideOpen");
        proc.arg("cstate",      Procedure.STRING, "Havannah");
        proc.arg("country",     Procedure.STRING, "United Kindown" );   

        result:QueryResult = service.serve(proc)
        if(result.status is not True):
            raise result.error;


if __name__=="__main__":
    unittest.main();

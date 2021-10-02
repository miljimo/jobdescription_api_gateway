import unittest
from procedure import Procedure


class ProcedureTest(unittest.TestCase):

    
    def test_ProcedureWithParamters(self):
        proc = Procedure("locationaddressviewproc");
        proc.arg("pid", Procedure.STRING, "2" );
        proc.arg("ownerID", Procedure.STRING, "WideOpened" );
        proc.arg("postcode", Procedure.STRING, "NE13 6LD" );
        proc.arg("houseNumber", Procedure.STRING, "38" );
        proc.arg("street", Procedure.STRING, "Havannah");
        proc.arg("cstate", Procedure.STRING, "Havannah");
        proc.arg("country", Procedure.STRING, "United Kindown" );

        expected ="CALL locationaddressviewproc(pid => '2',ownerID => 'WideOpened',postcode => 'NE13 6LD',houseNumber => '38',street => 'Havannah',cstate => 'Havannah',country => 'United Kindown')"
        self.assertEqual(expected , str(proc))

    def test_ProcedureWithoutParameters(self):
        proc = Procedure("locationaddressviewproc");
        expected ="CALL locationaddressviewproc()"
        self.assertEqual(expected , str(proc))


if __name__ =="__main__":
    unittest.main()
                    






import unittest
import helper;
import json;


class TestHelper(unittest.TestCase):

    def test_loadPostgresDatabaseSection(self):
        filename="settings.ini";
        option = helper.load_postgres_database_settings(filename);
        self.assertNotEqual(option, None);        

    def test_HelperLoadProcedureFromJsonContent(self):
        jsonContent  =  """
            {
                "ProcedureName":"someprocedurename",
                "Parameters":[
                    {
                        "Field":"pid",
                        "Type":"string",
                        "Value":"1000"
                    },
                    {
                        "Field":"Name",
                        "Type":"string",
                        "Value":"Obaro"
                    },
                    {
                        "Field":"Gender",
                        "Type":"string",
                        "Value":"Male"
                    },
                    {
                        "Field":"Email",
                        "Type":"string",
                        "Value":"someone@email.com"
                    },
                    {
                        "Field":"Age",
                        "Type":"integer",
                        "Value": 90
                    },
                    {
                        "Field":"Money",
                        "Type":"number",
                        "Value": 10.90
                    }
                    
                ]
            }
        """
        jsobObect         = json.loads(jsonContent)        
        procedure, error  = helper.loadProcedureFromJsonRequest(jsobObect);
        if(error is not None):
            raise error;
        self.assertNotEqual(None,procedure);


if __name__ =="__main__":
    unittest.main();
    

        

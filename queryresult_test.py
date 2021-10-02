import unittest
from queryresult import QueryResult


class QueryResultTest(unittest.TestCase):
    
    def test_RowCount(self):
        result  = QueryResult(0);
        result.records = ( ( "Johnson",12,"31/09/1020"), ( "Obaro",32,"31/09/1020"))
        result.columns = ["Name", "Age", "Date"]
        result.row_counts =2;
        self.assertEqual(2, result.row_counts)      

    def test_Data(self):
        result  = QueryResult(0);
        result.records = ( "Obaro",32,"31/09/1020")
        result.columns = ["Name", "Age", "Date"]
        result.row_counts =1;
        
        data  = result.data();
        expected ={'Status': False, 'Error': 'None', 'RowCounts': 1, 'RecordSets': {'Name': 'Obaro', 'Age': 32, 'Date': '31/09/1020'}}
        self.assertDictEqual(expected, data);

if __name__ =="__main__":
    unittest.main()
                    






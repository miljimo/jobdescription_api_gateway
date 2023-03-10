import psycopg2
from dataaccess.connectors.queryresult import QueryResult;
from dataaccess.connectors.procedure   import Procedure
from dataaccess.connectors.option import Option

                
class PostgresConnector(object):

    def __init__(self, option:Option):        
        self.__option     = option;        
        self.__conn       =  None;

    def connect(self)->bool:
        self.__conn = psycopg2.connect(host = self.__option.host, 
                                       port = self.__option.port,
                                       database = self.__option.dbname,
                                       user=self.__option.rolename,
                                       password=self.__option.password);        
     
    @property
    def status(self):  
        if(self.__conn is not None):
            return self.__conn.status
        return False;

    @property
    def is_closed(self):
        if(self.__conn != None):
            return self.__conn.closed;
        return False;

    def close(self):
        if(self.__conn is not None):
            self.__conn.close();      
    
    def call_procedure(self, procedure:Procedure):
        if(type(procedure) != Procedure):
           raise ValueError("@call_procedure: parameter one must be Procedure type")
        queryStr =  procedure.__str__();
        print( queryStr)
        return self.__excute_query(queryStr)
        
    def __get_cursor(self):
        if(self.__conn == None):
                raise ValueError("@conn not initialised yet.");
        if(self.is_closed):
            raise ValueError("@connection is closed.")
        cur = self.__conn.cursor();
        if(cur == None):
            raise ValueError("@cursor return none.")   
        return cur; 

    def __excute_query(self, query:str)->QueryResult:
        result  = QueryResult(0)
        cur     = None;
        try:
            cur  = self.__get_cursor();        
            cur.execute(query);

            if(cur.rowcount > 0):
                #this operation must be a function otherwise                 
                if(cur.rowcount == 1):
                    resultsets     = cur.fetchone();
                else:                    
                    resultsets     = cur.fetchall();                    
                result.row_counts = cur.rowcount
                result.columns    = self.__getColumnNames(cur.description);               
                result.records    = tuple(resultsets);
            else:
                self.__conn.commit();
            cur.close();
            cur = None
            result.status  = True;
        except Exception as err:
            result.error   = err;
            result.status  = False;
            self.__conn.rollback();
        finally:
            if(cur is not None):
                if(cur.closed is not True):
                    cur.close();            
        return result;

    def __getColumnNames(self,columns:tuple):
        names  =  list();
        for col in columns:
            names.append(col.name.capitalize())
        return names;

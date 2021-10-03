from flask import request;
from connector import Option
from service   import Service;
from procedure import Procedure;
import helper;
import logger;

VERSION     = 1
__DB_OPTION = helper.load_postgres_database_settings(helper.DEFAULT_POSTGRES_DATABASE_FILE);
service     = Service(__DB_OPTION);   


def IndexController():
    data  = dict(Error = 'the resource does not exists');
    try:
        json_content  =  request.get_json();
        print(json_content);        
    except Exception as err:
        data['Error'] = str(err);      
    finally:
        if helper.recovered_error(data):           
            return data, 500      
        return data, 200
    

def ProcedureController():
    data  =  dict(Success   = False,
                      Error = None);
    responseCode  =  200;
    try:
        json_content  =  request.get_json();
        if(type(json_content) is not dict):
             raise TypeError("invalid json request sent, please check API documentation");
            
        procedure, error = helper.loadProcedureFromJsonRequest(json_content);
        if(error is not None):
            raise error;
        result = service.serve(procedure); 
        data['Results']   =  result.data()
        data['Success']   = True        
            
    except Exception as err:
        data['Error'] =  str(err);
        logger.error(err);
        
    finally:
        if(helper.recovered_error(data)):            
            responseCode = 500;
    return data, responseCode;


def ErrorHandlerController(errorcode):
    data  = dict(Error='resource not available.');   

    return data, 404;

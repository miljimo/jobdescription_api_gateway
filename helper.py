import os;
from procedure    import Procedure;
from configparser import ConfigParser;
from connector    import Option;

POSTGRES_SETTING_SECTION       ="POSTGRES_DATABASE_DEFAULT";
DEFAULT_POSTGRES_DATABASE_FILE ="settings.ini"

def recovered_error(data:dict) -> bool:
    if("Error" in data):
        if(data['Error'] != None) and (data['Error'] != ""):
            return True
    return False  


def load_postgres_database_settings(filename:str) ->Option:    
    option = None;
    try:
        parser = ConfigParser()      
        parser.read(filename)
        
        if(parser.has_section(POSTGRES_SETTING_SECTION) is not True):
            raise ValueError("setting section {0} not found".format(POSTGRES_SETTING_SECTION));
        params = parser.items(POSTGRES_SETTING_SECTION)
        rolename  =  None;
        password  =  None;
        dbname    =  None;
        port      =  None
        hostname  = None;
        
        for param in params:
            key = param[0];
            if(key=='username'):
                rolename  =  param[1];
            if(key=="password"):
                password  =  param[1];
            if(key =="dbname"):
                dbname  =  param[1]
            if(key=='port'):
                port = int(param[1]);
            if(key=='host'):
                hostname =  param[1];
                
        option = Option(rolename = rolename ,
                        password = password,
                        dbname=dbname,
                        port=port,
                        host=hostname);
    except Exception as err:
        raise err;
    finally:   
        return option;
    

def loadProcedureFromJsonRequest(content:dict)->tuple:
    PROCNAME   = "ProcedureName";
    PARAMETERS = "Parameters"
    FUNCTION   = "Function"
    procedure  =  None;
    exception  =  None;
    
    try:
        if(PROCNAME in content) is not True:
            return (None, ValueError("procedure name cannot be empty or None"));
        
        parameters = list();
        if(PARAMETERS in content) :  
            parameters  =  content[PARAMETERS];            
            if(type(parameters) != list):
                return (None, ValueError("expecting parameters to be a json list of Field, Type and Value"));
            
        isFunc  =  False
        if(FUNCTION in content):
             isFunc  =  bool(content[FUNCTION]);
             
        procedure  =  Procedure(content[PROCNAME], isFunc);
        for param in parameters:
            if("Field" in param) is not True:
                return (None, ValueError("field missing from procedure parameter"))            
            if("Type" in param) is not True:
                return (None, ValueError("type missing from procedure parameter"))
            if("Value" in param) is not True:
                return (None, ValueError("value missing from procedure parameter"))                
            procedure.arg(param["Field"],param["Type"], param['Value'])
        return (procedure, None);
        
    except Exception as err:
        return None, err

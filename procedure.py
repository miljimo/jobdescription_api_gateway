
class Procedure(object):

    STRING    = 'string';
    INTEGER   = 'integer'
    NUMBER    = 'number'
    __Types = (STRING, INTEGER, NUMBER)


    def __init__(self, procname:str, isfunction = False):
        self.__procname  =  procname;
        self.__arguments   = dict()
        #postgres have two type of store procedure function and procedure.
        self.__isfunction    = isfunction;

    @property
    def is_function(self):
        return self.__isfunction;


    def __validate(self, field:str, ctype:str, value:object)->Exception:
        if(type(field) != str):
            return TypeError("parameter 1 must be a string type")
        if(field in self.__arguments):
            return ValueError("field {0} already exist".format(field))
        
        if(ctype in self.__Types) != True:
            raise ValueError("@args : invalid type provided {0}".format(ctype))
        return None;
        

    def arg(self, field:str, ctype:str, value :object)->None:
        error  = self.__validate(field,ctype, value);
        if(error is not None):
             raise error;
        parameter  = (ctype, value)
        self.__arguments[field]=  parameter;

    def __str__(self):
        query = "";
        ncount  =  len(self.__arguments);
        #parametism procedure
        if(ncount > 0):
            result = "";
            for key in self.__arguments:
                ncount -= 1;
                data    =  self.__arguments[key]
                ctype   =  data[0];
                cvalue  =  data[1];
                param   =  "";
                
                if(ctype == self.STRING):
                   param  = "{0} => '{1}'".format(key,cvalue)
                   
                elif(ctype == self.INTEGER):
                    param  = "{0} => {1}".format(key, int(cvalue))
                    
                elif(ctype == self.NUMBER):
                    param  = "{0} => {1}".format(key, float(cvalue))
                    
                if(ncount > 0):
                    result += param + ","
                else:
                    result += param
            if(self.is_function):
                query = "SELECT * FROM {0}({1})".format(self.__procname, result)
            else:
                query = "CALL {0}({1})".format(self.__procname, result)
            
        else:
            if(self.is_function):
                query = "SELECT * FROM {0}()".format(self.__procname)
            else:
                query = "CALL {0}()".format(self.__procname)
        return query;


if __name__ =="__main__":
    proc = Procedure("locationaddressviewproc");
    proc.arg("pid", Procedure.STRING, "2" );
    proc.arg("ownerID", Procedure.STRING, "WideOpened" );
    proc.arg("postcode", Procedure.STRING, "NE13 6LD" );
    proc.arg("houseNumber", Procedure.STRING, "38" );
    proc.arg("street", Procedure.STRING, "Havannah");
    proc.arg("cstate", Procedure.STRING, "Havannah");
    proc.arg("country", Procedure.STRING, "United Kindown");
    
    
        
    

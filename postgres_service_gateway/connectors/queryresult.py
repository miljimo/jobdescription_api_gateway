import json

class QueryResult(object):
    

    def __init__(self, rowCount:int):
        self.__rowCounts   = rowCount;
        self.__records     = None;
        #use to indicate that the operation is success without error.
        self.__status      = False;
        self.__Error       = None
        self.__columns     = list();

    @property
    def columns(self):
        return self.__columns;

    @columns.setter
    def columns(self, columns:list):
        if(type(columns) != list):
            raise TypeError("expecting a list object");
        self.__columns  = columns;        
 
    def data(self):
        result  =  dict();
        result['Status']    =  self.status;
        result['Error']     =  str(self.error)
        result['RowCounts'] =  self.row_counts;
        records  =  dict();
        
        if(self.row_counts ==1):
             result['RecordSets'] = dict(zip(self.columns, self.records))
        else:
            records  = list();
            for row in self.records:
                records.append(dict(zip(self.columns, row)))
            result['RecordSets']   =  tuple(records)      
        return result
    
    @property
    def status(self):
        return self.__status;

    @status.setter
    def status(self, bval:bool):
        if(type(bval) != bool):
            raise  TypeError("status expecting a bool");
        self.__status  =  bval;

    @property
    def error(self):
        return self.__Error;

    @error.setter
    def error(self, err:Exception):
        if(isinstance(err, Exception) is not True):
            if(type(err) == str):
                err =  ValueError(err);
            else:
                raise TypeError("@error expecting an exception type");
        self.__Error  =  err;        
        
    @property
    def row_counts(self):
        return self.__rowCounts;
    
    @row_counts.setter
    def row_counts(self, row:int):
        if(type(row) != int):
            raise TypeError("row_counts: expecting an int type");
        self.__rowCounts  =  row;
        

    @property
    def records(self):
        return self.__records;
    
    @records.setter
    def records(self, records:tuple):
        if(type(records) != tuple):
            raise ValueError("@record property expecting a tuple but {0} given",type(records)) 
        self.__records = records;

from flask import Flask , request
import os;
import json
from flask import Flask;
import controllers;


class HttpServer(Flask):

    def __init__(self, appname:str):
        super().__init__(appname);

    def handle_func(self, route:str, func:callable, methods:list = ['GET','POST']):        
        super().add_url_rule(route,view_func=func, methods=methods);
        #check if the route have a foward slash
        char   = route[-1];
        if(char != '/'):
            route +='/'
            super().add_url_rule(route,view_func=func, methods=methods);
            
app      =  HttpServer(__name__)
app.handle_func("/",controllers.IndexController);
app.handle_func("/api/v{0}/dataaccess/proc".format(controllers.VERSION), controllers.ProcedureController, methods=['POST'])




if __name__ =="__main__":
    app.run();






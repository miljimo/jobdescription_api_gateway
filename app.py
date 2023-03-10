from flask import Flask
from helpers.environment import Environment
import postgres_service_gateway.controllers as controllers;

class HttpServer(Flask):

    def __init__(self, app_name:str):
        super().__init__(app_name:str);

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
    port = Environment.get("PORT", 8080)
    app.run(port=port)






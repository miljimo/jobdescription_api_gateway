
FROM python:3.9
WORKDIR /usr/src/teletruck

LABEL  AUTHOR="Obaro I. Johnson"
EXPOSE 80 443
# Assign a 
COPY requirements ./

RUN  pip install -r requirements
COPY ./postgres_service_gateway src
COPY .environ .environ
RUN /bin/bash -c 'source .environ'

# There can only be one command instructuion in docker file
CMD [ "python" , "./src/app.py"]





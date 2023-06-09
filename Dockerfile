# app/Dockerfile

FROM python:3.9-slim

RUN  apt-get update
RUN  apt-get upgrade



RUN apt-get install -y git
RUN apt-get install -y nano

WORKDIR /app
COPY requirements.txt app/requirements.txt
COPY intrepid-decker-383607-466e94005135.json app/intrepid-decker-383607-466e94005135.json

#install all requirements in requirements.txt
RUN pip install -r app/requirements.txt

#Copy all files in current directory into app directory
COPY . /app

#Change Working Directory to app directory
WORKDIR /app

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]

FROM python:3.10
MAINTAINER Rishaab
RUN apt-get update
COPY . .
RUN pip install -r requirements.txt
RUN streamlit run app.py --port 80

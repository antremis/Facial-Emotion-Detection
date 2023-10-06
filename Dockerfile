FROM ubuntu
MAINTAINER Rishaab
RUN apt-get update
RUN apt-get install python
COPY . .
RUN pip install -r requirements.txt
RUN streamlit run app.py --port 80
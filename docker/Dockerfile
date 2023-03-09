FROM ubuntu:22.04

RUN apt-get update -y && apt-get install python3 python3-pip -y

# Add samba-latest repository
RUN apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:linux-schools/samba4.16 && \
    apt-get update

RUN apt-get install samba -y

RUN mkdir /samba-ad-api
WORKDIR /samba-ad-api
COPY helpers helpers
COPY managers managers
COPY controllers controllers
COPY app.py app.py
COPY requirements.txt requirements.txt
RUN chmod +x app.py
RUN pip install -r requirements.txt


#ENTRYPOINT ["python3","sleep 1000"]
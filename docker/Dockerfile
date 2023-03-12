FROM ubuntu:22.04

# Add samba-latest repository
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:linux-schools/samba4.17 && \
    apt-get update

# Add samba-latest repository
RUN apt-get install python3-samba python3-pip  -y
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY app samba-ad-api
RUN chmod +x app.py
RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/sh","/entrypoint.sh"]
FROM python:3.8.10-slim
RUN apt-get update && dpkg --configure -a && mkdir /usr/share/man/man1 && apt-get install -y openjdk-11-jre
COPY ./ ./opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "-u", "api.py"]
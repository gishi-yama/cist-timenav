FROM python:3.8.10-slim
COPY ./ /opt/app/
WORKDIR /opt/app
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]

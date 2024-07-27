FROM python:3.9-slim
COPY app.py /
WORKDIR /
ENTRYPOINT ["python3", "run", "app.py"]

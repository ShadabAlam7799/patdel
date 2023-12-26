FROM nvidia/cuda:11.4.3-runtime-ubuntu20.04
FROM python:3.8
ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p projects
WORKDIR "/app1"

RUN apt-get update && \
 apt-get install -y git protobuf-compiler openssl curl google-perftools portaudio19-dev

COPY api.py .
COPY requirements.txt .
COPY patent_files.json .
ADD templates templates

RUN python -m venv venv_app1 && \
 . venv_app1/bin/activate && \
 pip install --upgrade pip && \
 pip install -r requirements.txt
 
#Expose any required ports
EXPOSE 5000
# Define the command to run your application
CMD ["python", "api.py"]
<h1 align="center">
    AIQ Python App
</h1>

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)

[//]: # (4. [API]&#40;#api&#41;)

[//]: # (5. [Testing]&#40;#testing&#41;)

[//]: # (6. [Contributing]&#40;#contributing&#41;)

[//]: # (7. [License]&#40;#license&#41;)

## Introduction
AIQ App is a docker container that uses FastAPI to provide a RESTful API. We are using mongodb database for this so
please provide mongodb connection url in src/common/constants.py before executing.

## Installation
#### 1. Install Requirements
```bash
pip install -r requirements.txt
```

#### Run the server locally
```bash
python -m gunicorn src.main:aiq_app --config gunicorn_conf.py
```
## Usage
#### Run the server locally with Docker
```bash
docker build -t aiq-python .
docker run --name aiq-python -it --expose 8080 -p 8080:80 aiq-python:latest
```
Note: Remove `-it` if you want to run the container in the background

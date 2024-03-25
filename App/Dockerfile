from python:3.11.4-slim-buster
workdir /code/
run pip install --upgrade pip
copy requirements.txt /code/
run pip3 install -r requirements.txt --no-cache-dir
copy . /code/
expose 8000
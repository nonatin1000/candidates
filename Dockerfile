FROM python:3
# Remove delay of log
ENV PYTHONUNBUFFERED=1
# Put /code as main directory
WORKDIR /code
RUN apt-get update && apt-get install -y vim
# Add requirements.txt in the code folder
COPY requirements.txt /code/
# Install project dependencies into docker
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
# Add the code to /code/
COPY . /code/
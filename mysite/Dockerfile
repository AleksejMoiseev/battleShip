FROM python:3.8
WORKDIR /usr/src/battleShip/mysite
COPY ./requirements.txt /usr/bin/src/requirements.txt
RUN pip install -r /usr/bin/src/requirements.txt
COPY . /usr/src/battleShip/mysite
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
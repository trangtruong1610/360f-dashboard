FROM namgivu/ubuntu-pipenv:18.04-3.7

WORKDIR /app

COPY ./Pipfile      .
COPY ./Pipfile.lock .
RUN pipenv sync

COPY . .


CMD PYTHONPATH=`pwd`   pipenv run gunicorn   -b '0.0.0.0:5000'   src.app:api

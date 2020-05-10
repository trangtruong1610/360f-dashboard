FROM namgivu/ubuntu-pipenv:18.04-3.7

WORKDIR /app

RUN echo 200510_x  # update this when Pipfile change to force a rerun
    COPY ./Pipfile      .
    COPY ./Pipfile.lock .
    RUN pipenv sync

COPY . .

# expose port 5000 as running falcon+gunicorn web app
ENV PORT=5000
EXPOSE $PORT
    CMD PYTHONPATH=`pwd`   pipenv run gunicorn   -b "0.0.0.0:$PORT"             src.app:api
    #   register src/      start web app instance            serve at this port    module:falcon_instance

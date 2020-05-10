# quick start
```bash
# start selenium chrome standalone node
./docker-selenium/compose-up.sh

# install package
: require python 3.6 & pipenv ref. bit.ly/nnpipenv
pipenv sync 

# run test
export PYTHONPATH="$PYTHONPATH:$PWD" ;
pipenv run  pytest -v -s tests/test_google_search.py ;
```

# run aqa api
```bash 
source ./docker-api/.config.sh   && ./docker-api/build.sh   && ./docker-api/run.sh   
    
    docker logs $CONTAINER_NAME  # read api log
    http GET :$PORT/health  # healthcheck api endpoint

```

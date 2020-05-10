# quick start
```bash
# start selenium chrome standalone node
./docker/compose-up.sh

# install package
: require python 3.6 & pipenv ref. bit.ly/nnpipenv
pipenv sync 

# run test
export PYTHONPATH="$PYTHONPATH:$PWD" ;
pipenv run  pytest -v -s tests/test_google_search.py ;
```

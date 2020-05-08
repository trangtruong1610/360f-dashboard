# quickstart
```bash
#start docker container
./docker/compose-up.sh

#run test
pytest -v -s test/test_selenium.py

#if error i.e ModuleNotFoundError: No module named 'webdriver_docker'
export PYTHONPATH=$PYTHONPATH:$PWD
```

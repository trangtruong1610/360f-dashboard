# quick start
```bash
# start selenium chrome standalone node
./docker/compose-up.sh

# install package
: require python 3.6 & pipenv ref. bit.ly/nnpipenv
pipenv sync 

# run test
export PYTHONPATH="$PYTHONPATH:$PWD" ;
    pipenv run  pytest -v -s test/test_selenium.py

    #TODO error
e="
    file_path = os.path.abspath(os.pardir)
    excel = f'{file_path}/fixture/test_fixture.xlsx'
    test_case = load_input_from_xlsx(excel)
    test/test_selenium.py:15: 
    ...
    E                   FileNotFoundError: [Errno 2] No such file or directory: '/home/namgivu/NN/code/_other_/trang/fixture/test_fixture.xlsx'
    
    /home/namgivu/.pyenv/versions/3.6.10/lib/python3.6/zipfile.py:1113: FileNotFoundError
    ================================ short test summary info =================================
    FAILED test/test_selenium.py::Test::test_01 - FileNotFoundError: [Errno 2] No such file...
    =================================== 1 failed in 2.07s ====================================
"

```

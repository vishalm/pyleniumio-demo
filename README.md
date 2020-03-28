# Pyleniumio Demo


<p>
  <a href="https://twitter.com/intent/follow?screen_name=vishalm84"><img align="left" src="https://img.shields.io/twitter/follow/vishalm84.svg?style=social&label=Follow%20@vishalm84" alt="Follow on Twitter"></a>
<br />
</p>



| **CI Provider**  | **Status** |
| ------------- | ------------- |
| **Github Actions**  | ![Pylenium demo](https://github.com/vishalm/pyleniumio-demo/workflows/Python%20application/badge.svg?branch=master)|
| **Travis** | [![Travis](https://travis-ci.org/vishalm/pyleniumio-demo.svg)](https://travis-ci.org/vishalm/pyleniumio-demo) *[Failing because of package installation but test is passing ... so all good here :) ]*|


## Documentation
```url
https://elsnoman.gitbook.io/pylenium/
```

## Framework
```url
https://github.com/ElSnoMan/pyleniumio
```


### Required
* python 3.x.x
* pip3
* virtualenv
* [Install Chrome Driver](https://elsnoman.gitbook.io/pylenium/getting-started/install-chromedriver)
* [Run Tests in Parallel](https://elsnoman.gitbook.io/pylenium/testing/run-tests-in-parallel)
* [Docker-Setup](https://elsnoman.gitbook.io/pylenium/testing/run-tests-in-containers)
  


### Quick Setup
* Clone
  ```bash
    git clone https://github.com/vishalm/pyleniumio-demo.git
    cd pyleniumio-demo
  ```
  
* python --verison
  ```bash
    Python 3.8.0
  ```
* pip3 install
    ```bash
        pip3 install virtualenv
        virtualenv .env
        source .env/bin/activate
        pip install pyleniumio
    ```
* Run 
    ```python
        python -m pytest ui_tests/test_qap_dev.py
    ```

* Execution Log
  
```bash
(.env)vishalmishra$ python -m pytest ui_tests/test_qap_dev.py
============================= test session starts ==============================
platform darwin -- Python 3.8.0, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /Users/vishalmishra/selenium-demo/pylenium-demo
plugins: xdist-1.31.0, forked-1.1.3
collected 1 item

ui_tests/test_qap_dev.py .                                               [100%]

============================== 1 passed in 9.03s ===============================
```


###### Credits : https://github.com/ElSnoMan/pyleniumio

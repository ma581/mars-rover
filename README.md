# Mars Rover

## Setup

#### Install and activate Python [virtual env](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) 

In the project root directory, run:
```shell
# If you have already installed `virtualenv`, you can skip this first command 
$ python3 -m pip install --user virtualenv 

# Create a virtualenv called 'venv'
$ python3 -m venv venv

# Activate the virtualenv you created
$ source venv/bin/activate
```


## How to run

```shell
(venv) $ python marsrover.py 4 8  '(2, 3, E) LFRFF' '(0, 2, N) FFLFRFF'                
```


## Tests
```shell
(venv) $ python -m unittest
```
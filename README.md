# cuatro_en_linea
Basic implementation of the `connect four` game, using the OOP paradigm.

## Install with virtualenv
Builds are performed against Ubuntu 16.04 and Python 2.7.9. Follow these steps to get such a setup in a separate virtual environment:
- Install dependencies:
```
$ sudo apt-get install git wget python-virtualenv python-scipy
```
- Download and compile Python 2.7.9:
```
$ cd ~
$ mkdir PythonInstalls
$ cd PythonInstalls
$ wget http://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz
$ tar xfz Python-2.7.9.tgz
$ cd Python-2.7.9/
$ ./configure --prefix /usr/local/lib/python2.7.9 --enable-ipv6
$ make
$ make install
```
- Just to be sure things went ok:
```
$ /usr/local/lib/python2.7.9/bin/python -V
Python 2.7.9
```
- Clone the repo in your machine and `cd` into it:
```
$ cd ~
```
`$ git clone https://github.com/apojomovsky/cuatro_en_linea.git`
```
$ cd cuatro_en_linea
```
- Setup virtualenv with the proper binary:
```
$ virtualenv -p /usr/local/lib/python2.7.9/bin/python2.7 env
Running virtualenv with interpreter /usr/local/lib/python2.7.9/bin/python2.7
New python executable in env/bin/python2.7
Also creating executable in env/bin/python
Installing setuptools, pip...done.
```
- Activate the new virtual environment (important: each time you start a new terminal session you must execute this line to load the proper environment):
```
$ source env/bin/activate
```
- Install pep 8:
```
$ pip install pep8==1.7.0
Downloading/unpacking pep8==1.7.0
  Downloading pep8-1.7.0-py2.py3-none-any.whl (41kB): 41kB downloaded
Installing collected packages: pep8
Successfully installed pep8
Cleaning up...
```
- Unfortunately, we need to install numpy by hand (see https://github.com/numpy/numpy/issues/2434):
```
$ pip install numpy
```
- Setup project dependencies:
```
$ python setup.py develop
```
- Verify tests and pep8 are passing:
```
./run_tests.sh
./run_pep8.sh
```

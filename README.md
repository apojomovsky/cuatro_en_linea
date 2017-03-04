# cuatro_en_linea
Basic implementation of the `connect four` game, using the OOP paradigm.

## Install with virtualenv
Builds are performed against Ubuntu 16.04 and Python 2.7.9, but has also been tested working against Ubuntu 14.04. Follow these steps to get such a setup in a separate virtual environment:
- Install virtualenv:
```
$ sudo apt-get install wget python-virtualenv
```
- Download and compile Python 2.7.9:
```
$ sudo apt-get build-dep python2.7
$ cd ~
$ mkdir PythonInstalls
$ cd PythonInstalls
$ wget http://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz
$ tar xfz Python-2.7.9.tgz
$ cd Python-2.7.9/
$ ./configure --prefix /usr/local/lib/python2.7.9 --enable-ipv6
$ make
$ sudo make install
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
- Unfortunately, we need to install numpy by hand (see https://github.com/numpy/numpy/issues/2434):
```
$ pip install numpy==1.12.0
```
- Setup the other project dependencies:
```
$ python setup.py develop
```
- Verify tests are passing:
```
./run_tests.sh
```

## Running a Match
- First of all, make sure that you placed your strategy class file inside the `game/` directory.
- You can test your own strategy by playing against any of the built-in strategies or any other third party strategy by running a match.
- To run a new match you should make use of the `run_game.py` script, also placed inside the `game/` directory
- For this, open the file `run_game.py` on your favorite text editor (vim, for instance :P), and add your strategy class to the list of imports, just as the example below:
```
from super_duper_strategy import SuperDuperStrategyClass
```
- After that, you'll need to add your strategy to the lookup_strategies dictionary, for which we recommend to follow the same convention:
```
lookup_strategies = {
		(...)
    'super_duper': SuperDuperStrategy
}
```
- If everything went OK, now you should be able to play a match against any of the strategies placed inside the lookup dictionary, so let's play a match!
- In order to run a match, you'll need to provide both strategies names as arguments, followed by the rate at which you want each move to be done, let's see an example:
```
$ cd game/
$ python run_game.py --player-one closest_to_win_column --player-two my_super_duper_strategy --rate 0.5
```
- This will spawn a new game, and you'll be able to see the evolution of the game turn by turn. An example of what is shown in the middle of a gameplay is shown above:
```
None None None None None None None
None None None None None None None
None None None None None None None
W    None None None None None None
W    None None None None None None
W    B    B    None None None None

```
- After the game has finished you'll see a message with the result of the match, for example:
```
Color W won!
```
or
```
Nobody won!
```

## Running a Tournament
- You can run a tournament between an arbitrary number of strategies.
- It's possible to define which strategies will be involved on the tournament by opening the `run_tournament.py` file on yor text editor and modifying the `strategies` tuple by adding/removing the strategies classes what you want to participate. Let's take a look at the example below:
```
strategies = (
	ClosestToWinColumn,
	SuperDuperStrategy,
	TheBestStrategyEver
)
```
- A minimum of three strategies are needed in order to run a tournament, an exception will be raised otherwise
- After filling the list with the desired strategies to play, save the file and run the script in the following way:
```
$ cd game/
$ python run_tournament.py
```
- The all the matches will run automatically at this point, one after the other.
- After all the matches have run, a table with the results of each of them will be displayed, followed by a summary with the score earned by each of the strategies and the name of the winner. You can see an example below:
```
Results table:
Player1                     Player2                     Winner
--------------------------  --------------------------  --------------------------
FirstNonFullColumnStrategy  EmptiestColumnStrategy      FirstNonFullColumnStrategy
FirstNonFullColumnStrategy  ClosestToWinColumnStrategy  FirstNonFullColumnStrategy
FirstNonFullColumnStrategy  RandomColumnStrategy        RandomColumnStrategy
EmptiestColumnStrategy      FirstNonFullColumnStrategy  EmptiestColumnStrategy
EmptiestColumnStrategy      ClosestToWinColumnStrategy  EmptiestColumnStrategy
EmptiestColumnStrategy      RandomColumnStrategy        RandomColumnStrategy
ClosestToWinColumnStrategy  FirstNonFullColumnStrategy  ClosestToWinColumnStrategy
ClosestToWinColumnStrategy  EmptiestColumnStrategy      ClosestToWinColumnStrategy
ClosestToWinColumnStrategy  RandomColumnStrategy        ClosestToWinColumnStrategy
RandomColumnStrategy        FirstNonFullColumnStrategy  FirstNonFullColumnStrategy
RandomColumnStrategy        EmptiestColumnStrategy      RandomColumnStrategy
RandomColumnStrategy        ClosestToWinColumnStrategy  ClosestToWinColumnStrategy

Scores:
RandomColumnStrategy: 9
FirstNonFullColumnStrategy: 9
ClosestToWinColumnStrategy: 12
EmptiestColumnStrategy: 6
The winner of the tournament is: ClosestToWinColumnStrategy, with 12 points
```

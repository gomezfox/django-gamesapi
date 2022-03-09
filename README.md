# cd to the folder you want to contain your project directory and create the directory
mkdir django-api && cd django-api

# ensure python is aliased to python3 and python3 is aliased to your system's python3.9 (or later)
# if not, upgrade your python and alias them appropriately
which python3
which python

# ensure pip is aliased to pip3
which pip

# create a virtual environment (creates a folder env for example and puts creates bin and lib directories inside)
# the bin and lib directories will contain copies of your python executables, as well as scripts for using your venv
# the following uses python3's built-in virtual environment and creates it in a folder called env

python3 -m env

# activate your virtual environment
# running the activation script will change your PATH and realias the python executables to use the copies in bin
# it will also use the lib directory for all dependencies instead of installing them systemwide

source env/bin/activate

# your command line prompt will change to reflect that your venv is activated
# you should also see pyenv.cfg in the root folder of the venv



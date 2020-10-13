## ------------------- Python Setup ----------------------

This guide will allow you to install python through Anaconda.

- How to install Anaconda
- How to setup an environment 

### anaconda setup

1. go to https://www.anaconda.com/distribution/ and download link for Python 3.7 version
2. Complete the installation
3. On your terminal: update your base Anaconda packages. These should be already installed
    - `conda update conda`
    - `conda update anaconda`
    - `conda update python`
    - `conda update --all`

### creating the dev enviroment in anaconda

1. create an anaconda enviroment 
  - `conda create --name ADAS_env python=3.7 pip`
    - this create an enviroment called `Work_env` with python version 3.7 installed, and installs pip as well
2. activate that enviroment `. activate ADAS_env`  (MacOS), or  `conda activate Work_env`  (Windows)
  - later if you want to deactivate you can do this `. deactivate Work_env`
3. installing packages:
  - cd to the directory where requirements.txt is located. (i.e. `cd Desktop/Annotation_Tool/`)
  - `pip install -r requirements.txt` 
4. create a Jupyter kernel
  - With your `ADAS_env` environment activated do `conda install ipykernel`
  - `python -m ipykernel install --user --name ADAS_env --display-name "ADAS_env"` 



### Opening the notebook with python - recommended

1. Open your command prompt and activate your environment
2. From the command prompt cd to the directory where the notebooks are located. 
3. Lauch the script from terminal by typing `python name_of_script.py`
4. Once the script is launched, follow the instructions: select case e name of file

#### Note: you need to :

- Create folder called "labels" into each case folder
- Change path of  working directory path_all in the .py script
- After performing the annotation, close the plot and relaunch the script following the instructions above by typing `python name_of_script.py`.
- Restart the annotation
- Note: if the user wants to change any of his selections, he needs to move forward to the next plot by clicking 'Next', perform a selection of the anomalous data, and then go back and restart.



### Opening the notebook with jupyter

1. Open your command prompt and cd to the directory where the notebooks are located. 
2. Open the notebook from terminal by typing `jupyter notebook`
3. Once the notebook is open, select your `ADAS_env` kernel from Kernel
4. Follow the instructions




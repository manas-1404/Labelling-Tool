## ------------------- Python Setup ----------------------

This guide will allow you to install python through Anaconda.

- How to install Anaconda
- How to setup an environment 

### anaconda setup

1. go to https://www.anaconda.com/distribution/ and download link for Python 3.7 version
2. Complete the installation
3. On your terminal (MacOS) or on your Anaconda Prompt (Windows): update your base Anaconda packages. These should be already installed
    - `conda update conda`
    - `conda install jupyter`

### creating the dev enviroment in anaconda

1. create an anaconda enviroment 
  - `conda create --name Worka_env python=3.7 pip`
    - this create an enviroment called `Work_env` with python version 3.7 installed, and installs pip as well
2. activate that enviroment `. activate Work_env`  (MacOS), or  `conda activate Work_env`  (Windows)
  - later if you want to deactivate you can do:  `. deactivate Work_env` (MacOS) or `conda deactivate` (Windows)
3. installing packages:
  - cd to the directory where requirements.txt is located. (i.e. `cd Desktop/Annotation_Tool/`)
  - `pip install -r requirements.txt` 
4. create a Jupyter kernel
  - With your `Work_env` environment activated do `conda install ipykernel`
  - `python -m ipykernel install --user --name Work_env --display-name "Work_env"` 

### Opening the notebook with jupyter

1. Open your command prompt and cd to the directory where the notebooks are located. 
2. Open the notebook from terminal by typing `jupyter notebook`
3. Once the notebook is open, select your `Work_env` kernel from Kernel
4. Follow the instructions




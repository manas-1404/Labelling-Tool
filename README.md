# Interactive annotation tool for data labelling

Annotation in machine learning is the process of labeling data. Annotation of data sets is considered a tedious and a challenging task. Howevere it is still a necessary step to provide labelled data. 

In the context of the ADASen project, we want to address research questions regarding the utility of supervised and unsupervised machine learning models in anomaly detection. We have therefore selected a range of anomaly detection methods for benchmarking on environmentatal data.  

Critical to the benchmarking is the availability of fully labelled training and test data sets of normal and abnormal behavior in environmental data. 

For this purpose, we have created an interactive annotation tool that allows to perform the labelling procedure. The tool has being designed to facilitate the user's labelling procedure by using interactive widgets from the matplotlib library.

Labelled data is then returned for future further analysis.

Link Gitlab: https://gitlab.com/stefania8/data-labelling-tool



# Getting Started

### Prerequisites and Installing

The scripts run in Python that should be installed on your local machine. For installing the libraries, cd from terminal to the directory where requirements.txt is located and run (on your terminal):

`conda install -r requirements.txt`



## Repository content (general):

Here are shown three examples : 

1. FCS Data annotation tool: `FCS_data_annotation.ipynb`  is applied on .fcs data sets, where each data file is visusalised as a scatter plot that can be labelled by choosing from a series of different labels. This tool is based on the `event_handling` API from matplotlib.
2. UWO Data annotation tool: `UWO_data_annotation.ipynb`  is based on `SpanSelector`, a mouse widget from matplotlib used to select areas of the plot, returning the values within it. This data annotation tool is applied on time series data and it is used for single and multi-variate data sets.
3. NEST Data annotation: `NEST_data_annotation.ipynb`  is based on `SpanSelector`, a mouse widget from matplotlib used to select areas of the plot, returning the values within it. This data annotation tool is applied on time series data and it is used for single and multi-variate data sets. This tool can be used as .py version
4. `functions`
   - Functions for data preparation
5. `data_example`: examples of data sets types needed for running the labelling tool

Other files

- `requirements.txt`
  - Installation requirements
- `README_Python_setup.md`
  - Instructions to install Python



# FCS data

##### If not using the requirements file, make sure to have access to fcs data:

- Install anaconda with python 3.4
- Open anaconda prompt
- ''$ conda install -c bioconda fcsparser'

##### Using fcsparser

> ```python
> import fcsparser
> path = fcsparser.test_sample_path
> meta, data = fcsparser.parse(path, reformat_me)
> ```

### Data

- Create a folder where to store the data. The location of the folder will be your `path_base`. The folder name will be `folder` in the Jupiter notebook
- The repository contains examples of data sets types needed for running the labelling tool

The data is generated by means of an on-line flow cytometer. Each data file contains several folders with several samples.

This system automatically collects and prepares a water sample on a regular basis and measures a variety of properties for each particle in the prepared water sample. 

Each sample consists of several measured variables (columns) and observations (rows) from thousands to millions of particles. In general, the number of particles captured with a single measurement will vary over time. 



### Repository content 

- `FCS_data_annotation.ipynb` 

  - Allows labelling and saves the labels in each data file as `Labels_.txt`. Usage of the notebook can be found in the notebook itself

- `labels_processing/_FCS_labels_processing.ipynb` 

  - Post-process the labels. Here, label duplicates (e.g. when the labelling expert changed his mind) are removed and labels are saved in each data file as `Labels_postproc.csv`. Afterwards, for each sample of a specific data file, a unique ID is created and labels are associated to it by adding a column. For each data file containing several samples (e.g. s1, s2) a final data set is created by combining all the samples and their associated labels. The data set is saved as pickle file. 

  

# UWO data

### Data

Create a folder where to store the data. The location of the folder will be your `path_base`. The folder name will be `folder` in the Jupiter notebook. The repository contains examples of data sets types needed for running the labelling tool. The data is in the form of .csv data files. Each data file consists of many 24h sets across 3 sensors, the data  is in the format:

| time                | sensor1 | Sensor2 | sensor3 |
| ------------------- | ------- | ------- | ------- |
| yyyy-mm-dd hh:mm:ss | float   | float   | float   |



### Repository content

- `UWO_data_annotation.ipynb` 
  - Allows labelling and saves the labels for each sensor as `Labels_Anomaly_sensor_name.csv`. Usage of the notebook can be found in the notebook itself
- `labels_processing/_UWO_labels_processing.ipynb` 
  - Post-process the labels. Here, label duplicates (e.g. when the labelling expert changed his mind) are removed and labels are saved in each data file as pickle file: `sensor_name_Anomaly`. Afterwards,  a final data set is created by combining all the data and anomalies into a collective anomaly. The data set is saved as pickle file : `UWO_Anomaly_collective`. 



# NEST data

### Data

Create a folder where to store the data. The location of the folder will be your `path_base`. The folder name will be `folder` in the Jupiter notebook. The repository contains examples of data sets types needed for running the labelling tool. The data is in the form of .csv data files. Each data file consists of many 24h sets across 2 sensors, the date type is in the format:

| day        | hour     | sensor1 | sensor2 |
| ---------- | -------- | ------- | ------- |
| dd.mm.yyyy | hh:mm:ss | float   | float   |



### Repository content 

- `NEST_data_annotation.ipynb` 
  - Allows labelling of data file `data_name`and saves the labels for each sensor as `data_name_labels_time_sensor_name.csv`. Usage of the notebook can be found in the notebook itself
- `labels_processing/_NEST_labels_processing.ipynb` 
  - Post-process the labels. Here, label duplicates (e.g. when the labelling expert changed his mind) are removed and labels are saved in each data file as pickle file: `sensor_name_Anomaly`. Afterwards,  a final data set is created by combining all the data and anomalies into a collective anomaly. The data set is saved as pickle file : `CaseName_Anomaly_collective`. 



### Opening the notebook with jupyter

1. Open your command prompt and cd to the directory where the notebooks are located. 
2. Open the notebook from terminal by typing `jupyter notebook`
3. Once the notebook is open, select your `Work_env` kernel from Kernel
4. Follow the instructions


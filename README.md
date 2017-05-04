## Udacity Machine Learning Nanodegree: Capstone Project

## Intro

My capstone project is about predicting air pollutants using eXtreme Gradient Boosting (XGBoost). Please see my [proposal](https://github.com/ginberg/mlcapstone/blob/master/proposal.pdf) for a full explanation, this Readme describes how to install and run the code.

### Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [xgboost](https://github.com/dmlc/xgboost) 

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)

I recommend to install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 

### Code

The code is provided in different files: 

- `airquality.ipynb` is the notebook file
- `util.py` contains common functionality

### Run

In a terminal or command window, navigate to the project directory that contains this README and run the following command:

```jupyter notebook airquality.ipynb```

This will open the iPython Notebook software and project file in your browser.

### Data

The dataset used in this project is included in the data directory as `TrainingData.csv`. You can find more information on this dataset on [Kaggle](https://www.kaggle.com/c/dsg-hackathon/data) page.
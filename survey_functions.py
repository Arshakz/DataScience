import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.metrics import accuracy_score
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D



def create_heatmap(dataframe, size):
    '''
    INPUT
    
    dataframe - name of dataframe for which you need to create heatmap
    size - size of heatmap you want to see
    
    OUTPUT
    creates dataframe
    
    '''
    fig, ax = plt.subplots(figsize=(size,size))
    return sns.heatmap(dataframe.corr(), annot=True, fmt='.2f', ax=ax);




def creating_graph(dfName, col1, col2):
    '''
    INPUT
    dfName - name of tadatframe
    col1 - column name 1 as string which need to be analyze
    col2 - column name 2 as string which need to be analyze
    
    OUTPUT
    The function takes 2 colums from dataset, joins them, counts how many times each one repeats and shows in the graph
    
    '''
    
    check_count=dfName.groupby([col1, col2]).size().reset_index().rename(columns={0:'count'})
    connect_col = check_count[col1]+ check_count[col2]
    f = pd.DataFrame({'Together':connect_col,'Counting':check_count['count']})  
    fig = plt.figure(figsize = (15,20))
    plt.bar(f['Together'], f['Counting'])
    plt.xlabel("Together")
    plt.ylabel("Counting")
    plt.xticks(rotation='vertical')
    return plt.show()


def plot_expectation(colExpectation):
    
    '''
    INPUT
    colExpectation- dataframe with the name of column which need to be plotted
    
    OUTPUT
    The function column of the dataframe which need to be plotted and returnes graph showing number of 
    expectations in five years
    
    '''
    
    vl_list=colExpectation.value_counts()
    x_col=[x for x, y in vl_list.items()]
    y_col=[y for x, y in vl_list.items()]
    fig = plt.figure(figsize = (10,10))
    plt.bar(x_col, y_col)
    plt.xlabel("Count")
    plt.ylabel("HopeFiveYears")
    plt.xticks(rotation='vertical')
    return plt.show()


def plot_two_cols(dfName, col1, col2, size):
    '''
    INPUT
    dfName - name of dataframe
    col1 - name of column which need to be plotted
    col2 - name of column which need to be plotted
    size - size of the ploth
    
    OUTPUT
    
    Creates plot from col1 and col2
    
    
    '''
    
    fig = plt.figure(figsize = (size,size))
    plt.bar(dfName[col1], dfName[col2])
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.xticks(rotation='vertical')
    return plt.show();
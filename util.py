## Utility file for airquality
import matplotlib.pyplot as plt

# group df by grouping variable. Next plot 
def plotLabelsAfterGroupingInOnePlot(df, groupFeature,  labels):
    fig, ax = plt.subplots(nrows=8,ncols=5, figsize=(20, 15))
    fig.suptitle("Mean pollution per " + groupFeature, fontsize=14)
    count = 1
    uniqueGroupValues = df[groupFeature].unique()
    df_mean_by_group = df.groupby([groupFeature]).mean()
    for label in labels:
        plt.subplot(8,5, count)
        plt.plot(uniqueGroupValues, df_mean_by_group[label], '-o')
        plt.title(label)
        count = count + 1
    plt.show()


def plotFeature(X,  title):
    plt.bar(range(len(X)), X.values(), align='center')
    plt.xticks(range(len(X)), X.keys())
    plt.ylabel('Count')
    plt.title(title)
    plt.show()
    
    
def plotHistogram(X,  xlabel): 
    plt.hist(X);
    plt.xlabel(xlabel)
    plt.ylabel('Count')
    plt.title(xlabel + ' distribution')
    plt.show()

    
def plotFeatures(X, Y,  xlabel,  ylabel,  title):
    plt.plot(X, Y, '-o')
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()

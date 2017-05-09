## Utility file for airquality
import matplotlib.pyplot as plt

# group the given dataframe by grouping feature. Next create a plot for each label. 
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

# Plot the given feature. It will create a bar plot with on the X axis the feature and on the Y axis the count.
def plotFeature(X,  title):
    plt.bar(range(len(X)), X.values(), align='center')
    plt.xticks(range(len(X)), X.keys())
    plt.ylabel('Count')
    plt.title(title)
    plt.show()

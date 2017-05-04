## Utility file for airquality
import matplotlib.pyplot as plt


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

    
def plotFeatures(X, Y):
    plt.scatter(X, Y, 
                    marker='x', 
                    color='b', 
                    alpha=0.7, 
                    s = 124, 
                    label='Target')

    # Chart title
    plt.title('Battles Of The War Of The Five Kings')
    # y label
    plt.ylabel('Defender Size')
    # x label
    plt.xlabel('Attacker Size')
    # and a legend
    plt.legend(loc='upper right')
    # set the figure boundaries
    #plt.xlim([min(df['attacker_size'])-1000, max(df['attacker_size'])+1000])
    #plt.ylim([min(df['defender_size'])-1000, max(df['defender_size'])+1000])
    plt.show()

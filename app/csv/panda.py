import pandas as pd
import matplotlib
from io import BytesIO
import base64
import geopy.distance

## Testing Panda Function before placing inside tasks.py ##

# Remove unwanted columns from original csv file. I kept only the most consistent columns and those that could make good graphs.
def removeColumns():
    data = pd.read_csv('listings.csv', low_memory=False)
    keep_col=['neighbourhood', 'latitude', 'longitude', 'property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'amenities','square_feet', 'price', 'cleaning_fee', 'review_scores_rating']
    newFile = data[keep_col]
    newFile.to_csv("formatted.csv", index=False)

# View csv without limitation
def displayFile():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('formatted.csv')
    print(data)

# Puts the average price of each neighbourhood into a dictionary
def averagePriceNeighbourhood():
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt, mpld3
    priceAverages = {}
    data = pd.read_csv('formatted.csv')
    neighbourhoods = ['Mission District', 'Western Addition/NOPA', 'SoMa', 'Richmond District', 'Bernal Heights', 'Noe Valley', 'The Castro', 'Nob Hill', 'Pacific Heights', 'Potrero Hill', 'Outer Sunset', 'Downtown', 'Haight-Ashbury', 'Lower Haight', 'Union Square', 'Marina', 'Inner Sunset', 'Duboce Triangle', 'South Beach', 'Chinatown', 'Tenderloin', 'Hayes Valley', 'Telegraph Hill', 'Russian Hill', 'Alamo Square', 'Excelsior', 'Cole Valley', 'Bayview', 'Twin Peaks', 'Sunnyside', 'Cow Hollow', 'Glen Park', 'North Beach', 'Parkside', 'Mission Terrace', 'Balboa Terrace', "Fisherman's Wharf", 'Crocker Amazon', 'Financial District', 'Oceanview', 'Ingleside', 'Dogpatch', 'Lakeshore', 'Presidio Heights', 'Portola', 'Civic Center', 'Visitacion Valley', 'Diamond Heights', 'Mission Bay', 'Forest Hill', 'West Portal', 'Japantown', 'Western Addition', 'Sea Cliff', 'Sunset District', 'Presidio', 'Soma', 'Fillmore District', 'Daly City']
    for neighbourhood in neighbourhoods:
        row_contains_neighbourhood = (data['neighbourhood'] == neighbourhood)
        neighbourhood_rows = data[row_contains_neighbourhood]
        average = round(neighbourhood_rows.price.replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True ).astype(float).mean())
        priceAverages[neighbourhood] = average
    print(str(priceAverages))

# Creates a bar graph of the top 5 most common values of a csv column. Converts to base64 image for html.
def graphBar(column):
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt, mpld3
    data = pd.read_csv("formatted.csv")
    plot = data[column].value_counts()[:5].plot(kind='bar')
    plt.tight_layout()
    plt.title('Top 5 instances of column %s' % column)
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    with open('img.txt', 'w') as imgfile:
        imgfile.write(figdata_png.decode('utf8'))

# Creates a pie graph to display the % of times each value occurres in a specified column. Base64 image.
def graphPie(column):
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt, mpld3
    data = pd.read_csv("formatted.csv")
    plt.pie(data[column].value_counts()[:5], labels=data[column].value_counts()[:5].index)
    plt.tight_layout()
    plt.title('Top 5 instances of column %s in pie graph' % column)
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    with open('img.txt', 'w') as imgfile:
        imgfile.write(figdata_png.decode('utf8'))

# Get average of reviews for each neighbourhood
def averageReview(column):
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt, mpld3
    ratingAverages = {}
    data = pd.read_csv('formatted.csv')
    neighbourhoods = ['Mission District', 'Western Addition/NOPA', 'SoMa', 'Richmond District', 'Bernal Heights', 'Noe Valley', 'The Castro', 'Nob Hill', 'Pacific Heights', 'Potrero Hill', 'Outer Sunset', 'Downtown', 'Haight-Ashbury', 'Lower Haight', 'Union Square', 'Marina', 'Inner Sunset', 'Duboce Triangle', 'South Beach', 'Chinatown', 'Tenderloin', 'Hayes Valley', 'Telegraph Hill', 'Russian Hill', 'Alamo Square', 'Excelsior', 'Cole Valley', 'Bayview', 'Twin Peaks', 'Sunnyside', 'Cow Hollow', 'Glen Park', 'North Beach', 'Parkside', 'Mission Terrace', 'Balboa Terrace', "Fisherman's Wharf", 'Crocker Amazon', 'Financial District', 'Oceanview', 'Ingleside', 'Dogpatch', 'Lakeshore', 'Presidio Heights', 'Portola', 'Civic Center', 'Visitacion Valley', 'Diamond Heights', 'Mission Bay', 'Forest Hill', 'West Portal', 'Japantown', 'Western Addition', 'Sea Cliff', 'Sunset District', 'Presidio', 'Soma', 'Fillmore District', 'Daly City']
    for neighbourhood in neighbourhoods:
        row_contains_neighbourhood = (data['neighbourhood'] == neighbourhood)
        neighbourhood_rows = data[row_contains_neighbourhood]
        average = neighbourhood_rows.review_scores_rating.astype(float).mean()
        ratingAverages[neighbourhood] = average

# Return average lat/lng position of each neighbourhood
def averageCoordinates():
    coordinateAverages = {}
    data = pd.read_csv('formatted.csv')
    neighbourhoods = ['Mission District', 'Western Addition/NOPA', 'SoMa', 'Richmond District', 'Bernal Heights', 'Noe Valley', 'The Castro', 'Nob Hill', 'Pacific Heights', 'Potrero Hill', 'Outer Sunset', 'Downtown', 'Haight-Ashbury', 'Lower Haight', 'Union Square', 'Marina', 'Inner Sunset', 'Duboce Triangle', 'South Beach', 'Chinatown', 'Tenderloin', 'Hayes Valley', 'Telegraph Hill', 'Russian Hill', 'Alamo Square', 'Excelsior', 'Cole Valley', 'Bayview', 'Twin Peaks', 'Sunnyside', 'Cow Hollow', 'Glen Park', 'North Beach', 'Parkside', 'Mission Terrace', 'Balboa Terrace', "Fisherman's Wharf", 'Crocker Amazon', 'Financial District', 'Oceanview', 'Ingleside', 'Dogpatch', 'Lakeshore', 'Presidio Heights', 'Portola', 'Civic Center', 'Visitacion Valley', 'Diamond Heights', 'Mission Bay', 'Forest Hill', 'West Portal', 'Japantown', 'Western Addition', 'Sea Cliff', 'Sunset District', 'Presidio', 'Soma', 'Fillmore District', 'Daly City']
    for neighbourhood in neighbourhoods:
        row_contains_neighbourhood = (data['neighbourhood'] == neighbourhood)
        neighbourhood_rows = data[row_contains_neighbourhood]
        averageLat = neighbourhood_rows.latitude.astype(float).mean()
        averageLon = neighbourhood_rows.longitude.astype(float).mean()
        coordinateAverages[neighbourhood] = (averageLat, averageLon)
    return coordinateAverages

# Returns the absolute lowest and highest lat/lng positions. To help me draw maps boundary
def getCoordinateBoundaries():
    lowx = 200
    highx = -200
    lowy = 200
    highy = -200
    for x in coordinateAverages:
        array = coordinateAverages[x]
        if array[0] < lowx:
            lowx = array[0]
        if array[0] > highx:
            highx = array[0]
        if array[1] < lowy:
            lowy = array[1]
        if array[1] > highy:
            highy = array[1]
            
    print("Low - [%s, %s], High - [%s, %s]" % (lowx,lowy,highx,highy))

def findClosestNeighbourhood():
    testPoint = (37.739515412875775, -122.43595722216799)
    feetDistance = 100000
    closestNeighbourhood = ''
    averages = averageCoordinates()
    for neighbourhood in averages:
        neighbourhoodLocation = averages[neighbourhood]
        distance = geopy.distance.vincenty(testPoint, neighbourhoodLocation).ft
        if distance < feetDistance:
            feetDistance = distance
            closestNeighbourhood = neighbourhood


if __name__ == '__main__':
    while True:
        command = input("Write or Read? \n")
        if command == 'write':
            removeColumns()
        elif command == 'read':
            displayFile()
        elif command = 'price':
            averagePriceNeighbourhood()
        else:
            print("no command")


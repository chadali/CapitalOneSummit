from app import celery, SocketIO
import time
import pandas as pd
import matplotlib.pyplot as plt, mpld3
from io import BytesIO
import base64, os

@celery.task(soft_time_limit=2, time_limit=4)
def test():
    try:
        time.sleep(1)
        print("Celery Works!")
    except Exception as e:
        raise Exception("Failed because of: %s" % e)

@celery.task(soft_time_limit=10, time_limit=14)
def plotGraph(column, graphNumber, sid):
    try:
        # Init SocketIO
        socketio = SocketIO(message_queue="redis://localhost:6379")
        # Open CSV
        csvdata = pd.read_csv("app/csv/formatted.csv")
        # Create and Configure Plot
        plot = csvdata[column].value_counts()[:5].plot(kind='bar')
        plt.tight_layout()
        # Save Plot IMG as 64Base Iamge
        figfile = BytesIO()
        plt.savefig(figfile, format='png')
        figfile.seek(0)
        figdata_png = base64.b64encode(figfile.getvalue())

        # Send to User
        socketio.emit('incoming-graph', {"graphNumber":graphNumber,"img64":figdata_png.decode('utf8')}, room=sid)
    except Exception as e:
        socketio.emit('message', {"message":"Failed because of: %s" % e}, room=sid)
        raise Exception("Failed because of: %s" % e)

@celery.task(soft_time_limit=20, time_limit=22)
def findAveragePrice(sid):
    try:
        # Init SocketIO
        socketio = SocketIO(message_queue="redis://localhost:6379")
        # init dictionary
        priceAverages = {}
        # load csv data
        data = pd.read_csv('app/csv/formatted.csv')
        # for each neighborhood format the price as a float value and calculate mean
        neighbourhoods = ['Mission District', 'Western Addition/NOPA', 'SoMa', 'Richmond District', 'Bernal Heights', 'Noe Valley', 'The Castro', 'Nob Hill', 'Pacific Heights', 'Potrero Hill', 'Outer Sunset', 'Downtown', 'Haight-Ashbury', 'Lower Haight', 'Union Square', 'Marina', 'Inner Sunset', 'Duboce Triangle', 'South Beach', 'Chinatown', 'Tenderloin', 'Hayes Valley', 'Telegraph Hill', 'Russian Hill', 'Alamo Square', 'Excelsior', 'Cole Valley', 'Bayview', 'Twin Peaks', 'Sunnyside', 'Cow Hollow', 'Glen Park', 'North Beach', 'Parkside', 'Mission Terrace', 'Balboa Terrace', "Fisherman's Wharf", 'Crocker Amazon', 'Financial District', 'Oceanview', 'Ingleside', 'Dogpatch', 'Lakeshore', 'Presidio Heights', 'Portola', 'Civic Center', 'Visitacion Valley', 'Diamond Heights', 'Mission Bay', 'Forest Hill', 'West Portal', 'Japantown', 'Western Addition', 'Sea Cliff', 'Sunset District', 'Presidio', 'Soma', 'Fillmore District', 'Daly City']
        for neighbourhood in neighbourhoods:
            row_contains_neighbourhood = (data['neighbourhood'] == neighbourhood)
            neighbourhood_rows = data[row_contains_neighbourhood]
            average = round(neighbourhood_rows.price.replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True ).astype(float).mean())
            priceAverages[neighbourhood] = average
        # return dictionary containing averages for each neighbourhood
        socketio.emit('priceAverages', {'average':priceAverages}, room=sid)
    except Exception as e:
        socketio.emit('message', {"message":"Failed because of: %s" % e}, room=sid)
        raise Exception("Failed because of: %s" % e)

@celery.task(soft_time_limit=20, time_limit=22)
def findHighestRating(sid):
    try:
        # Init SocketIO
        socketio = SocketIO(message_queue="redis://localhost:6379")
        # init dictionary
        ratingAverages = {}
        # load csv data
        data = pd.read_csv('app/csv/formatted.csv')
        # for each neighborhood format the rating as a float value and calculate mean
        neighbourhoods = ['Mission District', 'Western Addition/NOPA', 'SoMa', 'Richmond District', 'Bernal Heights', 'Noe Valley', 'The Castro', 'Nob Hill', 'Pacific Heights', 'Potrero Hill', 'Outer Sunset', 'Downtown', 'Haight-Ashbury', 'Lower Haight', 'Union Square', 'Marina', 'Inner Sunset', 'Duboce Triangle', 'South Beach', 'Chinatown', 'Tenderloin', 'Hayes Valley', 'Telegraph Hill', 'Russian Hill', 'Alamo Square', 'Excelsior', 'Cole Valley', 'Bayview', 'Twin Peaks', 'Sunnyside', 'Cow Hollow', 'Glen Park', 'North Beach', 'Parkside', 'Mission Terrace', 'Balboa Terrace', "Fisherman's Wharf", 'Crocker Amazon', 'Financial District', 'Oceanview', 'Ingleside', 'Dogpatch', 'Lakeshore', 'Presidio Heights', 'Portola', 'Civic Center', 'Visitacion Valley', 'Diamond Heights', 'Mission Bay', 'Forest Hill', 'West Portal', 'Japantown', 'Western Addition', 'Sea Cliff', 'Sunset District', 'Presidio', 'Soma', 'Fillmore District', 'Daly City']
        for neighbourhood in neighbourhoods:
            row_contains_neighbourhood = (data['neighbourhood'] == neighbourhood)
            neighbourhood_rows = data[row_contains_neighbourhood]
            average = neighbourhood_rows.review_scores_rating.astype(float).mean()
            ratingAverages[neighbourhood] = average
        # return dictionary containing averages for each neighbourhood
        socketio.emit('ratingAverages', {'average':ratingAverages}, room=sid)
    except Exception as e:
        socketio.emit('message', {"message":"Failed because of: %s" % e}, room=sid)
        raise Exception("Failed because of: %s" % e)

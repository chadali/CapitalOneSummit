# CapitalOneSummit

Website Submission for the Januray 2018 Capital One Summit

Live at _____________


## Abstract

The requirements of the challenge were to

1. **Visualize the data**: Graph some (any 3) interesting metrics, maps, or trends from the dataset.
2. **Price estimation**: Given the geo-location (latitude and longitude) of a new property, estimate the weekly average income the homeowner can make with Airbnb.
3. **Bookings optimization**: Given the geo-location (latitude and longitude) of a property, what is the ideal price per night that will yield maximum bookings or revenue?
4. **Optionally:**
   * **Animate**: Add an animation to your visualization.
   * **Investment**: If I have $100 million to invest, where in San Francisco should I buy properties so I can maximize my returns with Airbnb? When will I break even?
   * **Popularity**: Can you identify the neighborhood that averages the most positive reviews?

## Technology/Feature Breakdown

[Pandas](#pandas)

[Flask-SocketIO](#flask-socketio)

[Celery](#celery)

## Pandas

Pandas is a python tool that I used to process the huge CSV files. I barely touched it's full potential, but I tried my best to learn it fast. 

### Personal Notes:

#### Importing CSV

`data = pd.read_csv('xx.csv', nrows=10)

#### Filtering Functions

* `data['column_name']`
* `data['column1', 'column2']`
* `data['column1'][:10]`
* `.value_counts()`

#### Plotting (real time plotting on site??)

## Flask-SocketIO

Easy to implement websockets for Flask. Allows for a interactivity. In my use-case I can send data from asynchrous tasks directly to the user.

## Celery

Asynchrous tasks for long running functions. We can allow the user to do custom processing of CSV data with Celery.
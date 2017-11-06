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

Pandas is the python tool that I used to process the huge CSV files. I barely touched it's full potential, but I tried my best to learn it fast.

### Personal Notes:

#### Importing CSV

`data = pd.read_csv('xx.csv', nrows=10)`

#### Filtering Methods

##### Columns

* `data['column1']` - Isolate column1

##### Rows
*   ```is_true = data['column'] == "value" # Returns True/False
    is_also_true = data['other_column'] == "value" # Returns True/False
    data[is_true & is_also_true] # Returns a row if True inside
    ```

##### Functions
* `data[:10]` - Get first 10 rows
* `data['column'].value_counts()` - Get the number of instances of each value in a specific column

##### Plotting
* `data['column1'][:10].plot(kind='bar')` - Makes matplotlib which should be convertible to html

##### Conversion
`data['column'].value_count().astype(float)`

##### Math
```small_section = data[data['column'] == "value"].value_count()
full_section = data['column'].value_count()
full_section / small_section
```

#### Export CSV
```keep_col = ['KeepThis1', 'KeepThis2']
newFile = data[keep_col]
newFile.to_csv('name.csv')
```
    

## Flask-SocketIO

Using websockets allows for a nice dynamic user experience because data can be sent in real-time to the user's html. A better replacement for AJAX, it's a requirement in my use case for sending data from asynchronous tasks to HTML.

## Celery

Celery is Flask's option for running long asynchronous tasks. Let's me run any Python in the background, and then Websockets allow me to update a user's website data in realtime.

## Server Setup

### Commands

``` 
Sudo apt-get update
Sudo apt-get upgrade
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
git clone git@github.com:chadali/CapitalOneSummit.git
sudo apt-get install python3-venv
python3 -m venv env
sudo apt-get install python3-pip
pip3 install -r requirements.txt
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04

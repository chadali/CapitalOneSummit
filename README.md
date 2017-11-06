# CapitalOneSummit

Website Submission for the Januray 2018 Capital One Summit

Website live - [HERE](https://capitalonesummitsubmission.pw)

## Abstract

The requirements of the challenge were to

1. **Visualize the data**: Graph some (any 3) interesting metrics, maps, or trends from the dataset.
2. **Price estimation**: Given the geo-location (latitude and longitude) of a new property, estimate the weekly average income the homeowner can make with Airbnb.
3. **Bookings optimization**: Given the geo-location (latitude and longitude) of a property, what is the ideal price per night that will yield maximum bookings or revenue?
4. **Optionally:**
   * **Animate**: Add an animation to your visualization.
   * **Investment**: If I have $100 million to invest, where in San Francisco should I buy properties so I can maximize my returns with Airbnb? When will I break even?
   * **Popularity**: Can you identify the neighborhood that averages the most positive reviews?

## Summary

I created this website using Flask as the backend. The site can reflect new data in real-time because there are no static calculations or values. To achieve this I am running processing functions (which can be time consuming) asynchronous using Celery, and sending the user data using websockets. The site is hosted on a AWS EC2 Instance with Gunicorn, Nginx, and LetsEncrypt for SSL. Gevent, Redis, and Supervisor were necessary to run Celery and Flask-SocketIo. My weakness is lack of experience with data structures and algorithms, this project was a good introduction to simple data processing. A lot of time was spent just learning the basics of Pandas (data processing tool), but as a result next time I'll be able to jump right into more complex functionality.

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
sudo apt-get install build-essential python-dev python3-dev
sudo apt-get install python3-tk
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04
sudo apt-get install supervisor
sudo mkdir /etc/log/celery
sudo touch /var/log/celery/CapitalOne.log
vim /etc/supervisor/conf.d/CapitalOne.conf
sudo supervisorctl reread
sudo supervisorctl update
https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04
```

### Resources

Parallax.JS - http://pixelcog.github.io/parallax.js/
Arrow Bounce - https://codepen.io/bisaillonyannick/pen/pvZeGg
Bootstrap - http://getbootstrap.com/
Flask-SocketIO - https://github.com/miguelgrinberg/Flask-SocketIO
Pandas - http://pandas.pydata.org/
Celery - http://www.celeryproject.org/

# CapitalOneSummit

Website Submission for the Januray 2018 Capital One Summit. [Visit here](https://capitalonesummitsubmission.pw).

## Summary

This website was creating using Flask for the Jan 2018 Capital One Summit.

Hosted on a AWS EC2 Instance with Gunicorn, Nginx, Redis, Gevent, Supervisor, and LetsEncrypt for SSL.

Pandas (python library) was used to process CSV data. Real-time processing was achieved by using Celery to run Python code in the background and using websockets to update the HTML.

## Abstract

My submission fulfilled these requirements using the given CSV data files from AirBnB

1. **Visualize the data**: Graph some (any 3) interesting metrics, maps, or trends from the dataset.
   * Pandas had a plotting feature I wanted to implement. I allowed the user to choose which column they wanted to process, then using Websockets and Celery, Base64 data of a MatLibPlot (processed data graphed) is returned to the browser to be displayed.
2. **Price estimation / Optimization**: Given the geo-location (latitude and longitude) of a new property, estimate the weekly average income the homeowner can make with Airbnb. What is the ideal price per night that will yield maximum bookings or revenue?
   * I implemented Google Maps to allow the user to choose the geo-location. I again use Celery to calculate which neighbourhood is closest to the specific marker using the GeoPy library. In addition, I process the average price and sizes of houses in that neighbourhood as data returned to the user.
3. **Optionally:**
   * **Animate**: Add an animation to your visualization.
     * Parallax, Bootstrap, JQuery
   * ~~**Investment**: If I have $100 million to invest, where in San Francisco should I buy properties so I can maximize my returns with Airbnb? When will I break even?~~
   * **Popularity**: Can you identify the neighborhood that averages the most positive reviews?
     * BONUS button at the very bottom right of webpage. This was a simple average calculation with Pandas.

## Key Files

[Routes for Flask and Websockets (Views.py)](https://github.com/chadali/CapitalOneSummit/blob/master/app/views.py)

[Celery Tasks (Tasks.py)](https://github.com/chadali/CapitalOneSummit/blob/master/app/tasks.py)

[Index.html](https://github.com/chadali/CapitalOneSummit/blob/master/app/templates/index.html)

[Processing Testing (Panda.py)](https://github.com/chadali/CapitalOneSummit/blob/master/app/csv/panda.py)

## Technology Breakdown

## Pandas

Pandas is the python tool that I used to process the huge CSV files. I barely touched it's full potential, but I tried my best to learn it fast. Personal documentation kept [here](http://chadali.com/libraries/libraries/).

## Flask-SocketIO

Using websockets allows for a nice dynamic user experience because data can be sent in real-time to the user's html. A better replacement for AJAX, it's a requirement in my use case for sending data from asynchronous tasks to HTML.

## Celery

Celery is Flask's option for running long asynchronous tasks. Let's me run any Python in the background, and then Websockets allow me to update a user's website data in realtime.

## Server Setup

I wrote personal documentation of how I set the server up [here](http://chadali.com/server/server/). Combine with files located [here](https://github.com/chadali/CapitalOneSummit/tree/master/ServerFiles).

### Resources

Parallax.JS - http://pixelcog.github.io/parallax.js/

Arrow Bounce - https://codepen.io/bisaillonyannick/pen/pvZeGg

Bootstrap - http://getbootstrap.com/

Flask-SocketIO - https://github.com/miguelgrinberg/Flask-SocketIO

Pandas - http://pandas.pydata.org/

Celery - http://www.celeryproject.org/

GeoPy - https://github.com/geopy/geopy

![Landing](https://imgur.com/CZLq828.jpg)
![Navigation](https://imgur.com/Er9IVIl.jpg)
![Graph](https://imgur.com/78y64eb.jpg)
![Google Map](https://i.imgur.com/uNR5lto.png)

from audioop import avg
from unittest import result
from bs4 import ResultSet
import numpy as np
from requests import session
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct
from flask import Flask, jsonify
import datetime as dt

engine = create_engine("sqlite:///..Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Base.classes.keys()

measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Precipitation Stats In Hawaii<br/>"
        f"Available Routes:<br/>"
        f"Precipitation: /api/v1.0/precipitation<br/>"
        f"Active Stations: /api/v1.0/stations<br/>"
        f"Most Active Station: /api/v1.0/tobs<br/>"
        f"Temps From Start Date: /api/v1.0/yyyy-mm-dd<br/>"
        f"Temps Between Time Periods: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/>"
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    rain = [measurement.prcp, measurement.date]
    results = session.query(rain).all()
    session.close()

    precip = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["Date"] = date
        precipitation_dict["Precipitation"] = prcp
        precip.append(precipitation_dict)

return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)
    stats = [station.name, station.id, station.station, station.elevation
          station.latitude,station.longitude]
    results = session.query(stats).all()
    session.close()

    stations = []
    for name, id, station, ev, lat, long in results:
        stations_dict = {}
        stations_dict["Name"] = name
        stations_dict["ID"] = id
        stations_dict["Station"] = station
        stations_dict["Elevation"] = ev
        stations_dict["Latitude"] = lat
        stations_dict["Longitude"] = long
        stations.append(stations_dict)

return jsonify(stations)

@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    start = "2016-08-23"
    end = "2017-08-23"
    tob = [measurement.date, measurement.tobs]
    results = session.query(*sel).\
            filter(measurement.date >= start,
             measurement.station == 'USC00519281').all()
    session.close()

    tobs = []
    for min, max, avg in results
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Max"] = max
        tobs_dict["Avg"] = avg
        tobs.append(tobs_dict)

    return jsonify(tobs)













if __name__ == '__main__':
    app.run(debug=True)






        
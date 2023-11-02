# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
engine = create_engine("sqlite:/// hawaii.sqlite")

#################################################

# reflect an existing database into a new model
Base = automap_base(engine)
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Hawaii = Base.classes.hawaii

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
app = Flask(__name__)
#################################################


#################################################
# Flask Routes

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last year."""
    prev_year = dt.datetime.now() - relativedelta(days=365)
    prcp_data = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date >= prev_year).all()
    return jsonify(prcp_data)
session.close()



@app.route("/api/v1.0/stations")
def stations():
    station_list = session.query(station.station).order_by(station.station).all()
    return jsonify(station_list)
session.close()



@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.datetime.now() - pd.DateOffset(years=1)
    most_active_station = session.\
    query(measurement.station,func.count()).\
    group_by(measurement.station).\
    order_by(func.count().desc()).first()[0]
    temp_data = session.\
    query(measurement.date, measurement.tobs).\
    filter(measurement.station == most_active_station).\
    filter(measurement.date >= prev_year).all()
    return jsonify(temp_data)
session.close()

@app.route("/api/v1.0/<start>") 
def start_end(start):
    sel = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max
           (measurement.tobs)]
    result = session.query(*sel).filter(measurement.date>=start).all()
    return jsonify(result)
session.close()

@app.route("/api/v1.0/<start>/<end>")
def start_end2(start, end):
    sel = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max
           (measurement.tobs)]
    result = session.query(*sel).filter(measurement.date>=start).filter(measurement.date<=end).all()
    return jsonify(result)
session.close()

if__name__ == '__name__'
app.run(debug=True)



#################################################

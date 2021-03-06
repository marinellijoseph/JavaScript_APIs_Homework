# import necessary libraries
import numpy as np
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////belly_button_biodiversity.sqlite"

db = SQLAlchemy(app)

#################################################
# Routes
#################################################

@app.route("/")
def home():
    return render_template("index.html")
#    """Return the dashboard homepage."""

@app.route('/names')
def sample_names():
    return 

#     """List of sample names. 

#     Returns a list of sample names in the format
#     [
#         "BB_940",
#         "BB_941",
#         "BB_943",
#         "BB_944",
#         "BB_945",
#         "BB_946",
#         "BB_947",
#         ...
#     ]

#     """

# @app.route('/otu')
#     """List of OTU descriptions.

#     Returns a list of OTU descriptions in the following format

#     [
#         "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
#         "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
#         "Bacteria",
#         "Bacteria",
#         "Bacteria",
#         ...
#     ]
#     """

# @app.route('/metadata/<sample>')
#     """MetaData for a given sample.

#     Args: Sample in the format: `BB_940`

#     Returns a json dictionary of sample metadata in the format

#     {
#         AGE: 24,
#         BBTYPE: "I",
#         ETHNICITY: "Caucasian",
#         GENDER: "F",
#         LOCATION: "Beaufort/NC",
#         SAMPLEID: 940
#     }
#     """

# @app.route('/wfreq/<sample>')
#     """Weekly Washing Frequency as a number.

#     Args: Sample in the format: `BB_940`

#     Returns an integer value for the weekly washing frequency `WFREQ`
#     """

# @app.route('/samples/<sample>')
#     """OTU IDs and Sample Values for a given sample.

#     Sort your Pandas DataFrame (OTU ID and Sample Value)
#     in Descending Order by Sample Value

#     Return a list of dictionaries containing sorted lists  for `otu_ids`
#     and `sample_values`

#     [
#         {
#             otu_ids: [
#                 1166,
#                 2858,
#                 481,
#                 ...
#             ],
#             sample_values: [
#                 163,
#                 126,
#                 113,
#                 ...
#             ]
#         }
#     ]
#     """

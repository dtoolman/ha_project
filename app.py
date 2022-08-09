from pydoc import render_doc
from flask import Flask
from datetime import datetime
import folium

app = Flask(__name__)

@app.route("/")
def home():
    return app.render_template('home.html')

    # map = folium.Map(
    #     location=[44.9212, -93.4687],
    #     tiles='cartodbpositron'
    # )
    # x = map.add_child(folium.LatLngPopup())
    # print(x.to_json())
    
    # return map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
app = Flask(__name__)  #create instance of flask class. 
						# If only 1x module, just do __name__. Else give a new name.

@app.route('/sample')  # define url
def running():
    return 'Flask is running!'

	
# Then goto to terminal:
# D:\flask_apps>set FLASK_APP=sample_app.py
# D:\flask_apps>flask run --host=0.0.0.0
# Then goto browser url
# http://localhost:5000/sample
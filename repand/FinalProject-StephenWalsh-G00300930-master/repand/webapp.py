from flask import Flask, request
app = Flask(__name__)  


@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route('/hello')
def hello():
	return render_template('hello.html') 
@app.route('/New Zealand')
def hello():
	return render_template('nz.html')
	
@app.route("/peru") 
def name():         
	return "The capital of Peru is Lima"
@app.route("/australia") 
def australia(): 
 return "http://127.0.0.1:5984/country/countriesDB/" 
@app.route("/canada") 
def canada(): 
 return "The capital of Canada is Ottawa"
if __name__ == "__main__":     
	app.run()
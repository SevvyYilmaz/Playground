from flask import Flask, render_template   # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

#Have the /play route render a template with 3 blue boxes
@app.route('/play')
def playground():
    return render_template("index.html", num=3, color="cyan")

#Have the /play/<x> route render a template with x number of blue boxes
@app.route('/play/<int:num>')
def integer(num):
    return render_template("index.html", num=num, color= "blue")

#Have the /play/<x>/<color> route render a template with x number of boxes 
# the color of the provided value
@app.route('/play/<int:num>/<string:color>')
def color_and_int(num,color):
    return render_template("index.html", num=num, color= color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


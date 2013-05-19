from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return "EZCheck"

@app.route("/tickets/", methods=["GET"])
# Returns all tickets
def get_tickets():
	tickets = [
		{'ticket_id': 1, 'color': "black", 'license': "V3101N", 'first_name': "Jason", 'last_name': "Willow"},
	]
	return render_template("tickets.html", tickets=tickets)

@app.route("/tickets/", methods=["POST"])
# Post a new ticket
def post_tickets():
	pass

if __name__ == "__main__":
	app.run(debug=True)
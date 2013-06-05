import os
import ujson as json
import logging

from flask import Flask, request
from flask import render_template
from models import Ticket

app = Flask(__name__)

@app.route("/")
def hello():
	return "EZCheck"

@app.route("/tickets", methods=["GET"])
# Returns all tickets
def get_tickets():
	tickets = Ticket.all()
	return render_template("tickets.html", tickets=tickets)

@app.route("/tickets", methods=["POST"])
# Add a new ticket to the database
def post_tickets():
	ticket_form = request.form.to_dict()
	new_ticket = Ticket.create(ticket_form)

	if not new_ticket:
		return json.dumps({
			'error': "couldn't add ticket"
		}), 422

	return json.dumps({
        'ticket': new_ticket
    }), 200


if __name__ == "__main__":
	app.run(debug=True)
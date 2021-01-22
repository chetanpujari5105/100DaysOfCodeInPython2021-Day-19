from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
biding = {}
bidding_finished = False
def add_name_bid(bidding_record):
	hegest_bid = 0
	winner = ""
	for bidder in bidding_record:
		bid_amount = bidding_record[bidder]
		if bid_amount > hegest_bid:
			hegest_bid = bid_amount
			winner = bidder
	print(f"The winner is {winner} with a bid of ${hegest_bid}")
	

while not bidding_finished:
		name = input("What is your name? ")
		bid_price = int(input("what is your bit price $"))
		biding[name] = bid_price
		sould_continue = input("Are there are any other bidders? type yes or no")
		if sould_continue == "no":
			bidding_finished = True
			add_name_bid(biding)
		elif sould_continue == "yes":
			pass# clear()


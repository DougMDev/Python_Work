logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to The Silent Auction!")
Bids = {}
Bidding_Finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    ## bidding_record = {"James": 123, "Chivers": 349}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid}")

while Bidding_Finished == False:
    Name = input("What is Your Name?: ")
    Amount = int(input("What is Your Bid?: $"))
    Bids[Name] = Amount
    bidCheck = input("Are there any more Bidders? ")
    if bidCheck == "no":
        Bidding_Finished = True
        find_highest_bidder(Bids)
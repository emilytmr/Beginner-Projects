
import art

print(art.logo)


bidder = {}

while True:

    name = input("What's your name?")
    bid = int(input("How much do you want to bid ($)?"))

    bidder[name] = bid

    new_bid = input("Are there any other bidders? Yes or no?").lower()

    if new_bid == "no":
        break

    print("\n" * 25)

print(bidder)

highest_bidder = 0
for name in bidder:
    bid_amount = bidder[name]
    if bid_amount > highest_bidder:
        highest_bidder = bid_amount
        winner = name

print(f"The highest bidder is {winner}, with a bid of ${highest_bidder}")





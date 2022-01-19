from art import logo
bidders = {}
end = False
print('Welcome to blind auction')
print(logo)
while not end:
    name = input("Type your name : ")
    bid = int(input("Your bid is $"))
    bidders[name] = bid
    print("Is there other bidder?. Type 'yes' or 'no'")
    des = input()
    if des == "no":
        end = True
winner = ''
bigbid = 0
for key in bidders:
    curbidder = key
    curbid = bidders[key]
    if bigbid<curbid:
        winner = curbidder
        bigbid = curbid
print(f'The winner is {winner} with bid of ${bigbid}')
import random

def deal_card():
    return random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])

def calculate_score(hand):
    score = 0
    ace_count = hand.count('A')
    for card in hand:
        if card in 'JQK':
            score += 10
        elif card == 'A':
            score += 11
        else:
            score += int(card)
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
    return score

def play_blackjack():
    user_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    print(f"Your hand: {user_hand}, score: {calculate_score(user_hand)}")
    print(f"Dealer's hand: {dealer_hand[0]}, X")

    if calculate_score(user_hand) == 21:
        print("Blackjack! You win!")
        return

    while input("Type 'hit' to get another card, 'stand' to pass: ") == 'hit':
        user_hand.append(deal_card())
        print(f"Your hand: {user_hand}, score: {calculate_score(user_hand)}")
        if calculate_score(user_hand) > 21:
            print("You went over. You lose!")
            return

    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    print(f"Dealer's hand: {dealer_hand}, score: {calculate_score(dealer_hand)}")

    if calculate_score(dealer_hand) > 21 or calculate_score(user_hand) > calculate_score(dealer_hand):
        print("You win!")
    else:
        print("You lose!")

play_blackjack()

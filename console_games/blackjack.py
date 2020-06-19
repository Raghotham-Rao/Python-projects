import random


def check_bust(pl_tot):
   return pl_tot > 21


def game(cards, bet):
   random.shuffle(cards) # shuffle the cards
   values = []

   # store the values of each card in a different list
   for i in cards:
       if i == 'A':
           values.append(1)
       elif str(i) in 'KQJ':
           values.append(10)
       else:
           values.append(i)

   # initialize player and dealer cards
   dealer, player = [cards[1], cards[3]], [cards[0], cards[2]]
   dealer_total, player_total = values[1] + values[3], values[0] + values[2]
   card_counter = 4

   print('Player: ', *[i for i in player], ' Total: ', player_total)
   print('Dealer: ', dealer[0], '-  Total: ', values[1])

   if 'A' in player and any([i == player[(player.index('A') + 1) % 2] for i in ['K', 'Q', 'J', 10]]):
       print('=' * 5, 'BLACKJACK', '=' * 5)
       print('You Win this Round')
       return 5 * bet

   if 'A' in dealer and any([i == dealer[(dealer.index('A') + 1) % 2] for i in ['K', 'Q', 'J', 10]]):
       print('Dealer: ', *[i for i in dealer], '-  Total: ', dealer_total)
       print('=' * 5, 'BLACKJACK', '=' * 5)
       print('Dealer Wins Round')
       return -1 * bet

   # check bust
   if check_bust(player_total):
       print('=' * 5, 'Busted', '=' * 5)
       print('Dealer Wins Round')
       return -1 * bet

   choice = input('\nHit / Stand (H/S)?\n')
   # hit - stand
   while choice in 'hitHitHIT':
       player.append(cards[card_counter])
       player_total += values[card_counter]
       card_counter += 1
       print('Player: ', *[i for i in player], ' Total: ', player_total)
       print('Dealer: ', dealer[0], '-  Total: ', values[1])
       if check_bust(player_total):
           print('=' * 5, 'Busted', '=' * 5)
           print('Dealer Wins Round')
           return -1 * bet
       choice = input('\nHit / Stand (H/S)?\n')

   if 'A' in player and player_total <= 11:
       player_total += 11

   print('Player: ', *[i for i in player], ' Total: ', player_total)
   print('Dealer: ', *[i for i in dealer], ' Total: ', dealer_total)

   # dealer hand
   while True:
       if dealer_total > 21:
           print('You Win this Round')
           return bet * 2
       elif 'A' in dealer:
           if dealer_total + 10 <= 21:
               if dealer_total > player_total:
                   print('Dealer Wins Round')
                   return -1 * bet
               elif dealer_total == player_total:
                   print('PASS')
                   return bet
       elif dealer_total >= 17:
           if dealer_total > player_total:
               print('Dealer Wins Round')
               return -1 * bet
           elif dealer_total == player_total:
               print('PASS')
               return bet
           else:
               print('You Win this Round')
               return 2 * bet
       elif dealer_total > player_total:
           print('Dealer Wins Round')
           return -1 * bet
       dealer.append(cards[card_counter])
       dealer_total += values[card_counter]
       card_counter += 1
       print('\nPlayer: ', *[i for i in player], ' Total: ', player_total)
       print('Dealer: ', *[i for i in dealer], ' Total: ', dealer_total)


cards = [j for i in range(4) for j in range(2, 11)] + [i for j in range(4) for i in 'AJKQ']
print('Hey there wanna play a game of Blackjack?(Y/N)')
choice = input().upper()
purse = 1000
while True:
   # ask for a bet
   if choice in 'YesyesYES':
       print('how much do you wanna bet?')
       print('Purse Remaining:', purse)
       bet = int(input())
       purse -= bet
       earnings = game(cards, bet)
       purse += earnings if earnings > 0 else 0
       print('\nTotal Earnings = ', purse - 1000)
       print('Purse Remaining:', purse)
       choice = input('\nWanna try another round?\n')
   elif choice in 'noNo':
       break
   else:
       print('INVALID INPUT')
       choice = input('\nEnter valid input:\n')



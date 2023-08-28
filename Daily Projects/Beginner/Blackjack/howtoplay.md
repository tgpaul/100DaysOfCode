## Let's Play Blackjack!

### **How To Launch The Game: -**

To play Blackjack, aka 21, just run the file named '[main.py](Daily%20Projects\Beginner\Blackjack\main.py)'

### **Game Rules and How To Play: -**

#### **Objective:**

The main objective of Blackjack is to beat the dealer by having a hand value as close to 21 as possible without exceeding it. If your hand value exceeds 21, you bust and lose the game.

You are the 'Player' and the computer is the 'Dealer'.

#### **Card Values:**

- Number cards (2-10) are worth their face value.
- Face cards (Jack, Queen, King) are each worth 10 points.
- An Ace can be worth either 1 or 11 points, depending on which value benefits the player more.

#### **Gameplay:**

- The Player is dealt two face-up cards, while the dealer receives one face-up card (the "upcard") and one face-down card (the "hole card").
- The Player can choose from several actions:
  - Hit: Take another card to increase the hand's total value.
  - Stand: Keep the current hand without taking any more cards.
  - Double Down: Double the original bet and take one more card, then automatically stand.
  - Surrender: Some variations allow the player to forfeit their hand and recover half of their bet.

[comment]: < ( - Split: If the first two cards have the same value, the player can split them into separate hands by placing an additional bet. (have to see how to add this)) >

- Dealer's Turn:
  - After the Player has completed his/her actions, the Dealer reveals their hole card.
  - The dealer must hit until their hand value reaches at least 17. After reaching 17 or higher, the dealer must stand.

#### **Winning and Payouts:**

- If a player's hand value exceeds 21, they **BUST** and lose their bet.
- If a player's hand value is closer to 21 than the dealer's without busting, they win and receive a payout equal to their bet.
- If the player's hand value equals the dealer's, it's a **PUSH**, and the player's bet is returned.

[comment]: < ( - Insurance: If the dealer's upcard is an Ace, players can place an additional bet (insurance) that pays 2:1 if the dealer has a Blackjack.) >
[comment]: <- Blackjack: If a player's initial two cards are an Ace and a 10-point card (10, Jack, Queen, King), they have a Blackjack. This typically pays out at 3:2 odds.>

##### **Features that haven't been implemented yet:**

- Split: If the first two cards have the same value, the player can split them into separate hands by placing an additional bet.
- Insurance: If the dealer's upcard is an Ace, players can place an additional bet (insurance) that pays 2:1 if the dealer has a Blackjack.

- Blackjack: If a player's initial two cards are an Ace and a 10-point card (10, Jack, Queen, King), they have a Blackjack. This typically pays out at 3:2 odds.

**NOTE:** I believe using a class structure to keep all the values together would be easier, but the course has not reached classes yet. So, I am gonna continue without classes

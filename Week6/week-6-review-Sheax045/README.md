# Week 6 Review

## Assessing your Problem Solutions
The content of this week's module is less about new expression and algorithmic structures, and more about _how_ you design and build your programs. Although correctly meeting problem requirements remains part of how you will be graded, we will now also focus on how you designed the program that meets those requirements. Specifically, we will look for:

* appropriate separation of concerns
* appropriate use of function interfaces (i.e., using parameters and return values, not using variables declared as part of a script to make them accessible in all function scopes)
* comments explaining the why behind more difficult areas of code
* good function, parameter, and variable names that communicate the purpose and make the program more readable

Please keep in mind there is no single correct answer for how you design the program: there are many good approaches that are worth full credit. If you find yourself in a spiral of trying to perfectly optimize function interfaces and writing a lot of functions with a single line of code in them, you are overthinking it.

## 1 [roll_until_sum.py]
Write a program that simulates rolling two 6-sided dice, and repeatedly rolls them until a target sum is reached. A user should input what the target sum is. The program should output the result of rolling each die and the sum, finally reporting how many rolls it took to reach the target sum. For example:

```
This program rolls two 6-sided dice until their sum is a given target value.
Enter the target sum to roll for: 9

Roll: 5 and 3, sum is 8
Roll: 3 and 1, sum is 4
Roll: 4 and 1, sum is 5
Roll: 4 and 1, sum is 5
Roll: 6 and 3, sum is 9
Got it in 5 rolls!
```

## 2 [random_shapes.py]
You will write a program that generates random drawings that can be drawn using the shape painter.

The shape painter consumes a drawing file where each line corresponds to a rectangle or circle shape that is part of the drawing. A line in a drawing file has the following structures:

```
Circle; 80, 72; 15; 32, 208, 86
Rectangle; 145, 106; 421, 274; 32, 208, 205
```

The first line would draw a circle with a center point at coordinate (80, 72), a radius of 15, and a fill color with 32 for the red intensity, 208 for the green intensity, and 86 for the blue intensity. The second line would draw a rectangle with an upper left corner at coordinate (145, 106), a lower right corner at coordinate (421, 274), and a fill color with 32 for the red intensity, 208 for the green intensity, and 205 for the blue intensity.

Your goal is to create a program that generates drawing files by randomly creating these shape lines. A user should input, in this order:

* the name of the drawing file to write the shape lines out to
* the number of shapes to generate and write to the file as lines

For each line to be written into the drawing output file, your program should randomly choose:

* the shape type (Circle or Rectangle)
* the corresponding Point coordinates: currently the shape painter assumes the window size is 500 pixels wide by 500 pixels tall so you should only generate Point coordinate values that will remain within those bounds
* a fill color: you should not randomly generate each intensity color for the full range of 0 to 255. In order to make your drawings more attractive, you should use smaller ranges of intensity values, and those smaller ranges are up to you. For example, you could randomly select blue intensity values in the range 192 to 255.
* any other necessary values (e.g., the radius of a Circle).

An example interaction:

```
Enter the drawing file name to create: d3.txt
Enter the number of shapes to make: 30
```

This will write 30 shape lines to the file `d3.txt`. A sampling of five of those lines could look like:
```
Rectangle; 127, 143; 318, 332; 32, 208, 253
Circle; 302, 323; 15; 32, 208, 255
Circle; 458, 253; 47; 32, 208, 129
Circle; 80, 72; 15; 32, 208, 86
Rectangle; 145, 106; 421, 274; 32, 208, 205
```

The user should then be able to open that file with the included `shape_painter.py` program and see what the drawing looks like.

## 3 [roulette_sim.py]
You will write a program that simulates using different betting strategies in the game of roulette. In American style roulette, there is a wheel with the numbers 0 to 36 and a 00 as well. A dealer spins the wheel and then drops a ball onto the wheel where it will eventually land on one of the 38 possible numbers.

Below is the roulette betting table. Before a spin of the wheel, players can place chips in different locations to signify different types of bets. For this simulation, we're concerned with three types of bets: (1) betting on a single number (e.g., 7), (2) betting on even (even numbers from 2 to 36) or odd (odd numbers from 1 to 35), and (3) betting on a dozen numbers (i.e., 1st 12 is numbers 1 to 12, 2nd 12 is numbers 13 to 24, 3rd 12 is numbers 25 to 36). Note that for all the even/odd bets and dozen bets that if the winning number is 0 or 00 then any bet is a losing bet.

![american-roulette-table](/images/american-roulette-table.gif)

If you place a bet and do not win, then you lose the amount of money you bet. If you place a winning bet then you receive your bet back plus some payout amount times your bet. Each type of bet has its own payout schedule. For example:

* Single numbers have a 35 to 1 payout. If you place a bet of $2 on the number 7, and 7 is the winning number, you receive your $2 bet back plus $70.
* Even or odd bets have a 1 to 1 payout. If you place a bet of $2 on odd and the winning number is 7, which is an odd number, you receive your $2 bet back plus $2.
* Dozen bets have a 2 to 1 payout. If you place a bet of $2 on 1st 12 and the winning number is 7, which is in the 1st 12 numbers, you receive your $2 bet back plus $4.

Your goal is to write a program that simulates betting for some given number of roulette wheel spins using a strategy chosen by the user. The user should input, in this order:

* the number of dollars they start with
* the number of spins they will play
* the number of dollars they will bet on each spin
* their strategy choice followed by
  * Any information required for their strategy choice (e.g., the number to bet on for the single number strategy)

The program should then simulate taking a bet, spinning the wheel, determining if the player's bet is a winning bet, then paying out as appropriate. The simulation should stop when the number of desired spins is reached or out the player runs out of money (i.e., their personal bank is $0 or less).

When the simulation is complete, the program should output:

* the total number of spins, which may be less than the desired spins if the player runs out of out money to bet
* the toal wins and winning percentage
* the total losses and losing percentage
* the amount of money the player has left in their bank
* the net winnings (i.e., you started with $1000, ended with $750, thus the net winnings is -$250)

Example Simulation 1

```
Enter the number of dollars you start with: 1000
Enter the number of spins you will play: 1000
Enter how many dollars you will bet for each spin: 1
Choose one of the following strategy choices
 - Bet on a (s)ingle number (pays 35 to 1)
 - Bet on (e)ven or odd numbers (pays 1 to 1)
 - Bet on a (d)ozen numbers (pays 2 to 1)
 
Enter your strategy choice (s, e, d): d
Enter 1 to bet on numbers 1-12, 2 for numbers 13-24, or 3 for numbers 25-36: 3

After 1000 spins
Wins: 316 (31.60%)
Losses: 684 (68.40%)
Ending bank: 948
Net winnings: $-52
```

Example Simulation 2

```
Enter the number of dollars you start with: 1000
Enter the number of spins you will play: 1000
Enter how many dollars you will bet for each spin: 5
Choose one of the following strategy choices
 - Bet on a (s)ingle number (pays 35 to 1)
 - Bet on (e)ven or odd numbers (pays 1 to 1)
 - Bet on a (d)ozen numbers (pays 2 to 1)
 
Enter your strategy choice (s, e, d): s
Enter the single number you want to bet on (00 or 0 to 36): 7

After 1000 spins
Wins: 23 (2.30%)
Losses: 977 (97.70%)
Ending bank: 140
Net winnings: $-860
```

Example Simulation 3

```
Enter the number of dollars you start with: 1000
Enter the number of spins you will play: 1000
Enter how many dollars you will bet for each spin: 25
Choose one of the following strategy choices
 - Bet on a (s)ingle number (pays 35 to 1)
 - Bet on (e)ven or odd numbers (pays 1 to 1)
 - Bet on a (d)ozen numbers (pays 2 to 1)
 
Enter your strategy choice (s, e, d): e
Enter if you want to bet on (e)ven or (o)dd numbers: o

After 274 spins
Wins: 117 (42.70%)
Losses: 157 (57.30%)
Ending bank: 0
Net winnings: $-1000
``` 

Note: this assignment is not intended to endorse or otherwise encourage gambling. I would hope after running this simulation a few times you have the impression that generally, such gambling will not be in your favor.

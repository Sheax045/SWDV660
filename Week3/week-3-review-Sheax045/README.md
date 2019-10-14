# Week 3 Review

## 1 [mad-libber.py]
A mad lib is a game where you take a sentence and fill in some of the words to make a (typically) silly story. For example, you might make up a sentence `"She ate the [noun] and [past_tense_verb]."` Then someone else picks a noun and a past tense verb at random, like `"alarm clock"` and `"smiled"`, and they are put into the sentence to make `"She ate the alarm clock and smiled."` Usually the mad libs are a much longer story, but this is the general idea.

You are to create your own mad lib. Here is an example:
```
Madlib Maker
name: Paul
place: airport
verb: wait

Old Mc-Paul had a airport, E-I-E-I-O
And on that airport he liked to wait, E-I-E-I-O
With a wait wait here, and a wait wait there, everywhere a wait wait
```
I picked part of a song, and you could too, but your mad lib should:

* have at least three lines or sentences
* have at least three and no more than five replacements (in the the example there are three: name, place, and verb) 
* two of the replacements must be present in more than one sentence (e.g., in the example note how `airport` is lines 1 and 2, and `wait` is in lines 2 and 3)
* not use the concatenation operator: `+`. Why? Because although it is straightforward to do so, your solution would very likely be tedious and would not work for more than just your sentences. String methods exist to make work with Strings more efficient than that. You can solve this simply with sequences and some String methods (maybe string formatting?).

HINT: If you find yourself devising an elaborate algorithm involving programming content we have not yet covered (e.g., conditionals), you are overthinking it.



## 2 [caesar-encrypter.py, caesar-decrypter.py]
Extend the encrypter to read messages to be encrypted from an input file and write each of them out to the output file.

Currently our encrypting has the user input a message in the console. But what if we want to encrypt more than one message? We could do this by having a file with multiple messages in it: one message per line. For example, we could have `msgs.txt` file with the contents:
```
So pure of heart
And strong of mind
So true of aim with his marshmallow laser
Marshmallow laser
```
You are to modify the encrypter so that it accepts a file with multiple lines of messages as input. Your updated encrypter should prompt the user to input a file name, such as `msgs.txt`, as the input rather than just a single message. Then after having the user input the shift key and output file, it should encrypt each line of the file as a separate message, printing each encrypted message on its own line in the output file. For example, given a shift key amount of 7, and the alphabet as it is currently in the encrypter, it would produce the followingin the output file:
```
LhtinkXthYtaXTkm
ugWtlmkhgZthYtfbgW
LhtmknXthYtTbftpbmatabltfTklafTeehpteTlXk
FTklafTeehpteTlXk
```
You should not need to modify the decrypter. It should already handle having multiple encrypted messages in the file. If there are errors from the decrypter, or the messages do not appear as you expect after decrypting, then the error will be in your encryption method.



## 3 [sales-totaler.py]
Write a program that takes some sales numbers from a file written as dollars (e.g., `$1120.47`), sums them across rows, and outputs the rows again with the sum at the end. For example for an input file named `17-oct-sales.txt` with these contents:
```
$1120.47 $944.42
$72.29 $588.23
$371.21 $2183.84
```
your program would output to another file the contents:
```
$ 1120.47  $  944.42  $ 2064.89
$   72.29  $  588.23  $  660.52
$  371.21  $ 2183.84  $ 2555.05
```
Notice how in the output file all the numbers are nicely formatted with right alignment. Hint: you will probably need to use splitting, string slicing, converting data types, and string formatting.

You program should prompt a user to input a file containing the sales numbers. Then prompt the user to enter a file name for outputting the sales numbers and their totals, formatted as indicated in the example above. Here is an example interaction:
```
Enter sales file name: 17-oct-sales.txt
Enter name for total sales file: 17-oct-totals.txt

Done writing totals to 17-oct-totals.txt
```
You will find the `17-oct-sales.txt` file already included in the repository.



## 4 [dynamic-typography.py]
You will write a program that generates a drawing from a message input by the user. The message should be drawn in some way that is based on the ordinal values of the characters.

For example, the input message for the drawing below, "That was a Freebie." is drawn such that the position of the letters is based on their integer ordinal value (i.e., the `T` is higher up than the `a` because its ordinal value is smaller than `a`'s ordinal value).

![dynamic_typography](/images/dyanmic-typography.png)

What's also special about the image is the use of color and the creation of a shadow behind the letters in the message. NOTE: a shadow is not a requirement, that is just my special thing example.

Your program should:

* Prompt the user to input a message, this can be done in the console or using an Entry box with a mouse click handler
* Use the ordinal values of the characters in the input message to draw them in some unique way (i.e., we discussed how numbers are used in graphics, be creative in how you use the number of a character to make it unique such as color, position, repetitions, streaks, outlines)
* Have some color, not just black and white
* Change the typography in some way (e.g., change the size, font of the letters)
* Include comments explaining how your program is using the ordinal value to make a unique image from the message

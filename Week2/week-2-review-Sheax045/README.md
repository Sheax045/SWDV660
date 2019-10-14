# Week 2 Review

## 1 [ball_filler.py]
You have been contracted by a bowling ball manufacturer to write a program that estimates the amount of ball "filler" they will need to order for a new line of bowling balls.

Each spherical bowling ball has a diameter that can vary from 8.4 to 8.6 inches. Inside that ball there are two things: (1) a uniquely shaped metal object called the _core_ that affects the spin of the ball, and (2) stuff packed around the core making the ball's spherical shape called the _filler_. Given the intended diameter of a bowling ball, the volume of the ball's core, and the number of bowling balls to produce, your program should calculate the amount of filler the company should order.

For example, let assume a company wants to produce 100 bowling balls with a diameter of 8.5 inches. Each of these balls will contain a core that has a volume of 124 inches cubed. Then each ball will require 197.55 inches cubed of filler (i.e., the total [volume of the spherical](https://www.mathopenref.com/spherevolume.html) ball containing no core, which can be computed with the formula V=4/3πr<sup>3</sup>, minus the volume of the core). If each ball needs 197.55 inches cubed of filler, and the company is producing 100 balls, then in total they will need ~19,755 inches cubed of filler. 

You program should prompt a user to input in this order: the number of balls to manufacture, the diameter of each ball in inches, and the volume of the core in inches cubed. It should then compute and output the total amount of filler required.

Below is an example interaction with a program correctly solving this problem (recall that user inputs are in bold text):

```
How many bowling balls will be manufactured? 100
What is the diameter of each ball in inches? 8.5
What is the core volume in inches cubed? 124
You will need 19755.509806430524 inches cubed of filler
```



## 2 [total_service_score.py]
A franchise restaurant is attempting to understand if customers think their service is good day-to-day by summarizing a series of daily scores. The restaurant computes a daily score based on the number of positive comments and negative comments it receives that day. Each the score begins at 0. A positive comment adds 1 to the score, and a negative comment subtracts 1. So on a given day if there were 5 positive comments and 2 negative comments, the score for that day would be 3 (5 - 2).

Your task is to write a program that enables a restaurant manager to input these daily scores and report the total score for those days. For example, if the score on Monday is 3, Tuesday is 4, Wednesday is -2, and Thursday is 3, then the total score for those days would be 3 + 4 + (-2) + 3, which is 8. This would indicate the service is being positively reviewed over the past few days.

You program should prompt the user for how many days of scores they will be entering, and then prompt them for the score for each day. The score prompt should include the number of the day for which they entering a score (i.e., notice the `day 1` phrase in the prompt of the example below).

Once all the scores have been entered, it should then output the number total score for those days. 

Below is an example interaction with a program correctly solving this problem:

```
How many days of scores? 4
Enter score for day 1: 2
Enter score for day 2: 4
Enter score for day 3: -2
Enter score for day 4: 1
The total score of the 4 days is 5
```


## 3 [my_house.py]
In a graphics window, you are to draw an outdoor scene containing a house.

Your drawing should include at least the following shapes:
* three rectangles
* two lines
* one circle
* one text label

Your picture should not be boring black and white. It should include at least three colors, tastefully distributed to bring your house to life.

Finally, it should have some interactive feature such that when a user clicks on your picture something changes (e.g. a color changes, a tree falls over, the sun rises, a door opens). The change only has to happen once.



## 4 [gradient_bar.py]

![gradient_bar](/images/gradient_bar.png)

In the picture above you will see a gradient bar. Gradients in computer graphics typically show a color progression. The example above is a progression of the green intensity from 0 to 255, with red and blue remaining at intensity 0 through the progression, spread across six rectangles. When you see graduated colors on your computer they are often created using this technique: having thinner and thinner rectangles makes a smoother gradient progression. For example the gradient below is a green progression through 64 rectangles:


![gradient_bar_64](/images/gradient_bar_64.png)

Your task is to draw a gradient bar. You can make the color progression as simple (e.g., just green intensities changing) or sophisticated (e.g., linear equations manipulating the red, green, and blue intensities independently) as you desire. Your main requirements are this:

* The window you draw the bar in must be 400 pixels wide and the progression must be horizontal.
* There can be no gaps or overlaps in the progression: no spaces between the rectangles, no spaces from the edges of the window, no bars drawn on top of one another.
* The number of bars you use must be a multiple of 6 (i.e., 6 bars, 12 bars, 18 bars, etc.)
* The bars must have no outline (hint: setWidth method)
* All bars must have a width within one pixel of the same width. For example, if we have 6 bars in a 400-pixel window, then each bar should be 66 or 67 pixels wide. This goes along with the no overlaps constraint.

It is strongly recommend that first figure out how to draw rectangles that fill the window without gaps or overlaps. Then, if necessary, consider how you could reduce the redundancy of your work using repetition. Finally work on making the colors progress (hint: a loop variable can progress through a range of values enabling your progression).

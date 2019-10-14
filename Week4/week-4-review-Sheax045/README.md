# Week 4 Review

## 1 [golf-helper.py]
You have been contracted by a golf training company in need of a new golf club recommendation app for their clients.

Your new client is looking for an application where a user enters some information about their current golfing situation and the app replies with what club the person should use. They want to start simple first. The application should ask the user, in this order, if

* they have hit the ball on the green (answer should be `y` or `n`)
* how far they are from the hole 

If the ball is on the green, then the app should recommend using the 'Putter' club. Otherwise, if the distance is 200 yards or more, it should recommend the 'Driver', between 140 and 200 yards it should recommend the '5-Iron', between 100 and 140 yards the '9-Iron', and for any other distance it should recommend the 'Pitching Wedge'.

You are to write a program that makes those recommendations based on the user's input. You can assume the user will only enter valid values. Here are two examples:

```
Welcome to the Golf Club Helper!
Tell me your situation, and I'll recommend a club

Did you hit it on the green (y/n)? y
How far is the ball from the hole? 15

I recommend using your Putter
```
```
Welcome to the Golf Club Helper!
Tell me your situation, and I'll recommend a club

Did you hit it on the green (y/n)? n
How far is the ball from the hole? 110

I recommend using your 9-Iron
```

## 2 [cool-or-drool/cool-or-drool-rater.py]
Currently the cool or drool rater will give three possible ratings: cool, drool, or too soon to rule. We want to add a badge that goes along with these ratings: the foolie. A foolie is not a rating. It does not replace cool, drool, or too soon to rule. It is a badge additionally awarded to a movie when it is very controversial.

A movie earns the Foolie badge when it has a strongly split opinion in its ratings. The following conditions must be true to earn the Foolie:

* The total number 1 and 2 ratings must be nearly the same as the total number of 9 and 10 ratings (i.e., the totals are within 5 of each other)
* The total number of 1, 2, 9, and 10 ratings must make up more than 35% of the movie's ratings

For example, a movie has 100 ratings: 21 of them are a 1 or a 2, and 23 of them are a 9 or 10. That is a total of 44 ratings that are a 1, 2, 9 or 10. This comprises 44% of all the ratings (44/100), which is greater than 35% of the total. The movie has nearly the same total of 1 or 2 ratings (21) as it does 9 or 10 ratings (23) because the difference between the totals is 2, which is within the threshold of 5. Thus this movie would earn a Foolie badge in addition to being either cool or drool.

You are to extend the cool or drool rater program to determine if a movie qualifies for a Foolie badge. To indicate a movie has earned a Foolie badge, you should print the word 'FOOLIE' in large, colored (your choice) letters anywhere in the cool/drool/to-soon-to-rule drawing window. That badge should not appear if the movie does not earn a Foolie badge.

In order to reduce clutter in the project, you will find the `cool-or-drool-rater.py` program, and its associated images/data files in the `cool_or_drool` folder. Do not move this folder or its contents. Also in that folder, you will find a new movie rating file, `foolie_movie.csv`, which should be a movie that qualifies for a Foolie badge.

## 3 [sales-invoice-finder.py]
You are working for a computer parts manufacturer that needs a new program to find sales information based on one of two pieces of information

* an invoice identifier (id) or
* a customer's last name (lname)

Your company logs each parts sale in an Excel file saved as a CSV file called `sales_data.csv` (NOTE: if you think no company would ever do this, you are incorrect: it has been done). The first line in that file contains the column headers: textual descriptions of what data is in each column. The columns are invoice id, a customer's first name, last name, part number, quantity, and total. 

Your goal is to make this file searchable. Your program should prompt the user for the following inputs, in this order:

* Whether they want to search using an invoice id (input of `id`) or by a customer's last name (input of `lname`). The program should reject any input that is not `id` or `lname`, forcing the user to choose one of those two options.
* The search term, either an `id` value or an `lname` value

After the user enters these inputs, the program should open the data file (note that the user does not input the data file), then search within the chosen column (i.e., either `id` or `lname`, but not both) for the input value. If the program finds a match in any invoice recrords, then it it should print (not save) all recorded invoices that match. Finally it should print the total number of records found that match the search term. 

Here are three examples:
```
Search by invoice id (id) or customer last name (lname)? firstname
ERROR: You must enter either 'id' for invoice id search or 'lname' for customer last name search
Search by invoice id (id) or customer last name (lname)? lname
Enter your search term: Hutz
87681,Lionel,Hutz,218,1,50.83
34018,Lionel,Hutz,112,3,88.88
34018,Lionel,Hutz,386,3,86.04
34018,Lionel,Hutz,216,1,53.54
4 records found.
```
```
Search by invoice id (id) or customer last name (lname)? id
Enter your search term: 93303
93303,Frank,Grimes,392,2,90.74
93303,Frank,Grimes,142,3,73.2
93303,Frank,Grimes,353,1,45.87
3 records found.
```
```
Search by invoice id (id) or customer last name (lname)? lname
Enter your search term: Maryville
0 records found.
```

## 4 [polygon-tool.py]
You are to write a graphical program that enables a user to draw a polygon in a window. A polygon is a shape with a number of straight sides. For example, a triangle is 3-sided polygon: a shape with three straight sides.

We can describe a polygon as a series of points where we will draw lines between those points. For example: if we draw a line from the point (10, 10) to the point (25, 20), then a line from (25, 20) to the point (10, 30), and finally a line from (10, 30) back to the first point (10, 10), we end up with a triangle as in the example below.

![polygon_tool_triangle](/images/polygon-tool-triangle.png)

Previously we stated specific points, but it would be just as simple for a user to click on points and then draw lines between them to create a polygon drawing. Imagine now a user has a graphical window and the following occurs:

1. The user clicks on the point (10, 10), shown as `Click 1` above.
1. Then the user clicks on the point (25, 20), shown as `Click 2` above, causing a line to be drawn from the point (10, 10) to the point (25, 20).
1. Next the user clicks on the point (10, 30), shown as `Click 3` above, causing the line from (25, 20) to (10, 30) to be drawn.
1. Finally, the user in some yet unspecified way `Clicks Close` to close the Polygon, drawing a line from the last point clicked, (10, 30), to the first point clicked (10, 10). 

Creating polygons need not be limited to triangles. Polygons can have any number of sides. Here is an illustration of a user clicking to create a pentagon (5-sided polygon):

![polygon_tool_pentagon](/images/polygon-tool-pentagon.png)
You are to write a program enables a user to click points and create a polygon with any number of sides. The window the user clicks in should also contain a rectangular shape that functions as a button to close the polygon. That is, when a user clicks "inside" that rectangular shape, your program should draw the last line of the polygon from the final point that was clicked to the first point that was clicked.

To summarize, your program should

* Open up a graphical window
* When the user first clicks in the window it should draw a point
* When the user clicks on the next point, it should draw that point and a line between that new point and the first point
* It should enable the user to continue clicking on points, drawing a line between the point that the user just clicked on to the last point on which they clicked.
* Display a rectangular button (styling of your choice, text of your choice) that when clicked inside will draw the final polygon line from the last Point clicked for the polygon to the first point clicked for the polygon.

HINT: You should not need sophisticated data collections, or even the Polygon object from the graphics library, to make this work. If you think about this in terms of sequential processing, or more specifically as a sentinel/fencepost problem, it should be clearer.

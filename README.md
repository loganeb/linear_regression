# Linear Regression in Python

This project is an attempt to implement single-variable linear regression. I decided to build this project after taking Andrew Ng's free online machine learning course, located here:

https://www.coursera.org/learn/machine-learning

##Variables

The purpose of linear regression is to model relationships between a dependent variable and one or more independent variables. Stock prices were used for this project. The dependent variable (Y) is the price of Caterpillar. The single independent variable is the price of Target.

##Gradient Descent and pyplot

This program has two ultimate outputs: a PyPlot graph and a set of numbers.

The graph is used to make sure gradient descent is working properly, which means an accurate result will be produced in a reasonable amount of time.

The numerical output represents m and b in the standard formula for a line plot: y = mx + b. This formula is what would be used to model the price of Caterpillar.

It turns out that you can't really predict the price of Caterpillar using only Target's price.

##Data Sources

Stock price data was downloaded from https://finance.yahoo.com/

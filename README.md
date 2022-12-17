## Motivation
Parking violations can be a pain especially when it comes with price. Maybe you forgot to move your car when there’s street cleaning or speeding over the speed limit. In New York City, there are 100 violation codes, fines, rules, and regulations with millions of records in a given year. Wouldn’t it be nice if you could know which violations are the most common so you can avoid getting those tickets? And if you knew not just one but the top 5 most common violations, you could avoid paying tickets left and right. We as a team want to reduce the amount of parking violations given in a year in New York City. To ensure that you don’t get a violation and your driving experience is smooth of paying a fine, we need to identify the correlation between the violation code and other features. With the motivation of wanting to help you not get a violation code and to save your money, we explored the data of violation codes in New York City to help drivers like you figure out how likely it is for you to get a violation and what violations you might get in New York City. So it not only helps you as a driver but everyone in New York City! pretty neat if you ask me. 

## Data
You might be interested in the data that we are using to solve our question of, how likely is it for people in New York City to get a parking violation. We are using the parking violations issued from the year 2021 through 2022 on NYC OpenData. You might be asking why the year 2021 to 2022 and the reason is because of the pandemic! Due to the COVID-19 and the lockdown, 2021 to 2022 will be more relevant to how life is now since those years are from before COVID-19. While exploring the data we noticed that most of the data columns are more in favor of specific categories. An example is color, we chose to admit color from our exploration because the data has 265 unique colors. We cleaned the data but the time complexity to change each color to make it standardized took an enormous amount of time. Although, it was pretty interesting that the most common colors in New York City are Black, White, Gray, Red, and Brown. 

A lot of the data was skewed to one specific category; another example is violation codes where most of the codes were number 36, 21, 38, 7, 40, 71, 14, and 5. So our limitation of our data is that we don't have a lot of data to make the data evenly distributed. There are a lot of outliers within columns of the data.

36: Exceeding the posted speed limit in or near a designated school zone.
21: Street Cleaning: No parking where parking is not allowed by sign, street marking or traffic control device.
38: Parking for longer than the maximum time permitted by sign, street marking or traffic control device.
40: Stopping, standing or parking closer than 15 feet of a fire hydrant. Between sunrise and sunset, a passenger vehicle may stand alongside a fire hydrant as long as a driver remains behind the wheel and is ready to move the vehicle if required to do so.
71: Standing or parking a vehicle without showing a current New York inspection sticker.
14: General No Standing: Standing or parking where standing is not allowed by sign, street marking or; traffic control device.
5: Failure to make a right turn from a bus lane. (Violation amounts are based on violations received in a 12-month period)

It was fun exploring the data and creating the models. We were able to find the vehicle color and the vehicle type that has the most violation codes. When we plot this data we can discover interesting data and this can probably give you a hint if your vehicle is most likely to get a violation code. So if you drive a black honda you probably are more likely to get a violation code in New York City. 
The graph below shows that there’s a sharp increase in violation tickets from 8 AM - 12 PM. This could be due to the fact that people are commuting and parking their cars to go to work. This could also explain why violation codes 36, 21, 38, 7, 40, 71, 14, and 5 are the most common parking codes that are violated. They might be late for work and park in an area where parking isn’t allowed or near a fire hydrant because it’s the only parking spot left near their office! Furthermore, we see that there’s a decrease in violation tickets after 12 PM and this could be because everyone ends their day at work at different times and there’s less people commuting back home compared to the morning. Also, once everyone is home during the evening, there’s even less violation tickets. 

If we group the data frame by violation county and then get the sum of violation codes we can see that the county that has the most violation codes is Queens. If we group the data frame by the vehicle make and then get the sum of violation codes we can see that the vehicle that gets the most violation codes is a Honda. If we group the data frame by the vehicle color and then get the sum of violation codes we can see that the vehicle color that gets the most violation codes black.
So if you live in Queens and drive a black honda you might be more likely to get a ticket maybe… Let's put some models to the test! We're gonna be using random forests, decision trees, and a neural network!

## Evaluation
Decision Tree
The decision tree model is used to predict which violation codes drivers might get. The decision tree model trained on an 80 - 20 split of train and test respectively. The model was able to achieve a fairly good result of an accuracy of 68% when predicting violation codes the driver might get which you can see below. 

Although the model was able to achieve this score, I do not feel confident about its performance. The model was trained on an unevenly distributed train and test data. The model may have learned violation code 36 was the most common and assigned every prediction to violation code 36. This is because the majority of the dataset was mostly populated with this violation. Another possibility is that it learned to assign violation codes based on the time of the day. For example, violation code 36 is speeding in the school zone and violation code 21 is street cleaning. They are closely tied to time of the day as violation code 31 is more likely given out in the morning hours and violation code 21 is less likely to be given out at night.  

However, the fact that the decision model was able to should say that violators are violating the same violation code at any given time of the day.


## Neural network
We decided to do a neural network because the data set that we have has a lot of categorical data. We first have to encode the data so that it is only numbers in order to use the neural network. However, the accuracy was a little too good, it came out to be a 99% accuracy in predicting if you would get a violation code when given the data of registration state, plate state, plate type, violation code, vehicle body type, vehicle make, and violation precinct. It's good that our model has a 99% accuracy but we are not too confident that it's accurate. 


## Random Forest
We wanted to use a random forest because our data set is a large data set and random forests are usually efficient with large data. Using the random forest we wanted it to say yes or no to whether you would get a violation code or not.  It came out to a 69% accuracy given the labels I think the random forest is one that we are most confident about. Random forests have many decision trees and given that we have so much categorical data I think a 69% accuracy is pretty good. Although, same as the decision tree the data may be skewed because some of the given data are more favored to certain data. 

## Future Work
For our future work I think we would want to play with the different variables inputted into the different models to see which gives a higher accuracy on whether or not you would get a ticket. If the accuracy increases based on changing what variables we input then that variable is a feature that is more likely to get you a violation code. 

I think what would increase the accuracy of our models and data is if we use all the data sets excluding the data during the pandemic. This might have a change in results but it would be a lot to process for the model as it is a big data set.

In addition, I hope to collect and obtain more specific data that would help us better train our model and answer our question. For example, we hope to collect officers in charge, street, nearby parking signs, available parking spots, and more are all features that could help our model.

While building models to answer our question of how likely it is to get a violation in New York City, we thought about more specific questions. Some of you might want to know if your specific color is more likely to get a violation, or lets say a make of your car would lead to a violation. So with our questions we could ask other questions such as 
Does x color make it more likely to get a violation?
Does a vehicle make x, make it more likely to get a violation? 
and so on and so forth. 




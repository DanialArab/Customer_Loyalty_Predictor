<a href="http://customer-loyalty-predictor.azurewebsites.net/" target="_blank" rel="noopener">Customer Loyalty Predictor</a>


This application was developed in django and deployed in Azure. It takes several inputs from the user and then use a pre-trained logistic regression model to predict customer loyalty: to determine whether or not a customer keeps using the company's service. The 20 feaures used to train the model are as follows:

+ Customer gender
+ Marital status
+ Having dependents 
+ Monthly payment for the service 
+ ... 


The list of all other features can be found in the first page of the web application where the suer has a chance to enter their inputs. 

16 of these features can be trerated as categorical features and so one-hot encoding approach was applied to encode them. This step alog with other preprocessing steps, applied before being able to feed the data into the ML model, was incorporated in the ML pipeline (all available in the views.py file inside the myapp folder). The model accuracy vs. the applied threshold, confusuon matrix detailing Precision and Recall are summarized in the last page of the application where user will be presented with the final results.
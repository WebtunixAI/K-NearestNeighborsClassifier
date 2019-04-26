K_NEAREST-NEIGHBORS DESCRIPTION::

K-Nearest-Neighbors algorithm is used for classification and regression problems. 
In this project, it is used for classification. 
The heart_statlog  data set is bundled for test, however you are free to use any data set of your choice provided that it follows the specified format


DATA SET FORMAT::

CSV (Comma Separated Values) format. 
Attributes can be integer or real values. 
List attributes first, and add response as the last parameter in each row. 
E.g. [4.5, 7, 2.6, "Orange"], where the first 3 numbers are values of attributes and "Orange" is one of the response classes. 
Another example can be [1.2, 4.3, 3], in this case there are 2 attributes while the response class is the integer 3. 
The square brackets are shown for convenience in reading, don't put them in your CSV file. 
Responses can be integer, real or categorical. 

USING TRAIN_TEST_SPLIT::

Train dtata is in x_train,y_train
test data is in x_test , y_test
test_size=(how much data we want to test)


WORKING::

We can implement a KNN model by following the below steps:
Load the data 
Initialise the value of k 
For getting the predicted class, iterate from 1 to total number of training data points 
Calculate the distance between test data and each row of training data. Here we will use Euclidean distance as our distance metric since it’s the most popular method. The other metrics that can be used are Chebyshev, cosine, etc. 
Sort the calculated distances in ascending order based on distance values 
Get top k rows from the sorted array 
Get the most frequent class of these rows 
Return the predicted class 


NOTES::

Keep the data set files in the working directory of project as defined by the IDE configuration. 
When running in stand alone mode (E.g. command line), keep the data sets in the same directory as the script. 

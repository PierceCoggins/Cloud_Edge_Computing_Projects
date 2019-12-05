For this assignment I attempted a few different tweaks to the original lunar lander code that was provided.

Trial #1: Original Code
Using the Adam optimizer I was able to get the following baseline results. Give that this was the stock code we were given, I will look to compare future performance against these metrics.

Loss Range: 550 - 125
Total successes: 28

Trial #2: Adamax Optimizer implemented
I was able to test improved performance of the Adamax optimizer. The fundamental difference between Adam optimizer and Adamax is that the Adamax optimizer leverages the "infinite-order norm" which allows the algorithm to be much more stable and less sensitive to changes made to hyper-perameters.

Ultimately, this optimizer outperformed the relatively short training period for each of our trials and stock hyper-parameters, I think 

Loss Range: 550 - 172
Total successes were 60

Trial #3: Increasing number of layers
Finally, I attempted to build upon the improved performance of the Adamax optimizer by doubling the number of nodes in internal dense layer of the 'nnmodel' algorithm. I increased the hidden layer from 16 to 32 nodes, hoping that this would improve performance by providing additional information to the output layer.

Will update with performance metrics


Videos can be accessed here:
http://s3.us-south.cloud-object-storage.appdomain.cloud/cos-standard-00e/frame3000.mp4
http://s3.us-south.cloud-object-storage.appdomain.cloud/cos-standard-00e/frame10000.mp4
http://s3.us-south.cloud-object-storage.appdomain.cloud/cos-standard-00e/frame20000.mp4
http://s3.us-south.cloud-object-storage.appdomain.cloud/cos-standard-00e/frame30000.mp4
http://s3.us-south.cloud-object-storage.appdomain.cloud/cos-standard-00e/frame40000.mp4
http://s3.us-south.cloud-object-storage.appdomain.cloud/cos-standard-00e/frame50000.mp4

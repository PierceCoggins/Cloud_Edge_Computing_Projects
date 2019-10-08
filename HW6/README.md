1.) Detail differences in performance between P100 and V100

The V100 provided much stronger performance. While the P100 to just over 6.5 hours to train, the V100 took just under 2.5 hrs (2:29:28 exactly). Additionally, I was suprised that there was a slight difference in performance against the test data, althought this is likely due to a different random seed being generated for each instance. 

Overall, my AUC scores across the two machines were similar:

P100 AUC: 0.96653
V100 AUC: 0.96546

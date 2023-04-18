# Hirer Coding Challenge

This repository contains the code submitted as a part of an online coding assessment for a leading Australian tech company for the position of Data engineer.

The requirements are included in an offline problem statement and requires answering 12 questions about a big-data analysis using pyspark.

# Pre-reqs

 1. Docker version 20 or upwards *(tested on docker version 20 & upwards, might work on some minor versions - try it at your own risk)*
 2. Disk size of ~ 2.5 GB (this project involved downloading a big data file). While attempt is made to optimize the memory needs, this is the best attempt for a coding assessment exercise.

# Setup Instructions

 1.  Clone the project to a local workspace directory
	  `git clone https://github.com/sanjos30/hirer-coding-challenge.git`
 2.  cd to the working directory
	  `cd hirer-coding-challenge`
 3.  docker build - *this step also downloads the required test data from s3.  As a result, the build might take up-to 2-3 minutes*
	  `docker build . -t hirer-coding-challenge`
 4. docker run
	  `docker run -it hirer-coding-challenge`
 5. Alternatively, run docker build & run in one command
	 `docker build . -t hirer-coding-challenge && docker run -it hirer-coding-challenge`

Docker build step requires downloading a password protected test-data file from a public AWS S3 bucket. This step has been configured during docker build phase. 

# Developer notes

 1. There are 2 branches on this repo - dev and main. Refer to the main branch for the latest/stable version of the code.
 2. The user information is expected to be unique, while the code would allow for duplicate records too. 


##  Future optimizations

Possible improvements

 1. Load s3 data directly into spark
 2. Complete question 11 and 12
 3. Spark resource optimizations

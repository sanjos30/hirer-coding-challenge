#!/usr/bin/python

SPARK_CONFIG_PATH = "config/spark-config.json"
DATA_FILE_FOLDER_PATH = "src/data/test_data/*.json"

QUESTION_1_RAW_TEXT =   "Question:1       - Please load the dataset into a Spark dataframe. You may want to look at the data using jq or a similar tool to get an idea of how thedata is structured."
QUESTION_2_RAW_TEXT =   "Question:2       - Print the schema"
QUESTION_3_RAW_TEXT =   "Question:3       - How many records are there in the dataset?"
QUESTION_4_RAW_TEXT =   "Question:4       - What is the average salary for each profile? Display the first 10 results, ordered by lastName in descending order."
QUESTION_5_RAW_TEXT =   "Question:5       - What is the average salary across the whole dataset?"
QUESTION_6_RAW_TEXT =   "Question:6       - On average, what are the top 5 paying jobs? Bottom 5 paying jobs? If there is a tie, please order by title, location."
QUESTION_7_RAW_TEXT =   "Question:7       - Who is currently making the most money? If there is a tie, please order in lastName descending, fromDate descending."
QUESTION_8_RAW_TEXT =   "Question:8       - What was the most popular job title that started in 2019?"
QUESTION_9_RAW_TEXT =   "Question:9       - How many people are currently working?"
QUESTION_10_RAW_TEXT =  "Question:10     - For each person, list only their latest job. Display the first 10 results, ordered by lastName descending, firstName ascending order."
QUESTION_11_RAW_TEXT =  "Question:11     - For each person, list their highest paying job along with their first name, last name, salary and the year they made this salary. Store theresults in a dataframe, and then print out 10 results"
QUESTION_12_RAW_TEXT =  "Question:12     - Write out the last result (question 11) in parquet format, compressed, partitioned by the year of their highest paying job."

#!/usr/bin/python

from .helper import JOB_PYSPARK_STRUCT
from .constants import *
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as func
from pyspark.sql import types as types
from .class_seek_user import User
import os
term_size = os.get_terminal_size()

class Questions:
    """ This class abstracts all the question answers.
        get_all_answers() is invoked to print all the answers in sequence 1 - 12
    """
    
    def __init__(self, name, spark_session, data_file_path):
        self.name = name
        self.spark_session = spark_session
        self.dataframe = spark_session.read.json(data_file_path)


    # Q1 Please load the dataset into a Spark dataframe.
    def get_answer_1(self, spark_session:SparkSession):
        print(QUESTION_1_RAW_TEXT)
        print()
        print("Success: Data loaded to the dataframe.")
        print()
        print('=' * term_size.columns)


    # Q2 Print the schema.
    def get_answer_2(self):
        print(QUESTION_2_RAW_TEXT)
        print()
        self.dataframe.printSchema()
        print("Success.")
        print()
        print('=' * term_size.columns)


    # Q3 How many records are there in the dataset?
    def get_answer_3(self):
        print(QUESTION_3_RAW_TEXT)
        print()
        record_count = self.dataframe.count()
        print("Success. {} records total in the input dataset", record_count)
        print()
        print('=' * term_size.columns)


    # Q4 What is the average salary for each profile? Display the first 10 results, ordered by lastName in descending order.
    def get_answer_4(self):
        print(QUESTION_4_RAW_TEXT)
        # use user-defined function (udf) to calculate the avg salary
        user_average_salary_udf = func.udf(lambda user_entry: User(user_entry).get_average_salary(), types.FloatType())

        df_with_avg_salary = self.dataframe.withColumn("average_salary", user_average_salary_udf(self.dataframe["profile"]))
        # sort by last name as desc
        df_with_avg_salary.sort(func.desc("profile.lastName")).show(10)
        print()
        print('=' * term_size.columns)

    # Q5 What is the average salary across the whole dataset?
    def get_answer_5(self):
        print(QUESTION_5_RAW_TEXT)
        #create a dataframe for user jobs
        df_explode_userjobs = self.dataframe.select("id", "profile.firstName", "profile.lastName", func.explode("profile.jobHistory").alias("jobHistory"))

        # to avoid doing this in question 6
        self.df_explode_userjobs = df_explode_userjobs

        rs_average_salary = df_explode_userjobs.select(func.avg("jobHistory.salary").alias("average_salary")).collect()
        input_dataset_avg_salary = rs_average_salary[0]["average_salary"]
        print("Average salary is ", input_dataset_avg_salary)
        print()
        print('=' * term_size.columns)


    # Q6 On average, what are the top 5 paying jobs? Bottom 5 paying jobs? If there is a tie, please order by title, location.
    def get_answer_6(self):
        print(QUESTION_6_RAW_TEXT)

        # Sort the DataFrame by salary and title/location in ascending order
        df_ordered_jobs = self.df_explode_userjobs.groupby("jobHistory.title", "jobHistory.location").agg(func.round(
            func.avg("jobHistory.salary"),2).alias("avg_job_salary")
        )

        top_jobs_df = df_ordered_jobs.sort(func.desc("avg_job_salary"), func.desc("jobHistory.title"), func.desc("jobHistory.location"))
        top_jobs_df.show(5)

        bottom_jobs_df = df_ordered_jobs.sort(func.asc("avg_job_salary"), func.desc("jobHistory.title"), func.desc("jobHistory.location") )
        bottom_jobs_df.show(5)

        print()
        print('=' * term_size.columns)


    # Q7 Who is currently making the most money? If there is a tie, please order in lastName descending, fromDate descending.
    def get_answer_7(self):
        print(QUESTION_7_RAW_TEXT)

        # udf to calculate current salary
        udf_get_current_salary = func.udf(lambda u: User(u).get_current_salary(), types.IntegerType())
        udf_get_current_from_date = func.udf(lambda d: User(d).get_current_from_date(), types.DateType())

        # new df with current_salary view
        df_with_current_salary = self.dataframe.select(
            "profile.firstName",
            "profile.lastName",
            udf_get_current_salary(func.col("profile")).alias("cur_salary"),
            udf_get_current_from_date(func.col("profile")).alias("current_job_since")
        )

        df_with_current_salary.sort(
            func.desc("cur_salary"),
            func.desc("lastName"),
            func.desc("current_job_since")
        ).show(15)
        print()
        print('=' * term_size.columns)       

    # Q8 What was the most popular job title that started in 2019?"
    def get_answer_8(self):
        print(QUESTION_8_RAW_TEXT)

        df_jobs_since_2019 = self.df_explode_userjobs.filter(func.year(func.col("jobHistory.fromDate")) == 2019)
        df_job_count_since_2019 = df_jobs_since_2019.groupby(
            "jobHistory.title"
        ).count()
        df_job_count_since_2019.sort(
            func.desc("count")
        ).show(1)
        print()
        print('=' * term_size.columns)


    # Q9 How many people are currently working?
    def get_answer_9(self):
        print(QUESTION_9_RAW_TEXT)  
        udf_is_currently_working = func.udf(
            lambda x: User(x).is_currently_working(), types.BooleanType()
        )
        currently_working_df = self.dataframe.select(
            udf_is_currently_working(func.col("profile")).alias("is_currently_working")
        ).filter(
            func.col("is_currently_working")
        )
        print(f"{currently_working_df.count()} currently working.")
        print()
        print('=' * term_size.columns)    


   # Q10 For each person, list only their latest job. Display the first 10 results, ordered by lastName descending, firstName ascending order
    def get_answer_10(self):
        print(QUESTION_10_RAW_TEXT)
        udf_get_current_job = func.udf(lambda u: User(u).get_current_job(), JOB_PYSPARK_STRUCT)
        current_jobs_df = self.dataframe.select(
            "profile.firstName",
            "profile.lastName",
            udf_get_current_job(func.col("profile")).alias("current_job"),
        )
        current_jobs_df.select(
            "firstName",
            "lastName",
            "current_job.*",
        ).sort(
            func.desc("lastName"),
            func.asc("firstName")
        ).show(10)
        print()
        print('=' * term_size.columns)  

   # Q11 For each person, list their highest paying job along with their first name, last name, salary and the year they made this salary. Store theresults in a dataframe, and then print out 10 results
    def get_answer_11(self):
        print(QUESTION_11_RAW_TEXT)

        print("...........NOT COMPLETED.......")

        print()
        print('=' * term_size.columns)  
   

    # Q12 Write out the last result (question 11) in parquet format, compressed, partitioned by the year of their highest paying job.
    def get_answer_12(self):
        print(QUESTION_12_RAW_TEXT)

        print("...........NOT COMPLETED.......")

        print()
        print('=' * term_size.columns)  

    
    def get_all_answers(self, spark_session:SparkSession):
        """ This method prints answers to all the questions in sequence
        """
        self.get_answer_1(spark_session)

        self.get_answer_2()

        self.get_answer_3()

        self.get_answer_4()

        self.get_answer_5()

        self.get_answer_6()

        self.get_answer_7()

        self.get_answer_8()

        self.get_answer_9()

        self.get_answer_10()

        # Not completed
        self.get_answer_11()

        # Not completed
        self.get_answer_12()


        
# Blockbuster-Evolution-Project

Blockbuster Evolution Project
Hey Learners! Welcome to Project 1: Blockbuster Evolution Project! 🍿🎬

Movies are more than just entertainment - they are a massive global business. Every year, thousands of films are released, competing for audience attention and box-office success.
Chef is a huge movie enthusiast and has collected historical box-office data of movies released over the last 40 years. He wants to answer big questions:

Which studios dominate the market?
How has the industry grown financially over decades?
What are the short-term revenue trends?
Chef needs your help to analyze this dataset. Your task is to use the Pandas library to clean, analyze, and extract meaningful insights.

What’s Already Provided
You are given a single file: main.py

All required function names are already defined.
The program flow is already set up.
You only need to complete the missing logic using the Pandas Library.
Do NOT change function names or print statements.
Dataset
In this Project, you will work with a CSV file: movies.csv

This dataset contains 40 years of movie data.
Columns:
name → Movie title
released → Full release date string (e.g., "June 13, 1980")
Note: Needs parsing into a proper Date object.
gross → Total Box-Office Revenue ($)
If missing (NaN), revenue data is unavailable.
company → Production Company / Studio Name
rating → MPAA Rating (e.g., R, PG, PG-13)
genre → Movie Genre (e.g., Action, Drama)
country → Country of origin
Dataset Preview (First 5 rows):
name,rating,genre,released,country,gross,company
The Shining,R,Drama,"June 13, 1980",United Kingdom,46998772.0,Warner Bros.
The Blue Lagoon,R,Adventure,"July 2, 1980",United States,58853106.0,Columbia Pictures
Star Wars: Episode V - The Empire Strikes Back,PG,Action,"June 20, 1980",United States,538375067.0,Lucasfilm
Airplane!,PG,Comedy,"July 2, 1980",United States,83453539.0,Paramount Pictures
Caddyshack,R,Comedy,"July 25, 1980",United States,39846344.0,Orion Pictures
Tasks
Load Dataset
Inside load_flight_data(filename):
Load the CSV file into a Pandas DataFrame.
Docs: pandas.read_csv()
Clean the Data
Inside clean_data(df):
Step 1: Convert the released column to datetime objects.
Step 2: Remove rows where gross revenue is NaN (Missing).
Docs: dropna | pandas.to_datetime()
Optimize Memory
Inside optimize_memory(df):
Text columns like rating ("PG", "R") and genre ("Action", "Comedy") repeat thousands of times. Storing them as simple text strings wastes RAM.
Task: Convert the following columns to the category data type:
"rating", "genre", "country", "company"
Docs: Pandas Categorical Data
Rank Production Studios
Inside rank_studios(df):
Who are the giants of the industry?
Step 1: Group movies by company and sum their gross revenue.
Note: Use observed=True in your groupby to handle the categorical data cleanly.
Step 2: Rank the studios based on total revenue.
The highest earner gets Rank 1.
Use method='min' (if two studios tie for 1st place, they both get Rank 1).
Step 3: Combine the data into a new DataFrame.
Columns should be: "Total_Gross" and "Rank".
Sort the result by Rank (Ascending order).
Docs: groupby | rank
Industry Growth (Expanding Sum)
Inside calculate_industry_growth(df):
Chef wants to see the "All-Time Cumulative Revenue" of the film industry grow over the years.
Step 1: Sort the data by released date. (Time-series data must be sorted).
Step 2: Calculate the Expanding Sum of the gross column.
Store this in a new column called "cumulative_industry_gross".
Example:
Movie A: 
10
(
T
o
t
a
l
:
10(Total:10)
Movie B: 
20
(
T
o
t
a
l
:
20(Total:30)
Movie C: 
15
(
T
o
t
a
l
:
15(Total:45)
Step 3: Return a DataFrame with only these columns:
"released", "name", "gross", "cumulative_industry_gross"
Docs: DataFrame.expanding().sum()
Trend Analysis (Rolling Average)
Inside analyze_recent_trends(df):
Box office numbers are volatile. One massive hit is followed by three flops. We need to smooth the line.
Step 1: Sort by released date.
Step 2: Calculate the 3-Movie Rolling Average for gross.
Store this in a new column called "rolling_avg_3_movies".
Step 3: Fill the first two NaN values with 0.
Step 4: Return a DataFrame with only these columns:
"released", "name", "gross", "rolling_avg_3_movies"
Docs: rolling()
Expected Output:

### Blockbuster Evolution Project ###

1. Data Loaded Successfully.

2. Top 5 Companies by Total Gross:
                        Total Gross  Rank
company                                  
Universal Pictures     1.643803e+10   1.0
Paramount Pictures     1.480054e+10   2.0
Warner Bros.           1.389824e+10   3.0
Twentieth Century Fox  1.233287e+10   4.0
Columbia Pictures      9.153184e+09   5.0

3. Industry Growth (First 5 Entries):
     released                        name       gross  cumulative_industry_gross
81 1980-01-18                     Windows   2128395.0                  2128395.0
74 1980-01-18  Just Tell Me What You Want   2086905.0                  4215300.0
65 1980-02-01                       Fatso   7653061.0                 11868361.0
29 1980-02-01             American Gigolo  22743674.0                 34612035.0
18 1980-02-08                     The Fog  21448782.0                 56060817.0

4. Recent Trends (First 10 Entries):
     released                          name       gross  rolling_avg_3_movies
81 1980-01-18                       Windows   2128395.0          0.000000e+00
74 1980-01-18    Just Tell Me What You Want   2086905.0          0.000000e+00
65 1980-02-01                         Fatso   7653061.0          3.956120e+06
29 1980-02-01               American Gigolo  22743674.0          1.082788e+07
18 1980-02-08                       The Fog  21448782.0          1.728184e+07
69 1980-02-08                 Hero at Large  15934737.0          2.004240e+07
20 1980-02-15                      Cruising  19814523.0          1.906601e+07
39 1980-03-07         Coal Miner's Daughter  67182787.0          3.431068e+07
83 1980-03-19  The King and the Mockingbird    167451.0          2.905492e+07
26 1980-03-21               Little Darlings  34326249.0          3.389216e+07


import pandas as pd


# 1. Load Dataset
def load_dataset(filepath):
    """
    Load the CSV file and handle file not found errors.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return pd.DataFrame()


# 2. Clean Data (Date Parsing & Removing Empty Rows)
def clean_data(df):
    """
    Parse the complex date format and remove rows with missing gross revenue.
    """
    # Step 1: Copy the dataframe to avoid modifying the original
    df_clean = df.copy()
    
    # Step 2: Parse 'released' column to datetime
    df_clean['released'] = pd.to_datetime(df_clean['released'])

    # Step 3: Remove rows where 'gross' is NaN
    df_clean = df_clean.dropna(subset=['gross'])
    
    # Step 4: Return cleaned dataframe
    return df_clean


# 3. Optimize Memory
def optimize_memory(df):
    """
    Convert string columns with repeated values to 'category' type to save RAM.
    """
    # Copy the dataframe
    df_optimized = df.copy()
    
    # List of columns that are good candidates for categorical conversion
    # These have few unique values compared to the total number of rows
    categorical_cols = ['rating', 'genre', 'country']
    
    for col in categorical_cols:
        # Check if column exists before converting
        if col in df_optimized.columns:
            df_optimized[col] = df_optimized[col].astype('category')
            
    # Returning optimized dataframe
    return df_optimized


# 2. Studio Ranking (Grouped Ranking)
def rank_studios(df):
    """
    Rank production companies by their total gross revenue.
    """
    # Step 1: Group data by Company and sum up the Gross revenue
    studio_gross = df.groupby('company', observed=True)['gross'].sum()
    
    # Concept: Ranking
    # method='min' handles ties (e.g., two companies with equal gross get the same rank).
    ranks = studio_gross.rank(ascending=False, method='min')
    
    # Combine into a clean table
    ranking_table = pd.DataFrame({
        'Total_Gross': studio_gross,
        'Rank': ranks
    }).sort_values('Rank')
    
    return ranking_table


# 3. Industry Growth (Expanding Sums)
def calculate_industry_growth(df):
    """
    Calculate the cumulative gross revenue over time.
    """
    # Step 1: Sort by release date (Essential for time-series calculations)
    df_sorted = df.sort_values('released').copy()
    
    # Concept: Expanding Sum
    # Calculates a running total of gross revenue from 1980 to present.
    df_sorted['cumulative_industry_gross'] = df_sorted['gross'].expanding().sum()
    
    return df_sorted[['released', 'name', 'gross', 'cumulative_industry_gross']]


# 4. Trend Analysis (Rolling Windows)
def analyze_recent_trends(df):
    """
    Calculate the '3-Movie Rolling Average' of Gross Revenue.
    """
    df_sorted = df.sort_values('released').copy()
    
    # Concept: Rolling Window
    # Averages the Gross of the current movie + previous 2 movies.
    # .fillna(0) ensures the first 2 rows (which don't have enough history) show 0 instead of NaN.
    df_sorted['rolling_avg_3_movies'] = (
        df_sorted['gross']
        .rolling(window=3)
        .mean()
        .fillna(0)
    )
    
    return df_sorted[['released', 'name', 'gross', 'rolling_avg_3_movies']]


if __name__ == "__main__":
    print("### Blockbuster Evolution Project ###")
    
    # 1. Load
    df_raw = load_dataset("movies.csv")
    
    if not df_raw.empty:
        # 2. Clean
        df_clean = clean_data(df_raw)
        
        # 3. Optimize
        df = optimize_memory(df_clean)
    
        # Check if we still have data after cleaning (e.g. dropping NaNs)
        if not df.empty:
            print(f"\n1. Data Loaded Successfully.")
            
            # 2. Rankings
            print("\n2. Top 5 Companies by Total Gross:")
            print(rank_studios(df).head())
            
            # 3. Cumulative Growth
            print("\n3. Industry Growth (First 5 Entries):")
            print(calculate_industry_growth(df).head())
            
            # 4. Rolling Trends
            print("\n4. Recent Trends (First 10 Entries):")
            print(analyze_recent_trends(df).head(10))
        else:
            print("Error: Dataframe is empty after cleaning.")
    else:
        print("Error: 'movies.csv' not found.")



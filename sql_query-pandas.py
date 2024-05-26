# pip install pandas #
# pip install duckdb #
import pandas as pd
import duckdb

df = pd.DataFrame({'id': [1, 2, 3],
                   'amount': [50, 30, 100],
                   'has_item': [True, False, False]})

duckdb.query("SELECT SUM(amount) FROM df").to_df()
"""
    sum(amount)
0           180.0
"""

duckdb.query("SELECT amount FROM df WHERE has_item=False").to_df()
"""
    amount
0       30
1       100
"""

duckdb.query("SELECT category, count(*) FROM df GROUP BY category").to_df()
"""
    category    count_star()
0           A               2
1           B               1
"""

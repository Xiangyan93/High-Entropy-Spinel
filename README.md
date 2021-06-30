# High Entropy Spinel
A database and machine learning model for high entropy spinel.

## Database
Database Creation, data import and export.
   1. Create the database.
        ```
        python create.py
        ```
   2. Import experimental data.
        ```
        python import.py --input data/sample1.csv --property Stabilized
        python import.py --input data/sample2.csv --property Stabilized
        python import.py --input data/sample3.csv --property Stabilized --remark KS
        python import.py --input data/sample4.csv --property T20
        ```
   3. Export experimental data
        ```
        python export.py --property Stabilized
        ```
   4. Active Learning
        ```
        python3 active_learning.py --n_samples 5
        ```
## Machine Learning
See [notebook](https://github.com/Xiangyan93/High-Entropy-Spinel/tree/master/notebook).
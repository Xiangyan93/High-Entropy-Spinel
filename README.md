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
        python import.py --input data/case2/5.csv --property Stabilized
        python import.py --input data/case2/6.csv --property Stabilized
        python import.py --input data/case2/7.csv --property Stabilized
        python import.py --input data/case2/8.csv --property Stabilized
        python import.py --input data/case2/9.csv --property Stabilized
        python import.py --input data/case2/10.csv --property Stabilized
        python import.py --input data/case2/catalyst.csv --property T90
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
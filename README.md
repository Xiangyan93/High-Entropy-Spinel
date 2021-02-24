# High Entropy Spinel
A database and machine learning model for high entropy spinel.

## Database
Database Creation, data import and export.
   1. Create the database.
        ```
        python3 database/db_create.py
        ```
   2. Import experimental data.
        ```
        python3 database/import_data.py -i datasets/sample1.txt --property Stabilized
        python3 database/import_data.py -i datasets/sample2.txt --property Stabilized
        python3 database/import_data.py -i datasets/sample3.txt --property Stabilized --remark KS
        ```
   3. Export experimental data
        ```
        python3 database/export_data.py --property Stabilized
        ```

## Machine Learning
See [notebook](https://github.com/Xiangyan93/HighEntropySpinel/tree/main/notebook).
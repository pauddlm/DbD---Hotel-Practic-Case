from adapters import SQLiteAdapter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
all_users_data = None
all_users_csv_data = None
# Retrieve info from SQLite table and export it to a CSV
query= """ 
SELECT
    dh.hotel,
    SUM(dh.adults) + SUM(dh.children) AS total_guests,
    SUM(CASE WHEN dh.children = 0 THEN dh.adults ELSE 0 END) AS couple,
    SUM(CASE WHEN dh.children = 0 THEN dh.adults ELSE 0 END)/2 AS number_of_couples,
    SUM(CASE WHEN dh.children > 0 THEN dh.adults + dh.children ELSE 0 END) AS family,
    COUNT(CASE WHEN dh.children > 0 THEN 1 END) AS number_of_families
FROM
    dim_users du
JOIN
    dim_hotels dh ON du.user_id = dh.user_id
GROUP BY
    dh.hotel;
"""

results = SQLiteAdapter.select(query)

#Export the query to a CSV file
csv_filename = "CoupleFamilies.csv"
with open(csv_filename, "w") as csv_file:
    # Write CSV headers
    csv_file.write("hotel,total_guests,couple_guests, number_couples, family_guests, number_families\n")
    # Write CSV results
    for row in results:
        csv_file.write(f"{row[0]},{row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}\n")

import sqlite3
import pandas as pd

def run_sql_analysis(csv_path="dataset_part_2.csv", db_path="spacex.db"):
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql("SPACEXTBL", conn, if_exists="replace", index=False)

    queries = {
        "ccafs_slc_40_count": "SELECT COUNT(*) AS n FROM SPACEXTBL WHERE LaunchSite='CCAFS SLC 40';",
        "success_rate": "SELECT ROUND(AVG(Class)*100,1) AS success_rate FROM SPACEXTBL;",
        "gto_count": "SELECT COUNT(*) AS n FROM SPACEXTBL WHERE Orbit='GTO';",
        "true_asds_count": "SELECT COUNT(*) AS n FROM SPACEXTBL WHERE Outcome='True ASDS';"
    }

    for name, query in queries.items():
        print("\n", name)
        print(pd.read_sql_query(query, conn))

    conn.close()

if __name__ == "__main__":
    run_sql_analysis()

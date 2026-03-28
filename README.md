# SpaceX Falcon 9 First Stage Landing Prediction

This repository support package contains a working CSV and Python scripts for a capstone-style report submission.

## Files
- `dataset_part_2.csv` - working launch table
- `spacex_api_collection.py` - API-style collection entry point
- `spacex_web_scraping.py` - web-scraping support script
- `data_wrangling.py` - cleaning, feature preparation, train/test split
- `eda_visualization.py` - charts for EDA
- `eda_sql.py` - SQL queries using SQLite
- `folium_map_analysis.py` - launch-site map generation
- `dash_app.py` - simple dashboard
- `predictive_analysis.py` - baseline classification models

## Quick start
```bash
pip install pandas numpy scikit-learn matplotlib folium dash plotly
python eda_visualization.py
python eda_sql.py
python predictive_analysis.py
```

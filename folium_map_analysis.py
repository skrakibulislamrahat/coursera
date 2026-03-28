import pandas as pd
import folium

def create_launch_map(csv_path="dataset_part_2.csv", out_html="spacex_launch_sites_map.html"):
    df = pd.read_csv(csv_path)
    site_df = df.groupby("LaunchSite")[["Latitude","Longitude"]].first().reset_index()

    m = folium.Map(location=[29.5, -95], zoom_start=4)
    for _, row in site_df.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=row["LaunchSite"]
        ).add_to(m)

    m.save(out_html)
    print(f"Saved {out_html}")

if __name__ == "__main__":
    create_launch_map()

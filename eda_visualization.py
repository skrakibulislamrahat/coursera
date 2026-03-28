import pandas as pd
import matplotlib.pyplot as plt

def run_eda(csv_path="dataset_part_2.csv"):
    df = pd.read_csv(csv_path)
    df["Year"] = pd.to_datetime(df["Date"]).dt.year

    site_counts = df["LaunchSite"].value_counts()
    orbit_counts = df["Orbit"].value_counts()
    success_by_year = df.groupby("Year")["Class"].mean() * 100
    success_by_site = df.groupby("LaunchSite")["Class"].mean() * 100

    print("Site counts:\n", site_counts)
    print("Orbit counts:\n", orbit_counts.head(10))
    print("Success by year:\n", success_by_year)
    print("Success by site:\n", success_by_site)

    plt.figure(figsize=(6,4))
    site_counts.plot(kind="bar")
    plt.title("Launches by Site")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("launches_by_site.png", dpi=200)

    plt.figure(figsize=(6,4))
    orbit_counts.plot(kind="bar")
    plt.title("Orbit Distribution")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("orbit_distribution.png", dpi=200)

    plt.figure(figsize=(6,4))
    success_by_year.plot(marker="o")
    plt.title("Landing Success Rate Over Time")
    plt.ylabel("Success Rate (%)")
    plt.tight_layout()
    plt.savefig("success_rate_over_time.png", dpi=200)

if __name__ == "__main__":
    run_eda()

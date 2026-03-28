import pandas as pd

def build_scraped_context(csv_path="dataset_part_2.csv"):
    """
    Placeholder web-scraping support file for the capstone repo.
    In a full project this would use requests + BeautifulSoup against the
    Falcon 9 launch list page. Here it derives a lightweight contextual table.
    """
    df = pd.read_csv(csv_path)
    scraped = df[["FlightNumber","Date","BoosterVersion","PayloadMass","Orbit","LaunchSite","Outcome"]].copy()
    scraped["MissionTitle"] = "Falcon 9 Mission " + scraped["FlightNumber"].astype(str)
    scraped["PageTitle"] = "List of Falcon 9 and Falcon Heavy launches - Wikipedia"
    print(scraped.head())
    return scraped

if __name__ == "__main__":
    build_scraped_context().to_csv("spacex_web_scrape_context.csv", index=False)

from etl import load_data, analyze_data
from visuals import create_dashboard

if __name__ == "__main__":
    FILENAME = 'sprzedaz_rowery_2024.csv'
    
    try:
        raw_df = load_data(FILENAME)
        metrics, man_df, type_df, city_df, time_df = analyze_data(raw_df)
        create_dashboard(metrics, man_df, type_df, city_df, time_df)
        
    except Exception as e:
        print(f"Wystąpił błąd podczas pracy programu: {e}")
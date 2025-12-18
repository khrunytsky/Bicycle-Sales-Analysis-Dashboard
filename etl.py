import pandas as pd
import os

# 1.ŁADOWANIE DANYCH(EXTRACT)
def load_data(filename: str) -> pd.DataFrame:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Nie znaleziono pliku: {filename}")
    
    df = pd.read_csv(filename, sep=';', encoding='utf-8-sig')
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    return df

# 2. ANALIZA DANYCH(TRANSFORM)
def analyze_data(df: pd.DataFrame):
    
    kpi = {
        'total_orders': len(df),
        'total_sell': df['selling_price'].sum(),
        'total_margin': df['margin'].sum(),
        'avg_margin_pct': (df['margin'].sum() / df['selling_price'].sum()) * 100
    }
    
    # Agregacja: Zysk wg producenta
    df_man = df.groupby('manufacturer')['margin'].sum().reset_index()
    df_man.columns = ['Producent', 'Zysk']
    
    # Agregacja: Zysk wg typu roweru
    df_type = df.groupby('type')['margin'].sum().reset_index()
    df_type.columns = ['Typ', 'Zysk']
    
    # Agregacja: Top 10 miast
    df_city = df.groupby('city')['margin'].sum().reset_index()
    df_city.columns = ['Miasto', 'Zysk']
    
    # Agregacja: Oś czasu (Zysk miesięczny)
    df_timeline = df.resample('ME', on='date')['margin'].sum().reset_index()
    df_timeline['Miesiąc'] = df_timeline['date'].dt.strftime('%B') # Nazwy miesięcy
    df_timeline.columns = ['Data', 'Zysk', 'Miesiąc']
    
    return kpi, df_man, df_type, df_city, df_timeline
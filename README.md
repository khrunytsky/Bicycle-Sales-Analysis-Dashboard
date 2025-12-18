# 🚲 Bicycle Sales Analysis Dashboard 2024

Projekt przedstawia proces ETL (Extract, Transform, Load) oraz wizualizację danych sprzedażowych sklepu rowerowego. 
Aplikacja przetwarza dane z pliku CSV i generuje dashboard analityczny.

## 🛠️ Struktura Projektu

* **`main.py`**: Główny plik uruchomieniowy.
* **`etl.py`**: Moduł wczytywania i analizy danych.
* **`visuals.py`**: Moduł generujący dashboard.
* **`requirements.txt`**: Lista niezbędnych bibliotek.

## 📊 Analiza Biznesowa

Program automatyzuje wyliczanie:
* Kluczowych metryk.
* Trendów zysku w ujęciu miesięcznym.
* Udziału kategorii produktów w zysku.
* Rankingu producentów i lokalizacji.

## 📂 Wyniki

Po zakończeniu analizy program automatycznie tworzy folder `reports/`, w którym zapisuje gotowy wykres:
* **`reports/dashboard_sprzedazy.png`** – kompletny dashboard gotowy do wstawienia do prezentacji lub wysłania mailem.

## 🚀 Uruchomienie

1. **Przygotuj dane**: Upewnij się, że plik `sprzedaz_rowery_2024.csv` znajduje się w głównym folderze projektu.
2. **Zainstaluj biblioteki**: `pip install -r requirements.txt`
3. **Uruchom program**: `python main.py`
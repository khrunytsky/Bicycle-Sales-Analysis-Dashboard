import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import os
# 3. WIZUALIZACJA (LOAD / DASHBOARD
def create_dashboard(kpi, df_man, df_type, df_city, df_timeline):
    
    # Ustawienie stylu Dashboardu (2x2)
    fig, axes = plt.subplots(2, 2, figsize=(24, 12), constrained_layout=True)
    fig.suptitle('RAPORT ANALITYCZNY: SPRZEDAŻ ROWERÓW 2024', fontsize=28, fontweight='bold', color='#333333')

    # 1: Zysk w czasie (Liniowy)
    ax1 = axes[0, 0]
    ax1.plot(df_timeline['Miesiąc'], df_timeline['Zysk'], marker='o', linewidth=4, color='mediumpurple', markersize=10)
    ax1.fill_between(df_timeline['Miesiąc'], df_timeline['Zysk'], color='mediumpurple', alpha=0.2)
    ax1.set_title('Dynamika zysku w ujęciu miesięcznym', fontsize=18, pad=10)
    ax1.grid(axis='y', linestyle='--', alpha=0.7)

    # 2: Udział Typu w Zysku (Kołowy)
    ax2 = axes[0, 1]
    df_type_sorted = df_type.sort_values('Zysk', ascending=False)
    colors_pie = ['mediumpurple'] + list(cm.Greys(np.linspace(0.7, 0.3, len(df_type_sorted)-1)))
    ax2.pie(df_type_sorted['Zysk'], labels=df_type_sorted['Typ'], autopct='%1.1f%%', 
            startangle=90, colors=colors_pie, explode=[0.05] + [0]*(len(df_type_sorted)-1),
            textprops={'fontsize': 12})
    ax2.set_title('Udział zysku według kategorii produktu', fontsize=18, pad=10)

    # 3: Zysk wg Producenta (Słupkowy Poziomy)
    ax3 = axes[1, 0]
    df_man_plot = df_man.sort_values('Zysk', ascending=True)
    ax3.barh(df_man_plot['Producent'], df_man_plot['Zysk'], color=list(cm.Greys(np.linspace(0.3, 0.7, len(df_man_plot)-1)))+ ['mediumpurple'])
    ax3.set_title('Ranking zysku według producentów', fontsize=18, pad=10)
    ax3.set_xlabel('Zysk (PLN)', fontsize=12)

    # 4: Top 10 Miast (Słupkowy Pionowy)
    ax4 = axes[1, 1]
    df_city_top = df_city.sort_values('Zysk', ascending=True).head(10)
    colors_bars = list(cm.Greys(np.linspace(0.3, 0.7, 9))) + ['mediumpurple']
    ax4.bar(df_city_top['Miasto'], df_city_top['Zysk'], color=colors_bars)
    ax4.set_title('Top 10 Miast', fontsize=18, pad=10)
    ax4.tick_params(axis='x', rotation=30)
    ax4.set_ylabel('Zysk (PLN)', fontsize=12)

    # RAMKA: METRYKI WYNIKÓW (Performance Metrics)
    info_text = (f"METRYKI WYNIKÓW:\n"
                 f"• Liczba zamówień: {kpi['total_orders']}\n"
                 f"• Zysk całkowity: {kpi['total_margin']:,.2f} PLN\n"
                 f"• Średnia marża: {kpi['avg_margin_pct']:.2f}%")
    
    # Pozycjonowanie ramki z metrykami
    fig.text(0.51, 0.52, info_text, fontsize=15, color='white', fontweight='bold',
             bbox=dict(facecolor='mediumpurple', alpha=0.9, edgecolor='none', boxstyle='round,pad=1'))

    # Zapisywanie raportu
    if not os.path.exists('reports'):
        os.makedirs('reports')
    plt.savefig('reports/dashboard_sprzedazy.png', dpi=300, bbox_inches='tight')
    
    print("Analiza zakończona sukcesem. Dashboard zapisano w folderze 'reports/'.")
    plt.show()

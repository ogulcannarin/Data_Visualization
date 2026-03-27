import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create outputs/gallery directory if it doesn't exist
os.makedirs('outputs/gallery', exist_ok=True)

# 1. Veriyi yükle
df = pd.read_csv('player_stats.csv', encoding='latin-1', low_memory=False)

# Style
sns.set_theme(style="whitegrid")

# 1. Correlation Heatmap
cols = ['age', 'ball_control', 'dribbling', 'marking', 'slide_tackle', 'height', 'weight']
plt.figure(figsize=(10, 8))
sns.heatmap(df[cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Özellikler Arasındaki Korelasyon Analizi')
plt.tight_layout()
plt.savefig('outputs/gallery/01_correlation_heatmap.png')
plt.close()

# 2. Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='ball_control', y='dribbling', hue='age', palette='viridis', alpha=0.6)
plt.title('Ball Control vs Dribbling (Yaş Gruplarına Göre)')
plt.tight_layout()
plt.savefig('outputs/gallery/02_scatter_age_hue.png')
plt.close()

# 3. Joint Plot (Hex)
g = sns.jointplot(data=df, x='height', y='weight', kind='hex', color='#4CB391')
g.fig.suptitle('Boy ve Kilo İlişkisi (Hexbin)', y=1.02)
plt.savefig('outputs/gallery/03_joint_plot_hex.png')
plt.close()

# 4. Violin Plot
top_ages = df['age'].value_counts().head(10).index
df_filtered = df[df['age'].isin(top_ages)]
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_filtered, x='age', y='ball_control', palette='muted')
plt.title('Yaşlara Göre Ball Control Dağılımı')
plt.tight_layout()
plt.savefig('outputs/gallery/04_violin_distribution.png')
plt.close()

# 5. Count Plot
plt.figure(figsize=(10, 5))
sns.countplot(data=df_filtered, x='age', palette='magma')
plt.title('Yaş Dağılımı (Oyuncu Sayısı)')
plt.tight_layout()
plt.savefig('outputs/gallery/05_count_plot_age.png')
plt.close()

# 6. Regression (Lmplot)
g = sns.lmplot(data=df, x='ball_control', y='dribbling', hue='age', palette='magma', height=6)
plt.title('Yetenek İlişkisi ve Regresyon')
plt.savefig('outputs/gallery/06_regression_analysis.png')
plt.close()

# 7. Pair Plot
small_cols = ['age', 'ball_control', 'dribbling']
g = sns.pairplot(df[small_cols], hue='age', palette='husl')
g.fig.suptitle('Değişken İlişki Matrisi', y=1.02)
plt.savefig('outputs/gallery/07_pair_plot_matrix.png')
plt.close()

# 8. Facet Grid
g = sns.FacetGrid(df_filtered, col="age", height=4)
g.map(sns.histplot, "ball_control", color="teal", kde=True)
plt.tight_layout()
plt.savefig('outputs/gallery/08_facet_grid_age.png')
plt.close()

# 9. Bar Plot (Categorical)
top_nations = df['country'].value_counts().head(5).index
df_nations = df[df['country'].isin(top_nations)]
plt.figure(figsize=(10, 6))
sns.barplot(data=df_nations, x='country', y='ball_control', palette='viridis')
plt.title('Ülkelere Göre Ortalama Yetenek')
plt.tight_layout()
plt.savefig('outputs/gallery/09_bar_plot.png')
plt.close()

# 10. Point Plot (Trend)
plt.figure(figsize=(10, 6))
sns.pointplot(data=df_filtered, x='age', y='ball_control', color='red')
plt.title('Yaşa Bağlı Yetenek Değişim Trendi')
plt.tight_layout()
plt.savefig('outputs/gallery/10_point_plot.png')
plt.close()

# 11. FacetGrid (Histograms)
g = sns.FacetGrid(df_filtered, col="age", height=4)
g.map(sns.histplot, "ball_control", color="teal", kde=True)
plt.tight_layout()
plt.savefig('outputs/gallery/11_facet_grid.png')
plt.close()

# 12. KDE Density Plot
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='ball_control', y='dribbling', fill=True, cmap='Purples')
plt.title('Yetenek Yoğunluk Analizi (KDE)')
plt.tight_layout()
plt.savefig('outputs/gallery/12_density_kde.png')
plt.close()

# 13. Pivot Heatmap
subset = df[df['country'].isin(df['country'].value_counts().head(5).index)]
pivot_table = subset.pivot_table(index='country', columns='age', values='ball_control', aggfunc='mean').fillna(0)
plt.figure(figsize=(14, 6))
sns.heatmap(pivot_table, cmap='YlGnBu')
plt.title('Ülke ve Yaşa Göre Yetenek Matrisi')
plt.tight_layout()
plt.savefig('outputs/gallery/13_pivot_heatmap.png')
plt.close()

# 14. Annotation
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='age', y='ball_control', alpha=0.3, color='gray')
top_player = df.loc[df['ball_control'].idxmax()]
plt.annotate(f"Zirve: {top_player['player']}", 
             xy=(top_player['age'], top_player['ball_control']), 
             xytext=(top_player['age'] + 4, top_player['ball_control'] - 10),
             arrowprops=dict(facecolor='red', shrink=0.05))
plt.title('Özel İşaretleme: En İyi Oyuncu')
plt.tight_layout()
plt.savefig('outputs/gallery/14_annotation.png')
plt.close()

# 15. Cluster Map
# Small subset for cluster map to be readable
cluster_cols = ['ball_control', 'dribbling', 'marking', 'slide_tackle']
sns.clustermap(df[cluster_cols].corr().fillna(0), annot=True, cmap='coolwarm')
plt.savefig('outputs/gallery/15_cluster_map.png')
plt.close()

print("Tüm 15 görsel başarıyla oluşturuldu!")

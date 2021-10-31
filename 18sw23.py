import pandas as pd
import json
import matplotlib.pyplot as plt

%matplotlib inline
cards_df = pd.read_csv('dokkan_cards.csv')
pettan_df = pd.read_csv('pettan_cards.csv')
cards_df.head()
pettan_df.head()
cards_df['Transformation Type'].value_counts()
cards_df['Rarity'].value_counts()
cards_df['HP'].dropna().apply(json.loads)
temp_df = cards_df[cards_df.T.apply(lambda x: str(x['ID'])[0] != '4')]
temp_df = temp_df[temp_df['Rarity'].isin(['UR', 'LR'])]
hp = temp_df['HP'].dropna().apply(lambda x: json.loads(x.replace("'", '"'))[-1]).astype(int)
attack = temp_df['Attack'].dropna().apply(lambda x: json.loads(x.replace("'", '"'))[-1]).astype(int)
defense = temp_df['Defense'].dropna().apply(lambda x: json.loads(x.replace("'", '"'))[-1]).astype(int)

plt.scatter(x=attack, y=hp, c=defense / defense.max())
plt.xticks([attack.min(), attack.max()])
plt.yticks([hp.min(), hp.max()])
plt.suptitle('Character Stats - Rainbowed at Max Level')
plt.title('Color = Defense')
plt.xlabel('Attack')
plt.ylabel('HP');

pettan_df['Series'].value_counts()
pd.DataFrame(pettan_df.groupby('Series')['Rarity'].value_counts()).unstack('Series')
import pandas as pd
import numpy as np
from tqdm import tqdm

df = pd.read_csv('dataset_spb.csv')

df.drop_duplicates(subset = 'name',inplace = True)

df.drop(columns=['Unnamed: 0','Unnamed: 0.1','id','uri','track_number'],inplace=True)

feature=df.columns.to_list()
feature.remove('album')
feature.remove('name')

X = df[feature]

y = df.drop(columns=feature)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().fit(X)
X = scaler.transform(X)
X = pd.DataFrame(X,columns= feature)

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

k=range(3,20)
sse=[]
for i in k:
    km=KMeans(n_clusters=i)
    km.fit(X)
    sse.append(km.inertia_)
km = KMeans(n_clusters=8)
clusters=km.fit_predict(X)
df['cat']=clusters



class SpotifyRecommender():
    def __init__(self, rec_data):
        #our class should understand which data to work with
        self.rec_data_ = rec_data
    
    #if we need to change data
    def change_data(self, rec_data):
        self.rec_data_ = rec_data
    
    #function which returns recommendations, we can also choose the amount of songs to be recommended
    def get_recommendations(self, song_name, amount=1):
        distances = []
        #choosing the data for our song
        song = self.rec_data_[(self.rec_data_.name.str.lower() == song_name.lower())].head(1).values[0]
        #dropping the data with our song
        res_data = self.rec_data_[self.rec_data_.name.str.lower() != song_name.lower()]
        for r_song in tqdm(res_data.values):
            dist = 0
            for col in np.arange(len(res_data.columns)):
                #indeces of non-numerical columns
                if not col in [0,1]:
                    #calculating the manhettan distances for each numerical feature
                    dist = dist + np.absolute(float(song[col]) - float(r_song[col]))
            distances.append(dist)
        res_data['distance'] = distances
        #sorting our data to be ascending by 'distance' feature
        res_data = res_data.sort_values('distance')
        columns = ['name']
        return res_data[columns][:amount]

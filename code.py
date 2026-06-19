# import the libraries
import pandas as pd
import matplotlib.pyplot as plt


#load dataset
df=pd.read_csv("netflix_titles.csv")
print(df.head())

#clean data
df=df.dropna(subset=["title","type","director","cast","country"])
type_counts=df["type"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title('Movies Vs tv_shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()


rating_counts=df["rating"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index,autopct="%1.1f%%",startangle=90)
plt.title('Percentage of content ratings')
plt.tight_layout()
plt.savefig('content_ratings.png')
plt.show()

movie_df=df[df["type"]=="Movie"].copy()
movie_df["duration"]==movie_df["duration"].str.replace("min","").astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df["duration"],bins=20,color="purple",edgecolor="black")
plt.title("Distribution of movie duration")
plt.xlabel('Duration')
plt.ylabel('No.of movies')
plt.tight_layout()
plt.savefig('duration.png')
plt.show()

release_counts=df["release_year"].value_counts().sort_index()
plt.figure(figsize=(8,6))
plt.scatter(release_counts.index,release_counts.values,color="red")
plt.title("Release year Vs no.of shows")
plt.xlabel('Release Year')
plt.ylabel('No.of shows')
plt.tight_layout()
plt.savefig('release.png')
plt.show()


country_counts=df["country"].value_counts().head()
plt.figure(figsize=(8,6))
plt.barh(country_counts.index,country_counts.values,color="teal")
plt.title("Top 10 countries")
plt.xlabel('No. of shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('country.png')
plt.show()

content_by_year=df.groupby(["release_year","type"]).size().unstack().fillna(0)
fig,ax=plt.subplots(1,2,figsize=(12,5))

#first subplot
ax[0].plot(content_by_year.index,content_by_year["Movie"],color="blue")
ax[0].set_title("Movies released per year")
ax[0].set_xlabel("year")
ax[0].set_ylabel("no.of movies")

#second subplot
ax[1].plot(content_by_year.index,content_by_year["TV Show"],color="orange")
ax[1].set_title("TV shows released per year")
ax[1].set_xlabel("year")
ax[1].set_ylabel("no.of shows")

fig.suptitle("Comparison of movies and TV shows released over years")
plt.tight_layout() 
plt.show()

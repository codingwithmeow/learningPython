import pandas as pd

df = pd.read_csv("datasets/youtube_ing.csv")

#1 - Bring the first 10 records.
result = df.head(10)

# 2- Bring the second 5 records.
result = df[5:20].head(5)

# 3- Find the column names and number in the Dataset.
result = df.columns
result = len(df.columns)

# 4- Delete some columns below and list the remaining columns.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)

# 5- Find the average of likes and dislikes.
result = df["likes"].mean()
result = df["dislikes"].mean()
# 6- Bring the like and dislike columns of the first 50 videos.
result = df.head(50)[["title","likes","dislikes"]]

#7- What is the most viewed video?
result = df[df["views"].max() == df["views"]]["title"].iloc[0]

#8- What is the lowest viewed video?
result = df[df["views"].min() == df["views"]]["title"].iloc[0]

#9- What are the top 10 most viewed videos?
result = df.sort_values("views", ascending=False).head(10)[["title","views"]]

# 10- Bring the average of likes according to the category in order.
result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# 11- Sort the number of comments by category from top to bottom.
result = df.groupby("category_id").sum().sort_values("comment_count", ascending = False)["comment_count"]

#12- How many videos are there in each category?
result = df["category_id"].value_counts()

# 13- Show the title length of each video in a new column.
df["title_len"] = df["title"].apply(len)

# 14- Show the number of tags used for each video in the new column.
def tagCount(tag):
    return len(tag.split('|'))

df["tag_count"] = df["tags"].apply(tagCount)

# 15- List the most popular videos (by like/dislike ratio)
def likedislikeoranhesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))

    oranListesi = []

    for like,dislike  in liste: 
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["beğeni_orani"] = likedislikeoranhesapla(df)

print(df.sort_values("beğeni_orani",ascending=False)[["title","likes","dislikes","beğeni_orani"]])
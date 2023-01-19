from youtube_data_api3 import YouTubeDataAPI
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

# API key for the YouTube Data API
api_key = "YOUR_API_KEY"

# Initialize the YouTubeDataAPI object
youtube = YouTubeDataAPI(api_key)

# Get the ID of the YouTube video from the user
video_id = input("Enter the ID of the YouTube video: ")

# Initialize an empty dataframe
df = pd.DataFrame(columns=['comment', 'sentiment'])

# Get the comments of the video in chunks
for comments in youtube.get_video_comments(video_id, chunksize=50):
    for comment in comments:
        # Analyze the sentiment of the comment
        sentiment = TextBlob(comment).sentiment.polarity
        if sentiment > 0:
            sentiment_text = "Positive"
        elif sentiment == 0:
            sentiment_text = "Neutral"
        else:
            sentiment_text = "Negative"

        # Append the comment and sentiment to the dataframe
        df = df.append({'comment': comment, 'sentiment': sentiment_text}, ignore_index=True)

# Export the dataframe to a csv file
df.to_csv('comments.csv', index=False)

# Read the csv file into a dataframe
df = pd.read_csv('comments.csv')

# Count the number of comments for each sentiment
sentiment_count = df.groupby('sentiment').count()['comment']

# Create a bar chart of the sentiment distribution
sentiment_count.plot.bar()

# Add a title and labels to the chart
plt.title('Sentiment Distribution of YouTube Comments')
plt.xlabel('Sentiment')
plt.ylabel('Number of Comments')

# Display the chart
plt.show()

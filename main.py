from tts.executeModel import create_synthesizer, generate_speech
from reddit.reddit import connect_reddit, get_hot_posts

syn = create_synthesizer()
headers = connect_reddit()
posts_df = get_hot_posts(headers)

for index, row in posts_df.iloc[1:].iterrows():
    print(f"Go: {index}")
    title = row[1]
    post_text = row[2]
    
    generate_speech(syn, title + "\n" + post_text, title)
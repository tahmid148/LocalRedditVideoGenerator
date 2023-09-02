from tts.executeModel import create_synthesizer, generate_speech
from reddit.reddit import connect_reddit, get_hot_posts
from utils.CustomStream import CustomStream
import sys, re, datetime

# Specify the file name where you want to save the output
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"log-{current_time}.txt"

# Create or open the output file for writing
with open(output_file, "w") as file:
    custom_stream = CustomStream(file, sys.stdout)

    # Redirect stdout to the custom stream
    sys.stdout = custom_stream

    syn = create_synthesizer()
    headers = connect_reddit()
    posts_df = get_hot_posts(headers)

    for index, row in posts_df.iloc[22:].iterrows():
        title = row[1]
        post_text = row[2]

        # Replace "AITA" with "Am I the asshole" in both title and post_text
        title = title.replace("AITA", "Am I the asshole")
        post_text = post_text.replace("AITA", "Am I the asshole")
        post_text = post_text.replace("(", ",")
        post_text = post_text.replace(")", ",")
        
        generate_speech(syn, title + "\n" + post_text, re.sub(r'[^a-zA-Z0-9\s]', '', title))

# Restore stdout to its original state
sys.stdout = sys.__stdout__

print("Output saved to:", output_file)

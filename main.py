from tts.executeModel import create_synthesizer, generate_speech
from reddit.reddit import connect_reddit, get_hot_posts, get_post
from utils.CustomStream import CustomStream
import sys, re, datetime

# Specify the file name where you want to save the output
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"output/log-{current_time}.txt"

reddit = connect_reddit()

def generate_hot_posts(no_of_posts):
    posts = get_hot_posts(reddit, "AmITheAsshole", no_of_posts)
    syn = create_synthesizer()


    for index, submission in enumerate(posts):
        print(f"Progress: {index + 1} / {no_of_posts}")
        title = submission.title
        post_text = submission.selftext
        
        print(title)
        print("\n")
        print(post_text)
    
        # Replace "AITA" with "Am I the asshole" in both title and post_text
        title = title.replace("AITA", "Am I the asshole")
        post_text = post_text.replace("AITA", "Am I the asshole")
        post_text = post_text.replace("(", ",")
        post_text = post_text.replace(")", ",")
        post_text = re.sub(r'(\d+)([mfMF])', lambda match: ', ' + match.group(1) + (' Male,' if match.group(2).lower() == 'm' else ' Female,'), post_text)
        post_text = re.sub(r'([mfMF])(\d+)', lambda match: (', Female ' if match.group(1).lower() == 'f' else ', Male ') + match.group(2) + ",", post_text)
        
        generate_speech(syn, title + "\n" + post_text, re.sub(r'[^a-zA-Z0-9\s]', '', title))

def generate_from_post(id):
    submission = get_post(reddit, id)
    print(submission.title)
    

def main():
    generate_from_post("15vlv9g")

if __name__ == "__main__":
    with open(output_file, "w") as file:
        custom_stream = CustomStream(file, sys.stdout)
        # Redirect stdout to the custom stream
        sys.stdout = custom_stream
        main()
    # Restore stdout to its original state
    sys.stdout = sys.__stdout__
    print("Output saved to:", output_file)
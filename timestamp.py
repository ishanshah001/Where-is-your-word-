from youtube_transcript_api import YouTubeTranscriptApi

# url = "https://youtu.be/nk2CQITm_eo"
url = input("Enter url: ")

# video id is the last 11 characters of the url
video_id = url[-11:]

# word = "say"
word = input("Enter word to be searched: ")
word = word.lower()

# returns a list of dictionaries, each containing the text, start timestamp and the duration of that text
dict = YouTubeTranscriptApi.get_transcript(video_id)

timestamp = []
generate_links = []
for i in dict:
    if word in i["text"].lower():
        timestamp.append(i["start"])

if len(timestamp) > 0:
    print("Found " + word + str(len(timestamp)) + "times.")
    for time in timestamp:
        str_time = str(time)
        generate_links.append(url + "&t=" + str_time.split(".")[0] + "s")

    for links in generate_links:
        print(links)
else:
    print("Couldn't find the word")
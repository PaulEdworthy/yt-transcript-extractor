from youtube_transcript_api import YouTubeTranscriptApi

# test link (short video)
# video_id = 'YcyIAOUcK6U'

# Peter Attia with Andy Galpin
video_id = 'UA5z1lAn2mc'

transcript_list = []

transcripts = YouTubeTranscriptApi.get_transcript(video_id)

for transcript in transcripts:
    # time_stamp = 
    temp = (transcript['text'])
    temp.replace('\n', ' ')
    # transcript_list.append(transcript['text'])

    with open('output_text', 'a') as op:
        op.write(temp + '\n')

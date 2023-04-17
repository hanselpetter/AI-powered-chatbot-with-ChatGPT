import os
import json
import openai
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from flask import (Flask, jsonify, request, abort, render_template, logging)

# Define OpenAI API key 
openai.api_key = os.environ["OPENAI_API_KEY"]

########################################## Home Page ################################################
app = Flask(__name__)
@app.route("/")
def home():
    """Serve homepage template."""
    return render_template("index.html")

#####################################################################################################

######################################### ChatGPT Bot ###############################################
# chatGPT Function
# Redirect to the chatbot UI
@app.route("/gpt1", methods = ['GET', 'POST'])
def _turbo1():
    return render_template("gpt.html")

# Redirect to the API call
@app.route("/gpt", methods = ['GET', 'POST'])
# Function
def _turbo():
    u_input = request.args.get('u_input') if request.method == 'GET' else request.form['u_input']
    messages = [{"role": "user", "content": u_input}]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        content = response.choices[0].message["content"]
    except:
        content = "AI Failed! Please try again at a later time."

    # Return API call result
    return jsonify(content=content)

#####################################################################################################

######################################### YouTube Downloader ########################################
# Youtube Downloader
@app.route("/download", methods = ['GET', 'POST'])
def downloader():
    return render_template("download.html")

#####################################################################################################

########################################## Sample ###################################################
# Page 3
@app.route("/p3", methods = ['GET', 'POST'])
def page3():
    return ("Coming Soon!!!")

#####################################################################################################

##################################### Youtube Transcribe ############################################
# HomePage for youtube transcript
@app.route("/transcript", methods = ['GET', 'POST'])
def transcript():
    return render_template('transcript.html')

@app.route('/transcript1', methods=['GET', 'POST'])
def transcript1():
    video_url = request.form['video_url']
    try:
                # download the video
        yt = YouTube(video_url)
        video_path = yt.streams.get_audio_only().download()

        # extract the transcript
        transcript_list = YouTubeTranscriptApi.get_transcript(yt.video_id)

        # format the transcript with timestamps
        transcript = []
        for line in transcript_list:
            timestamp = line['start']
            text = line['text']
            transcript.append({'timestamp': timestamp, 'text': text})
      
        # display the transcript
        return render_template('transcript1.html', transcript=transcript)
    
    except: 
        return render_template('error.html')
##################################################################################################

if __name__ == "__main__":
    # Use 'debug=True' to avoid resarting vs code 
    # everytime there is an update in the code.
    app.run(debug=True)

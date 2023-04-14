'''
    Sources:
    https://www.codegpt.co/docs/tutorial-basics/installation
    https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
    https://blog.devgenius.io/chatgpt-how-to-use-it-with-python-5d729ac34c0d
    https://www.youtube.com/watch?v=w-X_EQ2Xva4
    https://github.com/AIAdvantage/chatgpt-api-youtube/blob/main/02%20chatgpt%20chat%20assistant%20copy.py

'''
import os
import openai
from flask import (Flask, jsonify, request, abort, render_template, logging)
from flask import render_template
from flask import request

# Define OpenAI API key 
openai.api_key = os.environ["OPENAI_API_KEY"]

app = Flask(__name__)
@app.route("/")
def home():
    """Serve homepage template."""
    return render_template("index.html")

# chatGPT Function
@app.route("/gpt", methods = ['POST', 'GET'])
# Function
def _turbo():
    messages = []
    _chatbot = input("Enter the ChatBot type you want to create: ")
    messages.append({"role": "system", "content": _chatbot})

    print("\nThe ChatBot is ready, you can start!")
    
    # Click quit() to quit the while loop
    while input != "quit()":
        message = input("\nEnter your request: ")
        messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        try:
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
        except:
            reply = "AI failed ... "
     
        return render_template("gpt.html", reply = reply)


# Youtube Downloader
@app.route("/download", methods = ['POST', 'GET'])
def downloader():
    return ("Under Construction!!!")

if __name__ == "__main__":
    # Use 'debug=True' to avoid resarting vs code 
    # everytime there is an update in the code.
    app.run(debug=True)

from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/download_reel', methods=['GET'])
def download_reel():
    # get the Instagram reel URL from the request parameters
    url = request.args.get('url')
    print(url)
    if not url:
        return "Invalid URLL"
    # make a GET request to the URL and get the response content
    if not url.startswith('https://www.instagram.com/reel/'):
        return "Invalid URL"
    response = requests.get(url).content.decode('utf-8')


    # make a GET request to the video URL and get the video content
    video_content = requests.get(url).content

    # save the video content to a file
    with open('downloaded_reel.mp4', 'wb') as f:
        f.write(video_content)

    # return a JSON response indicating success
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)

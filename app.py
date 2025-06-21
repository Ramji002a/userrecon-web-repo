
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

platforms = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Pinterest": "https://www.pinterest.com/{}"
}

def check_user_exists(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except:
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lookup')
def lookup():
    username = request.args.get('username')
    results = []

    for platform, base_url in platforms.items():
        profile_url = base_url.format(username)
        found = check_user_exists(profile_url)
        results.append({
            'platform': platform,
            'status': found,
            'link': profile_url
        })

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)

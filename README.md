# Shrek.fm

A lightweight Python script that monitors your Last.fm scrobbles and updates your Discord profile with a **Now Playing** Rich Presence status in real time.

## How It Works

The script polls Last.fm every 60 seconds. If you're actively scrobbling a track, it pushes that info to your local Discord client as a Rich Presence status. When you stop playing, it clears the status automatically.

## Requirements

- Python 3.7+
- Discord desktop app running locally
- A [Last.fm account](https://www.last.fm) with scrobbling set up

## Setup

### 1. Clone the repo

\`\`\`bash
git clone https://github.com/yourusername/shrek.fm.git
cd shrek.fm
\`\`\`

### 2. Install dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Get your Last.fm API key

1. Go to [last.fm/api/account/create](https://www.last.fm/api/account/create)
2. Fill in the form (app name, description — anything works)
3. Copy your **API Key**

### 4. Configure

Copy the example config and fill in your credentials:

\`\`\`bash
cp config.example.json config.json
\`\`\`

Edit `config.json`:

\`\`\`json
{
  "lastfm_api_key": "your_lastfm_api_key",
  "lastfm_username": "your_lastfm_username",
  "discord_client_id": "1495842422133882982"
}
\`\`\`

> ⚠️ `config.json` is listed in `.gitignore` and will not be committed. Never share your API keys publicly.

### 5. Run it

\`\`\`bash
python shrek_fm.py
\`\`\`

Keep the script running in the background while you listen. Your Discord profile will update automatically.

## Notes

- Discord must be open and running on the same machine as the script
- Rich Presence is only visible to other Discord users — not in your own profile view
- The presence clears automatically when you stop scrobbling

## Dependencies

- [pypresence](https://github.com/qwertyquerty/pypresence)
- [requests](https://docs.python-requests.org)

## License

MIT
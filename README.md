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

```bash
git clone https://github.com/DexterClaire/shrek.fm.git
cd shrek.fm
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure

Copy the example config and set your Last.fm username:

```bash
cp config.example.json config.json
```

Edit `config.json` and replace `your_lastfm_username` with your Last.fm username. The API key and Discord client ID are pre-filled and ready to go.

> If you'd prefer to use your own Last.fm API key, you can create one at [last.fm/api/account/create](https://www.last.fm/api/account/create).

### 4. Run it

```bash
python shrek_fm.py
```

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

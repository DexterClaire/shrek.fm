import requests
import time
import json
from pypresence import Presence

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

LASTFM_API_KEY = config["lastfm_api_key"]
LASTFM_USER = config["lastfm_username"]
DISCORD_CLIENT_ID = config["discord_client_id"]
POLL_INTERVAL = config.get("poll_interval", 60)

def get_now_playing():
    try:
        response = requests.get(
            "http://ws.audioscrobbler.com/2.0/",
            params={
                "method": "user.getRecentTracks",
                "user": LASTFM_USER,
                "api_key": LASTFM_API_KEY,
                "limit": 1,
                "format": "json"
            },
            timeout=10
        )
        data = response.json()
        track = data["recenttracks"]["track"][0]

        # Only return if actively now playing
        if "@attr" in track and track["@attr"].get("nowplaying") == "true":
            return {
                "title": track["name"],
                "artist": track["artist"]["#text"],
                "album": track["album"]["#text"]
            }
        return None

    except Exception as e:
        print(f"[Last.fm] Error fetching track: {e}")
        return None

def main():
    print("Starting Last.fm → Discord Rich Presence...")

    presence = None
    current_track = None

    while True:
        if presence is None:
            try:
                presence = Presence(DISCORD_CLIENT_ID)
                presence.connect()
                print("Connected to Discord.")
            except Exception:
                print("[Discord] Not available, retrying...")
                presence = None
                time.sleep(POLL_INTERVAL)
                continue

        track = get_now_playing()

        try:
            if track:
                track_key = (track["title"], track["artist"])
                if track_key != current_track:
                    print(f"[Now Playing] {track['title']} — {track['artist']}")
                    presence.update(
                        details=track["title"].ljust(2),
                        state=track["artist"].ljust(2),
                        large_image="shrek",
                        large_text=track["album"] or "Unknown Album",
                        start=int(time.time())
                    )
                    current_track = track_key
            else:
                if current_track is not None:
                    print("[Stopped] Clearing presence.")
                    presence.clear()
                    current_track = None
        except Exception as e:
            print(f"[Discord] Lost connection: {e}")
            presence = None
            current_track = None

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
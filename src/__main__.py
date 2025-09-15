import webview
import os
import subprocess
import time
import urllib.request as request
from discordrp import Presence
from pathlib import Path

def main():
    fileLocation = Path(os.path.dirname(__file__))
    gameDataPath = fileLocation / Path("data/laingame.com")
    clientID = "1413625921394442280"
    if not os.path.exists(gameDataPath):
        print("Installing game data...")
        request.urlretrieve("https://laingame.net/offline/laingame.com", gameDataPath)
        print("Complete, window should open now!")

    subprocess.Popen(["start", "/wait", "/B", gameDataPath], shell=True)
    # ^ /wait and /b are needed to not create a window and to terminate the server
    # on the death of the main process
        
    with Presence(clientID) as presence:
        presence.set(
            {
                "state": "In the Wired",
                "details": "Playing Serial Experiments Lain",
                "timestamps": {"start": int(time.time())},
            }
        )

        webview.create_window("< game >", "http://localhost:8080/#/game", fullscreen=True)
        webview.start()

if __name__ == "__main__":
    main()
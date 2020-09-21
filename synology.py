import configparser
import os

class Synology():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config["internal"] = {}
        self.config["internal"]["conf_file"] = "/etc/synologyUpdater"
        self.config["internal"]["keys"]      = "['emailPort','emailUser','emailHost','emailSender','emailPassword',emailDestination','synologyPort','synologyIP','synologyUser','synologyPassowrd'"
        
        syncPath = os.getcwd() + "syng.json"
        print(syncPath)
    
    
    
if __name__ == "__main__":
    Synology()
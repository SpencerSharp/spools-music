import re, os
import data
from runner import RunnerDaemon
from dataitem import MappableItem
import spotify
class CLIRunnerDaemon(RunnerDaemon):
    def __init__(self):
        super().__init__(self.run_message)

    def run_message(self, message):
        if is_cmd(message):
            run_cmd(message)

def is_cmd(msg):
    return re.match('^music.*',msg)

def run_cmd(cmd):
    print(cmd)
    if cmd == 'music save':
        data.save_tables()
    elif cmd == 'music':
        print(data.tables)
    else:
        item = MappableItem(cmd,'user').item
        if '-d' in cmd:
            spotify.unpause_player()
        print(item.__dict__)
        item.save()
        data.save_tables()
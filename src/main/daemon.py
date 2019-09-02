import signal, os
import file
import ipc, filesys
class Daemon(object):
    def get_input_file(self):
        return type(self).__name__

    def get_desc_file(self):
        return '.'+type(self).__name__

    def __init__(self, signal, run):
        self.file = self.get_input_file()
        self.run = run
        self.signal = signal
        
        if not ipc.check_if_process_exists(self):
            if ipc.create_process(self.get_desc_file(), self.critical):
                ipc.set_handler(self, self.catch, signal)
                self.sleep()

    def critical(self):
        filesys.write(self.get_desc_file(), str(os.getpid())+'\n0', overwrite=True)

    def catch(self):
        messages = self.read_messages()
        self.run(messages)

    def sleep(self):
        signal.pause()

    def read_messages(self):
        return filesys.read(self.file, overwrite=True, splitlines=True)
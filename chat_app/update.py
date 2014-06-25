import threading
import time
from  chat_app.store import *
class Update(threading.Thread):
    def __init__(self, vector):
        threading.Thread.__init__(self)
        self.time = 60
        self.vector = vector
    def run(self):
        store = Store()
        while self.time!=0:
            print self.time
            print self.vector
            time.sleep(1)
            self.time = self.time - 1
            if self.time == 0:
                store.save_data(self.vector)
                self.time = 60
                self.vector = []
    def get_vector(self):
        return self.vector

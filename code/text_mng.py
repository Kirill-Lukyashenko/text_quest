import time

from settings import DELAY

class text_manager():

    def __init__(self) -> None:
        pass

    def load_script(self, path):
        with open(path, "r", encoding='UTF-8') as file:
            return file.read().split(';\n')

    def show_text_by_id(self,script,id):
        try:
            for i in script[id]:
                print(i, end = '', flush= True)
                time.sleep(DELAY)
        except:
            print(script[len(script)-2])
from settings import FILE_PATH as path
from text_mng import text_manager

         
text = text_manager()

script_arr = text.load_script(path)

start = False

if __name__ == "__main__":
    start = True
id = 1
while start:
    text.show_text_by_id(script_arr, id)
    command = str(input('   ваш ответ ->'))
    if command != '  ':
        id += 1
    else:
        id == 1
    if command == 'exit' or id > len(script_arr)-2:
        start = False 


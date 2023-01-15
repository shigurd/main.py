import os

def get_json_list(input_dir, out_text):
    file_list = []
    with open(out_text, 'w', encoding='utf-8', errors='replace') as text_file:
        for fname in os.listdir(input_dir):

            if fname.rsplit('.', 1)[-1] == 'json':
                file_list.append(fname)

        text_file.write(f'{file_list}')

def get_json_and_image_list(input_dir, out_text):
    file_list = []
    with open(out_text, 'w', encoding='utf-8', errors='replace') as text_file:
        for fname in os.listdir(input_dir):

            if fname.rsplit('.', 1)[-1] == 'json' or fname.rsplit('.', 1)[-1] == 'png':
                file_list.append(f"('{fname}', '.')")
        for f in file_list:
            text_file.write(f'{f}, ')


if __name__ =='__main__':
    input_dir = '.'
    #get_json_list(input_dir, 'json_list.txt')
    get_json_and_image_list(input_dir, 'pyinstaller_list.txt')
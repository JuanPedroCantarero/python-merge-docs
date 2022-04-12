import sys
import cmd
import os.path
import PySimpleGUI as sg

outputPath = './output/data.csv'

class EVENTS_KEY():
    FOLDER = 'FOLDER',
    MERGE = 'MERGE',
    FILE_LIST = 'FILE_LIST'
    CLOSE = 'CLOSE'




def merge_two_csv_files_with_same_lanes(path, firstFile, secondFile):
    fileone_to_merge = ''
    filetwo_to_merge = ''
    with open(path + firstFile, 'r') as t1, open(path + secondFile , 'r') as t2:
        fileone_to_merge = t1.readlines()
        filetwo_to_merge = t2.readlines()
    with open(outputPath, 'w') as outFile:
        for line in filetwo_to_merge:
            if line in fileone_to_merge:
                outFile.write(line)

def make_window():
    description = '''Este programa permite mezclar los dos primeros csv de una carpeta respecto a las lineas que tienen iguales,
dando como resultado un csv con las lineas coincidentes'''
    layout = [
        [sg.Text(description)],
        [sg.Text('Csv Folder'), sg.In(size=(60, 1), enable_events=True, disabled=True, key=EVENTS_KEY.FOLDER), sg.FolderBrowse()],
        [sg.Button('Mezclar archivos', key=EVENTS_KEY.MERGE, disabled=True)],
        [sg.Listbox(values=[], enable_events=True, size=(80, 20), key=EVENTS_KEY.FILE_LIST)]
    ]
    window = sg.Window('Mezclador csv', layout).Finalize()
    fnames = []
    folder = ''
    while True:
        event, values = window.read()
        
        if event == EVENTS_KEY.CLOSE or event == sg.WIN_CLOSED:
            break
        elif event == EVENTS_KEY.FOLDER:
            window[EVENTS_KEY.MERGE].update(disabled=True)
            folder = values[EVENTS_KEY.FOLDER]
            fnames = get_file_and_folder(folder)
            if len(fnames) == 2:
                window[EVENTS_KEY.MERGE].update(disabled=False)
            window[EVENTS_KEY.FILE_LIST].update(fnames)
        elif event == EVENTS_KEY.MERGE:
            merge_two_csv_files_with_same_lanes(folder + '/', fnames[0], fnames[1])
            fnames = []
            folder = ''
            window[EVENTS_KEY.FOLDER].update(folder)
            window[EVENTS_KEY.FILE_LIST].update(fnames)
            window[EVENTS_KEY.MERGE].update(disabled=True)
            success_window('El csv se ha mezldo con éxito, mire dentro de la carpeta output para ver el resultado')
            

    window.close()

def success_window(msg):
    success_layout = [  
        [sg.Text(msg)],
        [sg.Button('Cerrar', key=EVENTS_KEY.CLOSE)],
    ]
    success_window = sg.Window('Éxito', success_layout , element_justification='c').Finalize()
    while True:
        event, values = success_window.read()
        if event == EVENTS_KEY.CLOSE or event == sg.WIN_CLOSED:
            break 
    success_window.close()

def get_file_and_folder(folder):
    try:
        # Get list of files in folder
        file_list = os.listdir(folder)
    except:
        file_list = []

    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith((".csv"))
    ]
    return fnames

#main function
if __name__ == "__main__":
    make_window()

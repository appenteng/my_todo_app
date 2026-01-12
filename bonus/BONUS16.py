import PySimpleGUI as sg
from Scripts.rst2odt import output

from zip_creator import make_archive

label1 = sg.Text("select files to compress")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("select destination folder")
input2 = sg.Input()
button2 = sg.FolderBrowse("choose", key="folder")

compress_button = sg.Button("Compress Files")
output_label= sg.Text(key=output, size=(40,1), text_color="green")

windows = sg.Window("File Compressor",
                    layout=[[label1, input1, button1],
                            [label2, input2, button2],
                            [compress_button, output_label]])
while True:
    event, values =windows.read()
    print(event, values)
    filepaths = values["files"].split(';')
    folder = values["folder"]
    make_archive(filepaths, folder)
    windows["output"].update("Files compressed successfully!")
    if event == sg.WIN_CLOSED:
        break


windows.close()
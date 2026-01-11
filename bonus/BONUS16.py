import PySimpleGUI as sg

label1 = sg.Text("select files to compress")
input1 = sg.Input()
button1 = sg.FilesBrowse("Click Me")

label2 = sg.Text("select destination folder")
input2 = sg.Input()
button2 = sg.FolderBrowse("Click Me")

windows = sg.Window("File Compressor",
                    layout=[[label1, input1, button1],
                            [label2, input2, button2],
                            [sg.Button("Compress Files")]
])

windows.read()
windows.close()
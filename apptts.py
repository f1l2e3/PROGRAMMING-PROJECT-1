import PySimpleGUI as sg
import pyttsx3

TEXT_TO_SPEECH_ENGINE = pyttsx3.init()
VOICE_TYPES = TEXT_TO_SPEECH_ENGINE.getProperty('voices')



layout = [    [sg.Text('Select the type of voice:',text_color='black',background_color='gold'),
               sg.Radio('Male Voice', 'RADIO1', default=True, key='male',background_color='green'),
               sg.Radio('Female Voice', 'RADIO1', key='female',background_color='green')],
     [sg.Text('Enter text to speak:',text_color='black',background_color='white',)],
          
    [sg.InputText(key='input'),sg.Button('Speak',button_color='blue')],
   
    
]

window = sg.Window('TEXT TO SPEECH CONVETOR', layout,background_color='blue')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input']
        if values['male']:
            TEXT_TO_SPEECH_ENGINE.setProperty('voice', VOICE_TYPES[0].id)
        elif values['female']:
           TEXT_TO_SPEECH_ENGINE.setProperty('voice', VOICE_TYPES[1].id) 
    
        TEXT_TO_SPEECH_ENGINE.say(text)
        TEXT_TO_SPEECH_ENGINE.runAndWait()

window.close()
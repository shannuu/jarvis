import datetime
import wikipedia
import webbrowser
import os

while True:
    query = input('\nHukum Do Mere Aaka: ')
    if 'wikipedia' in query:
        print('Searching Wikipedia...', 0)
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print("According to Wikipedia", 0)
        print(results, 0)

    elif 'search' in query:
        query = query.replace("search", "")
        extraUrl = 'https://google.com/search?q='
        url = extraUrl + query
        print(f'searching {query}', 0)
        webbrowser.open(url)

    elif 'open' in query:
        query = query.replace("open", "")
        if 'link' in query: 
            link = input('Enter the link: ')
            print(f'opening {link}', 0)
            webbrowser.open(link)
        elif 'youtube' in query:
            webbrowser.open("https://youtube.com")
            print("opening youtube....", 0)

        elif 'google' in query:
            webbrowser.open("https://google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        else:
            link = input('Option not found, Please enter the url: ')
            print(link ,0)
            webbrowser.open(link)   

    elif 'music' in query:
        music_dir = input('enter the path');
        try:
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        except:
            print("unknown error")

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        print(f"Sir, the time is {strTime}", 0)


    elif 'print' in query:
        print("what should i print: ", 0)
        speach = input()
        print(speach, 1)

    elif 'help' in query:
        print('\n\nCommands:')
        print("     open \'website name or custom url\'")
        print('     wikipedia \'Anything\'')
        print('     search \'Anything\'')
        print('     play music')
        print('     time')
        print('     print')
        print('     Control + C to exit')

    else:
        print(f'Error: No Command Named {query}')


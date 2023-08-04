import pyttsx4

engine = pyttsx4.init()



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)


engine.say('você é cachorro')
engine.runAndWait()
# import pyttsx3
#
# sound = pyttsx3.init()
# list_of_names = []
# print("Enter The Name Of The Persons")
# while True:
#     name = input()
#     if name == '0':
#         break
#     list_of_names.append(name)
#
#
#
# for i in list_of_names:
#     sound.say(f"Shoutout to {i}")
#     sound.runAndWait()
#     print(f"Shoutout to {i}")
import win32com.client


# def speak(text):
speak = win32com.client.Dispatch("SAPI.SpVoice")
#     speak.Speak(text)

if __name__ == "__main__":
    list_of_names = []
    print("Enter The Name Of The Persons")
    while True:
        name = input()
        if name == '0':
            break
        list_of_names.append(name)
    for i in list_of_names:
        speak.Speak(f"Shoutout to {i}")

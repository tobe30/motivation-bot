#Ai by maizu

import random


DATA = [
    {'words': ['hi','hey','sup','hafa','hello','heyo', 'how are you'],
     'bot':["Hey there! How is ur day", "What's up", "i dey you", "Just chilling you.", "Hey there!how's it going"],
     'accept':['hi','hey','sup','hafa','hello','heyo','how are you']},

     {'words': ['bad','not fine','sad','mad','not good','heyo'],
     'bot':["Why whats wrong!"],
     'accept':['hi','hey','sup','hafa','hello','heyo','how are you']},
     
     {'words': ['am broke', 'thing are not going well', 'i need money','money'],
     'bot':["well if you need money or broke you have to find a skill or a job!"],
     },
     
     {'words': ['ok', 'kk'],
     'bot':["if you need anything else am always here"],
     },
     
     {'words': ['ok thanks', 'thanks', 'thank you'],
     'bot':["no problem"],
     },
     
     {'words': ['give me a motivational quote', 'motivate me', ],
     'bot':["never give up", "hustlers dont sleep they nap","life's a gift and i don't intend on wasting it","you deserve love"],
     },
     
     {'words': ['my girlfriend broke my heart', 'she broke me', 'my heart has been broken',],
     'bot':["well sorry it will heal with time"],
     },
     
     {'words': ['wow', 'that is a good one'],
     'bot':["Thanks"],
     },
     
    {'words': ['give me another one', 'generate again', 'generate', 'again', 'one more'],
     'bot':["it is what is", "surviving is winning what ever you do survive","chase the bag and everything will come with it","if dey doubt you prove em wrong"],
     },
]



while True:
    response = input('you: ')
    has_response = False

    
    for index, word in enumerate(DATA):
        for accepted_word in word['words']:
            if accepted_word in response:
                has_response = True
                text = random.choice(word['bot'])
                print('bot: ' + text)
                break
        if has_response:
            break
        

    if not has_response:
        print("Sorry, I don't understand that.")
        print(response)
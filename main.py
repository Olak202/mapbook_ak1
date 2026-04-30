

users: list = [
    {'username':'Oliwia','location':'łódź','posts':1,'usermessage':['życzenia1', 'kocham legię', 'sprzedam opla', 'kiwi']},
    {'username':'Paweł','location':'ostróda','posts':2,'usermessage':['życzenia2', 'kocham legię', 'sprzedam opla']},
    {'username':'Elizka','location':'radom','posts':3,'usermessage':['życzenia3', 'kocham legię']},
    {'username':'Filip','location':'dęblin','posts':4,'usermessage':['życzenia4', 'kocham legię', 'sprzedam opla', 'kiwi3']}

]

for user in users[1:]:
    print(f'twój znajomy {user['username']} z miejscowości {user["location"]} opublikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')

#   twój znajomy Filip z miejscowości Dęblin opublikował 1 post o treści: życzenia


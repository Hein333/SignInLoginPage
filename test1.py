datalsit = [('app', None), ('aung@gmail.com', 'aung'), ('hein@gmail.com', 'hein')]


def UsernameCheckInDatabase(Username,datalsit):
    usernamelist = []
    for i in range(len(datalsit)):
        usernamelist.append(datalsit[i][1])
    for i in range(len(usernamelist)):
        if Username in usernamelist:
            print("Your username is already used")
            break
        elif Username not in usernamelist:
            usernamelist.append(Username)
            print(usernamelist)
            print("Username added")
            break
        else:
            print("error in UsernameCheckInDatabase")
            
#this is to make the same method name as the Gmail           
def UsernameAnalysis(Username,datalsit):
    UsernameCheckInDatabase(Username,datalsit)

UsernameAnalysis('hein',datalsit)
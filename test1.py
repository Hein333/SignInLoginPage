datalsit = [('app', None), ('aung@gmail.com', 'aung'), ('hein@gmail.com', 'hein')]

def GmailCheckInDatabase(Gmail,datalsit):
    gmaillist = []
    for i in range(len(datalsit)):
        gmaillist.append(datalsit[i][0])
    for i in range(len(gmaillist)):
        if Gmail in gmaillist:
            print("Your gmail is already used")
            break
        elif Gmail not in gmaillist:
            gmaillist.append(Gmail)
            print(gmaillist)
            print("Gamil added")
            break
        else:
            print("error in GmailCheckInDatabase")
            
#need to improve later more specifically            
def GmailAnalysis(Gmail,datalsit):
    GmailKeyConfirmation =  "@" in Gmail
    if GmailKeyConfirmation:
        GmailCheckInDatabase(Gmail,datalist)
    else:
        print("Not a Gamil")

GmailAnalysis('hein',datalsit)
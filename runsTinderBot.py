import tkinter as tk
from  tinderBot import *
import uuid 
from PIL import Image
class LoginWindow:
    def __init__(self): 
        self.login = ''
        self.password = ''
        self.loginWindow = tk.Tk()
        self.loginWindow.title("Tinderbot start window")
        self.loginWindow.geometry('600x400+400+200')
        #Add explanation text
        explanationText = tk.Label(self.loginWindow, text="Please, enter your tinder account email and password " ,font='Helvetica 16 bold')
        explanationText.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)
        #Adding input data
        positionOfInputDataVertically = 0.5
        positionOfInputDataHorizontally = 0.5
        inputDataWidth = 40
        loginText = tk.Label(self.loginWindow, text="Email")
        loginText.place(relx = positionOfInputDataHorizontally - 0.24, rely = positionOfInputDataVertically - 0.1, anchor = tk.CENTER)
        self.loginInput = tk.Entry(self.loginWindow,width=inputDataWidth) 
        self.loginInput.place(relx = positionOfInputDataHorizontally, rely = positionOfInputDataVertically - 0.1, anchor = tk.CENTER)
        passwordText = tk.Label(self.loginWindow, text="Password")
        passwordText.place(relx = positionOfInputDataHorizontally - 0.25, rely = positionOfInputDataVertically - 0.03, anchor = tk.CENTER)
        self.passwordInput = tk.Entry(self.loginWindow,width=inputDataWidth, show="*")
        self.passwordInput.place(relx = positionOfInputDataHorizontally, rely = positionOfInputDataVertically - 0.03, anchor = tk.CENTER)

        #Adding buttons 
        positionOfButtonVertically = 0.6
        positionOfButtonHorizontally = 0.5
        confirmButton = tk.Button(self.loginWindow, text="Confirm", bg="black", fg="white", command=self.loginButtonWasCicked)
        confirmButton.place(relx = positionOfButtonHorizontally + 0.1, rely = positionOfButtonVertically, anchor = tk.CENTER)
        cancelButton = tk.Button(self.loginWindow, text="Cancel", bg="black", fg="white", command=self.cancelButtonWasClicked)
        cancelButton.place(relx = positionOfButtonHorizontally - 0.1, rely = positionOfButtonVertically, anchor = tk.CENTER)
        self.loginWindow.mainloop()

    def loginButtonWasCicked(self):
        self.login = self.loginInput.get()
        self.password = self.passwordInput.get()
        windowCanBeClosed = True
        if (self.login == ''):
            self.loginInput.config(bg = 'red',fg='black')
            self.loginInput.insert(0,'Please add your email')
            windowCanBeClosed = False
        elif('@' not in self.login ):
            self.loginInput.delete(0, tk.END)
            self.loginInput.config(bg = 'red',fg='black')
            self.loginInput.insert(0,'Please add a valid email')
            windowCanBeClosed = False
        if (self.password == ''):
            self.passwordInput.config(bg = 'red',fg='black')
            self.passwordInput.insert(0,'Please add your password')
            windowCanBeClosed = False
        if windowCanBeClosed: 
            self.loginWindow.destroy()       
    def cancelButtonWasClicked(self):
        self.loginWindow.destroy()


def getProfileImages():
    tinderBot = TinderBot('paoDeQueijoSobreRodas@gmail.com','paodequeijo2014')
    profileImage = tinderBot.getProfileImage()
    pathToSaveImage = '../imagesForTrainingCNN/' + str(uuid.uuid1())  + '.jpg'
    profileImage.save(pathToSaveImage)
    


def main():
    # loginWindow = LoginWindow()
    # print(loginWindow.login)
    # print(loginWindow.password)
    # if(loginWindow.login == '' and loginWindow.password == ''):
    #     print('Process canceled, ending the activities...')
    # else :
    #     tinderBot = TinderBot(loginWindow.login,loginWindow.password)
    # tinderBot = TinderBot('paoDeQueijoSobreRodas@gmail.com','paodequeijo2014')
    getProfileImages()
 
if __name__ == "__main__":
    main()
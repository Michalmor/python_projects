# -*- coding: utf-8 -*-

import tkinter as tk

class game:

    def __init__(self, input_lines):
        self.data = input_lines
        self.max = len(input_lines) - 1
        # will hold all the user answers
        self.answers = {}
        self.row = 0
        self.root = tk.Tk() # for GUI

        # dict will hold all objects on game screen
        self.dict = {}

    def start(self):
        self.buildGUI()
        self.root.mainloop()

    def buildGUI(self):
        #settings
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(1, weight = 1)

        dict = {}

        # -------- Question Label --------
        dict["label1"] = tk.Label(self.root,
            text= self.data[self.row][0],
            borderwidth=4, font=("Arial", 20), height= 2 )
        dict["label1"].grid(row=0, column = 0,columnspan= 6)

        # -------- Text Box --------
        dict["text1"] = tk.Text(self.root,
            borderwidth=4, font=("Arial", 20), height= 1)
        dict["text1"].grid(row=1, column = 0 )

        # -------- for approving text input --------
        dict["buttonEnter"] = tk.Button(self.root,
            text= "Next",
            borderwidth=4,
            width = 20, height = 4,command=lambda: self.__irqText())
        dict["buttonEnter"].grid(row=2, column= 0, padx = 5, pady = 5)

        # -------- Creating button 1 trough 6 --------
        for i in range(1,7): #1 trough 6
            dict[f"button{i}"] = tk.Button(self.root,
                text= self.data[self.row][i],
                borderwidth=4,
                width = 20, height = 4)

        # ! argument error caused me to take these out of the loop
        dict["button1"].config(command=lambda: self.__irq(1))
        dict["button2"].config(command=lambda: self.__irq(2))
        dict["button3"].config(command=lambda: self.__irq(3))
        dict["button4"].config(command=lambda: self.__irq(4))
        dict["button5"].config(command=lambda: self.__irq(5))
        dict["button6"].config(command=lambda: self.__irq(6))

        self.dict = dict

    def __irqText(self):
        """ starts on text input uppon button click"""
        # get data from text box
        ans = self.dict["text1"].get("1.0", "end-1c")

        if ans == "":
            print("\n",30*"# ","\n\t\tERROR, Nothing inserted!\n",30*"# ","\n")
            self.root.quit()

        self.answers[self.data[self.row][0]] = ans
        self.chagneGui()

    def __irq(self, arg):
        #save both question and answer to dict
        self.answers[self.data[self.row][0]] = self.data[self.row][arg]
        self.chagneGui()

    def chagneGui(self):
        self.row += 1
        # -------------------------------- END GAME
        if self.row > self.max:
            self.root.quit() #end game
            return
        # -------------------------------- Pick window State
        if self.data[self.row][1] == "Open":
            mode = "totext"
        else:
            mode = "tobuttons"
        # -------------------------------- Build GUI according
        if mode == "tobuttons": #MODE 1
            self.dict["buttonEnter"].grid_forget()
            self.dict["text1"].grid_forget()

            for i in range(1,7):
                self.dict[f"button{i}"].grid(row=1, column= i - 1, padx = 5, pady = 5)
                text = self.data[self.row][i]
                if text == "None":
                    text = 'X'
                    self.dict[f"button{i}"].configure(state= tk.DISABLED)
                else:
                    self.dict[f"button{i}"].configure(state= tk.NORMAL)

                self.dict[f"button{i}"]["text"] = text
            self.dict["label1"]["text"] = self.data[self.row][0]

        elif mode == "totext": #MODE 2
            #HIDE buttons
            for i in range(1,7):
                self.dict[f"button{i}"].grid_forget()


            self.dict["text1"].grid()
            #self.dict["text1"]["text"] = ""
            self.dict["text1"].delete("1.0", "end")
            self.dict["buttonEnter"].grid()
            self.dict["label1"]["text"] = self.data[self.row][0]


        else: # SHOULD NOT HAPPEN
            print("INTERNAL ERROR")

    def getData(self):
        return self.answers





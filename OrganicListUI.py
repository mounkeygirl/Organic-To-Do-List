"""
Creator: Anna Carlson
Last updated: 1/14/2020

"""

from breezypythongui import EasyFrame
from OrganicToDoList import *
from MyClasses import *
from tkinter import BOTH, END, LEFT,HORIZONTAL, N,S,E,W


class OrganicUI(EasyFrame):

    def __init__(self):
        """Sets up the window and the label."""
        EasyFrame.__init__(self)
        self["background"]="yellow"
        self.setSize(1000,700)

        #title
        titlePanel=self.titlePanel=self.addPanel(row=0,column=0,background="yellow")
        titlePanel.addLabel(text="Organic To Do List",row=1,column=0)
        #top menu bar
        self.setupTopMenuBar()

        #Basic set up for input and output is done here.
        #Defaulting to showing large Goals
        self.displayLargeGoalsCmd()

        #I may want to replace these with something else in a later situation
        """
        #buttons
        self.buttonPanel=buttonPanel=self.addPanel(row=3,column=0,background="tan")
        buttonPanel.addButton("Submit", row=0, column=0,
                              command=self.submitCmd)
        buttonPanel.addButton("Clear", row=0,column=1,
                              command=self.clearCmd)
        """
    def setupTopMenuBar(self):
        titlePanel=self.titlePanel
        self.topMenuBar=topMenuBar=self.titlePanel.addMenuBar(row=0,column=0)
        fileMenu=topMenuBar.addMenu("File")
        fileMenu.addMenuItem("Clear", command=self.clearCmd)
        fileMenu.addMenuItem("Quit",command=self.quitCmd)
        outputMenu=topMenuBar.addMenu("Output")
        outputMenu.addMenuItem("Text Area", command=self.useTextAreaOutput)
        outputMenu.addMenuItem("Fields of Interest", command=self.displayLargeGoalsCmd)
        outputMenu.addMenuItem("Projects", command=self.displayProjectCmd)
        outputMenu.addMenuItem("Chores",command=self.displayChoreCmd)
        outputMenu.addMenuItem("School Subjects",command=self.displaySubjectCmd)


    #turn on and off ability to modify text area
    def changeOutputState(self):
        if self.outputArea["state"]=="normal":
            self.outputArea["state"]="disabled"
        else:
            self.outputArea["state"]="normal"

    #using changeOutputState method update the text
    def changeOutputText(self,text):
        self.changeOutputState()
        self.outputArea.setText(text)
        self.changeOutputState()


    def submitCmd(self):
        self.changeOutputState()
        self.outputArea.setText(test())
        self.changeOutputState()


    #clear out text area
    def clearCmd(self):
        self.changeOutputText("")

    def quitCmd(self):
        self.exit()


    def useTextAreaOutput(self):
        self.outputPanel=outputPanel=self.addPanel(row=1,column=0,background="green")
        outputArea=self.outputArea=outputPanel.addTextArea(text="",row=0,column=0,
                                                           wrap="word")
        outputArea.setText(reasonsFile)
        print(reasonsFile)

    def displayLargeGoalsCmd(self):
        self.status="Large Goal"
        #listbox
        self.listBoxPanel=self.addPanel(row=1,column=0)
        self.listBox=self.listBoxPanel.addListbox(row=0,column=0,
                                           rowspan=4,width=40,
                                           listItemSelected=self.listItemSelected)
        self.loadListBox(getParentlessGoals(),self.listBox)
        self.listBox.setSelectedIndex(0)

        #Input
        self.inputPanel=self.listBoxPanel.addPanel(row=1,column=1)
        #radio group
        self.inputRadioGroup=self.inputPanel.addRadiobuttonGroup(row=0,column=0, columnspan=10, orient = HORIZONTAL)
        self.updateRadio=self.inputRadioGroup.addRadiobutton(text="Update Current Item")
        #set first selection to default
        self.inputRadioGroup.setSelectedButton(self.updateRadio)
        self.createProjectRadio=self.inputRadioGroup.addRadiobutton(text="Create New Project")
        self.createLargeGoalRadio=self.inputRadioGroup.addRadiobutton(text="Create New Large Goal")

        #The second row of radio buttons will change based on what I need
        #Radio Group for project needs
        #will be modified to show or disappear based on needs
        self.showProjectRadioButtons()

        #Add each text Field to a list to ease the clearing process
        self.inputTextFieldList=[]

        #Because my input needs vary, I'll throw all of these into an a function, and genereate them based on a list
        #reason project newBaseGoal
        self.useTheFollowingInput(["reason","project","newBaseGoal"])

        #parent goal

        #add button
        self.addInputBtn=self.inputPanel.addButton(text="Add",row=30,column=1,command=self.addInputCmd)

        #output

        self.outputPanel=self.addPanel(row=2,column=0,background="#FFAAFF", rowspan=12)


        #outputbox
        self.outputArea=self.outputPanel.addTextArea(text="",row=0,column=0,
                                                           wrap="word", width=80)

        self.outputArea["state"]="disabled"


        self.useTheFollowingOutputListboxes(["reason","subproject"])

    def useTheFollowingOutputListboxes(self,list):
        #Line by Line Output
        self.outputPanelLineByLine=self.addPanel(row=1,column=1,background="#FFAAFF",rowspan=2)
        rowNum=0

        for each in list:
            if each=="reason":
                #reason
                self.outputPanelLineByLine.addLabel(text="Reasons:", row=rowNum,column=0)
                rowNum+=1
                self.reasonsLbl=self.outputPanelLineByLine.addListbox(row=rowNum,column=0)
                rowNum+=1
            if each=="subproject":
                #subproject
                self.outputPanelLineByLine.addLabel(text="SubProjects:", row=rowNum,column=0)
                rowNum+=1
                self.subProjectsLbl=self.outputPanelLineByLine.addListbox(row=rowNum,column=0)
                rowNum+=1

    def useTheFollowingInput(self, list):
        #Using a list of strings to more naturally select the needed input boxes
        self.submissionPanel=self.inputPanel.addPanel(row=2,column=0)
        rowNum=2
        for each in list:
            if each=="reason":
                #reason
                self.submissionPanel.addLabel(text="New Reason", row=rowNum, column=0)
                self.reasonInput=self.submissionPanel.addTextField(text="", row=rowNum, column=1,width=60)
                self.inputTextFieldList.append(self.reasonInput)
                rowNum+=1
            if each=="project":
                #project
                self.submissionPanel.addLabel(text="New Project", row=rowNum, column=0)
                self.projectInput=self.submissionPanel.addTextField(text="", row=rowNum, column=1,width=60)
                self.inputTextFieldList.append(self.projectInput)
                rowNum+=1
            if each =="newBaseGoal":
                #newBaseGoal
                self.submissionPanel.addLabel(text="New Base Goal", row=4, column=0)
                self.baseGoalInput=self.submissionPanel.addTextField(text="", row=4, column=1,width=60)
                self.inputTextFieldList.append(self.baseGoalInput)



    def showProjectRadioButtons(self):
        #Add a radio group for types of projects
        self.projectRadioGroup=self.inputPanel.addRadiobuttonGroup(row=1,column=0, columnspan=10, orient = HORIZONTAL)
        self.defaultProjectRadio=self.projectRadioGroup.addRadiobutton(text="Normal Project")
        self.bookProjectRadio=self.projectRadioGroup.addRadiobutton(text="Book")

        #set first selection to default
        self.projectRadioGroup.setSelectedButton(self.defaultProjectRadio)


    def addInputCmd(self):
        #each input item needs to be striped of whitespace before use
        reason= self.reasonInput.getText().strip()
        project= self.projectInput.getText().strip()
        baseGoal=self.baseGoalInput.getText().strip()
        selectedRadioText=self.inputRadioGroup.getSelectedButton()["text"]

        #update old item
        if self.inputRadioGroup.getSelectedButton()["text"]==self.updateRadio["text"]:
            print("Update radio button pressed")
            #This returns the Goal object
            dictionarySelection=(Goal.getAllGoals()[self.listBox.getSelectedItem().strip()])
            print("Selected Item: "+dictionarySelection.getName())
            #update information if given box is not empty
            #update reason
            if reason!='':
                addReason(dictionarySelection.getName(),reason)
                print("reason added")
            else:
                print("reason not added")
            #update project
            if project!='':
                addProject(project,dictionarySelection.getName())
                print("Project added to "+dictionarySelection.getName())
            else:
                print("Project Not added")

        #Create new project
        elif selectedRadioText==self.createProjectRadio["text"]:
            print("Project creation radio button pressed")

        elif selectedRadioText==self.createLargeGoalRadio["text"]:
            print("New Base Goal radio button pressed")
            if baseGoal!='':
                addLargeGoal(baseGoal)


        #clear input after add button has been clicked
        for each in self.inputTextFieldList:
            each.setText("")

    def displaySubjectCmd(self):
        self.status="Subject"
        #clear listbox
        self.listBox.clear()
        #load in new list
        self.loadListBox(Subject.getTotalGoalList(),self.listBox)
        #set default selection to first item
        self.listBox.setSelectedIndex(0)


    def displayProjectCmd(self):
        self.status="Project"

        #listbox

        self.listBox.clear()
        self.loadListBox(Project.getTotatlGoalList(),self.listBox)
        self.listBox.setSelectedIndex(0)

    def displayChoreCmd(self):
        self.status="Chore"

         #listbox

        self.listBox.clear()
        self.loadListBox(Chore.getTotatlGoalList(),self.listBox)
        self.listBox.setSelectedIndex(0)


    #other
    def listItemSelected(self,index):
        if self.status==("Project"):
            goals=getProjectList()
            print("Pie")
            output=(goals[self.listBox.getSelectedItem().strip()])

        elif self.status==("Large Goal"):
            goals=(getParentlessGoals())
            print("This is not Pie")
            output=(goals[self.listBox.getSelectedItem().strip()])
        elif self.status==("Chore"):
            goals=getChores()
            output=(goals[self.listBox.getSelectedItem().strip()])
        elif self.status==("Subject"):
            goals=getSubjectList()
            output=(goals[self.listBox.getSelectedItem().strip()])
        else:
            output="self.status either not defined or not in pre-established list"


        print(output)
        self.changeOutputText(output)
        #change reasons list to string and show that
        listForm = goals[self.listBox.getSelectedItem().strip()].getReason()
        self.loadListBox(listForm,self.reasonsLbl)
        #self.convertListToOutputText(listForm,self.reasonsLbl)
        #self.subProjectsLbl
        self.loadListBox(goals[self.listBox.getSelectedItem().strip()].getProject(),self.subProjectsLbl)

    def reasonListItemSelected(self,index):
        print ("wip")

    def convertListToOutputText(self,listForm,outputLbl):
        #use an if statment to change part of the code durring an update without
        #having to wait until the updates are totally done to see the output

        if True==True:
            output=""
            for each in listForm:
                if isinstance(each,str):
                    output+=each+"\n"
                elif isinstance(each,Project):
                    output+=each.getName()+"\n"
                else:
                    output="convertListToOutputText function type failure"

            #outputLbl.setText(output)

    def loadListBox(self,loadFromList,listBox):
        goals=loadFromList
        listBox.clear()
        if isinstance(goals,dict):
            for (key,value) in goals.items():
                if value.getParent()==None :
                    listBox.insert(value.getId(), key)
                else:
                    listBox.insert(value.getParent().getId()+1, "    "+key)
        elif isinstance(goals,list):
            for each in goals:
                if isinstance(each,str):
                    listBox.insert(END,each)
                    print("Load Box Debug: "+each)
                elif isinstance(each,Goal):
                    listBox.insert(END,each.getName())
                else:
                    print ("loadListBox Error. each item in list not accounted for")

        else:
            print("loadListBox error. isinstance check failure")

def main():
    """"Instantiates and pops up the window."""
    OrganicUI().mainloop()

def getParentlessGoals():
    return getTotalGoalList()


def test():
    """This is to test out the ability to go down the method list"""
    return showAllLargeGoals()


if __name__=="__main__":
    main()

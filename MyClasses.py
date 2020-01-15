"""
Cretor: Anna Carlson
Last Updated 1/14/2020

"""
#Section of code is similer between LargeGoal and Project,
#So I'm making a seperate class to do that
import datetime

class InternalClassData(object):
    def __init__(self):
        self.numberOfGoals=0
        self.totalGoalList={}

    def assignNewId(self):
        returningId=self.numberOfGoals
        self.numberOfGoals+=1
        return returningId

    def addToTotalGoalList(self,additionalGoal):
        self.totalGoalList[additionalGoal.getName()]=additionalGoal

    def getTotalGoalList(self):
        return self.totalGoalList

class Goal(object):
    _internalData=InternalClassData()

    def __init__(self,name):
        #add a runing directory of each goal added
        #Goal._internalData.addToTotalGoalList(self)
        self.id=Goal._internalData.assignNewId()
        self.name=name
        self.reason=[]
        self.subgoals=[]
        self.parent=None
        self.projects=[]
        self.chores=[]
        Goal._internalData.addToTotalGoalList(self)
        self.dateLog=[]

    def getAllGoals():
        return Goal._internalData.getTotalGoalList()

    #getters and setters
    def getName(self):
        return self.name

    def setName(self, name):
        self.name=name

    def getReason(self):
        return self.reason

    def getId(self):
        return self.id

    def addReason(self, newReason):
        Goal.addToList(self,self.reason,newReason)

    def addProject(self, newProject):
        Goal.addToList(self,self.projects,newProject)

    def getProject(self):
        return self.projects

    def addChore(self, newChore):
        Goal.addToList(self,self.chores,newChore)

    def addSubgoal(self,goal):
        #Goal.addToList(self,self.subgoals,Goal(goal))
        #self.subgoals.append(Goal(goal))
        if type(goal) is list:
            for eachItem in goal:
                self.addParentToNewSubGoal(eachItem)
        else:
            self.addParentToNewSubGoal(goal)



    def getSubgoals(self):
        return self.subgoals

    def getParent(self):
        return self.parent

    def setParent(self,parent):
        self.parent=parent
    #assitant functions
    # def addParentToNewSubGoal(self,subgoal):
    #     newGoal=Goal(subgoal)
    #     self.subgoals.append(newGoal)
    #     newGoal.setParent(self)



    def addToDateLog(self,note=None):
        dateLog.append(DateLog(note))

    def getDateLog(self):
        return dateLog


    #output lists
    def convertListToString(self,list,name):
        output=""
        if len(list)>0:
            output+="\n\t"+name+":\t"
            addComma=False
            for eachThing in list:
                if addComma==True:
                    output+=", "
                output+=eachThing
                addComma=True
        return output


    def addToList(self,addToList,newThing):
        if type(newThing) is list:
            addToList.extend(newThing)
        else:
            addToList.append(newThing)

    def printSubgoals(self):
        output=""
        if len(self.subgoals)>0:
            output+="\n\tSubgoals:\n"
            addBreak=False
            for eachThing in self.subgoals:
                if addBreak==True:
                    output+="\n"
                output+="\t"+str(eachThing)
                addBreak=True
        return output



    def getReasonsString(self):
        return Goal.convertListToString(self,self.reason,"Reason(s)")

    def __str__(self):
        return "Name: "+self.name+" ID: "+str(self.getId())+Goal.getReasonsString(self)+Goal.printSubgoals(self)

#Used to keep track of school classes. Subject is used to avoid confusion with
#programming class
class Subject(Goal):
    _internalData=InternalClassData()
    def __init__(self,name):
        Goal.__init__(self, name)
        #add a runing directory of each goal added
        Subject._internalData.addToTotalGoalList(self)

    def getTotalGoalList():
        return Subject._internalData.getTotalGoalList()



class LargeGoal(Goal):
    _internalData=InternalClassData()
    def __init__(self,name):
        Goal.__init__(self, name)
        #add a runing directory of each goal added
        LargeGoal._internalData.addToTotalGoalList(self)

    def getTotalGoalList():
        return LargeGoal._internalData.getTotalGoalList()


    def addParentToNewSubGoal(self,subgoal):
        newGoal=LargeGoal(subgoal)
        self.subgoals.append(newGoal)
        newGoal.setParent(self)



class Project(Goal):

    _internalData=InternalClassData()
    def __init__(self,name,type=None):
        Goal.__init__(self, name)

        #add a runing directory of each goal added
        Project._internalData.addToTotalGoalList(self)

        self.type=type
        #Add this to a list on the LargeGoal type if that is defined
        if self.type !=None:
            LargeGoal.getTotalGoalList()[type].addProject(self)


    def getTotatlGoalList():
        return Project._internalData.getTotalGoalList()


    def addParentToNewSubGoal(self,subgoal):
        newGoal=Project(subgoal)
        self.subgoals.append(newGoal)
        newGoal.setParent(self)

    def typeStringOutput(self):
        if self.type !=None:
            return "\nType: "+self.type
        else:
             return ""

    def __str__(self):
        output=self.typeStringOutput()
        return Goal.__str__(self)+output

#Chores differ from projects in that they have no finishing point.
#I may have completed the task for the day, but it'll regenerate over time
class Chore(Goal):

    _internalData=InternalClassData()

    def __init__(self,name,type=None):
        Goal.__init__(self, name)

        #add a runing directory of each goal added
        Chore._internalData.addToTotalGoalList(self)

        self.type=type
        #Add this to a list on the LargeGoal type if that is defined
        if self.type !=None:
            LargeGoal.getTotalGoalList()[type].addChore(self)

                ###

    def getTotatlGoalList():
        return Chore._internalData.getTotalGoalList()



    def addParentToNewSubGoal(self,subgoal):
        newGoal=Project(subgoal)
        self.subgoals.append(newGoal)
        newGoal.setParent(self)

#I want to keep notes based on date and time, so it makes sense to make
#a seperate class
class DateLog(object):
    def __init__(self,note=None):
        self.note=note
        self.date=datetime.datetime.now()

    def getDate(self):
        return self.date

    def getNote(self):
        return self.note




#Reading a book is a normal task, so I want to keep track of various properties
class Book(object):
    def __init__(self,name,numberOfPages):
        self.name =name
        self.numberOfPages=numberOfPages
        self.pages=[]
        setUpPages()

    def setNumberOfPages(number):
        self.numberOfPages=number

    def getNumberOfPages():
        return self.numberOfPages

#As I've got number of manuals, I often jump around. Reading the pages in order
#is not always practical

    def setUpPages(self):
        for each in self.numberOfPages:
            pages.append(Page())


    def readThesePages(startPage, endPage):
        #calculate total number of pages
        numberOfPages=endPage-startPage
        #update pages in that range to read

class Page(object):
    def __init__(self):
        self.read=False

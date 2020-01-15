#I ran into a book talking about cleaning by personality type.
#Being a sucker for personality type quizes and found that I'm an
#organic clearner.
#This to do list is supposed to lean into some aspects of that personality.


from MyClasses import *

baseGoals={"Programming":LargeGoal("Programming"),
           "Physical Fitness":LargeGoal("Physical Fitness"),
           }
allTheGoals=Goal.getAllGoals()

def addBaseGoal(addName):
    baseGoals[addName]=LargeGoal(addName)

def getTotalGoalList():
    return LargeGoal.getTotalGoalList()

def getReason(goalName):
    return allTheGoals[goalName].getReason()

#Files= adding to and laoding from
#add to
def addLargeGoal(goalName,parentGoalName=None):
    #Create new project item
    LargeGoal(goalName)

    #open file in append form
    f=open("largeGoals.txt",'a+')
    #save all pertenent info seperated by $ signs
    #check if parentGoalName is None
    if parentGoalName==None:
        parentGoalName=''
    #if there is a parent, I need to add this to it's subgoal list
    else:
        getTotalGoalList()[parentGoalName].addSubgoal(goalName)

    f.write(goalName+"$"+parentGoalName+"\n")
    #close file
    f.close()


def addReason(goalName, reason):
    f=open("reasons.txt",'a')
    f.write(goalName+"$"+reason+"\n")
    allTheGoals[goalName].addReason(reason)
    f.close()

def addProject(projectName,largeGoalName=None):
    #open file in append form
    f=open("projects.txt",'a+')
    #save all pertenent info seperated by $ signs
    f.write(projectName+"$"+largeGoalName+"\n")
    #close file
    f.close()
    #Create new project item
    newProject=Project(projectName,largeGoalName)

def addChore(choreName, largeGoalName=None):
    #open file in append form
    f=open("chores.txt",'a+')
    #save all pertenent info seperated by $ signs
    f.write(choreName+"$"+largeGoalName+"\n")
    #close file
    f.close()
    #Create new project item
    Chore(choreName,largeGoalName)

def addSubject(classSubjectName):
    #open file in append form
    f=open("subject.txt",'a+')
    #save all pertenent info seperated by $ signs
    f.write(classSubjectName+"\n")
    #close file
    f.close()
    #Create new School Subject
    Subject(classSubjectName)



#load from
def loadLargeGoal():
    f = open("largeGoals.txt","r+")
    for each in f:
        parts = each.split("$")
        #check if parent is '', which was how I save the None reference,
        #and change it back
        parentGoal=parts[1].rstrip()
        if parentGoal=='':
            parentGoal=None
        #if parent goal does exist , add this to it
        else:
            print("Parent Goal: "+parentGoal+" Loaded Goal: "+parts[0])
            getTotalGoalList()[parentGoal].addSubgoal(parts[0])
        LargeGoal(parts[0])


def loadProjects():
    f=open ("projects.txt")
    for each in f:
        parts = each.split("$")
        newProject=Project(parts[0],parts[1].rstrip())

def loadChores():
    f=open ("chores.txt")
    for each in f:
        parts = each.split("$")
        Chore(parts[0],parts[1].rstrip())

def loadReasons():
    f=open("reasons.txt")
    for each in f:
        parts=each.split("$")
        allTheGoals[parts[0]].addReason(parts[1].rstrip())

def loadSubjects():
    f=open("subject.txt")
    for each in f:
        parts=each.split("$")
        Subject(parts[0].rstrip())


def loadStartupFiles():
    loadLargeGoal()
    loadProjects()
    loadReasons()
    loadChores()
    loadSubjects()

addBaseGoal("Art")
baseGoals["Art"].addSubgoal(["Anatomy","Animation"])
addBaseGoal("Cleaning")
baseGoals["Cleaning"].addReason("Need to research a competent butler")
baseGoals["Cleaning"].addReason("I want a cleaner house")
addBaseGoal("Music")
baseGoals["Music"].addReason(["I want to design my own video game music", "Join in jam sessions at family gatherings"])
baseGoals["Physical Fitness"].addReason(["Loose weight","Be able to write and draw about it"])
baseGoals["Physical Fitness"].addSubgoal("Research Boxing")
baseGoals["Physical Fitness"].addSubgoal("Learn to Dance")
baseGoals["Programming"].addSubgoal(["Python","Java","Javascript","Game Maker Studio 2"])
getTotalGoalList()["Javascript"].addReason("Bushel Application Is in Javascript")
getTotalGoalList()["Python"].addReason("It is required for one of my required classes this semester")
getTotalGoalList()["Java"].addReason("My first programming language and I want to keep up with it")


#My lists automaticlly expand whenever I create an object.
#project
myStarterProjects=([Project("Make this Program","Python"),Project("Do Bushel Projets")])
#chore
myStarterChores=([Chore("Dishes"),Chore("Laundry")])

#School Subjects
([Subject("Ethical Hacking")])



#load from files
loadStartupFiles()


def showAllLargeGoals():
    output=""
    for (key,value) in baseGoals.items():
        output+="\n"+str(value)
        print(value)
    return output


def printOutTotalGoalList():
    goalList=getTotalGoalList()
    for eachItem in goalList:
        print (str(eachItem))

def getProjectList():
    return Project.getTotatlGoalList()


def getChores():
    return Chore.getTotatlGoalList()

def getSubjectList():
    return Subject.getTotalGoalList()

def main():
    intro="Organic to do list"

    print(intro)
    showAllLargeGoals()

if __name__=="__main__":
    main()

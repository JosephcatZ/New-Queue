import json
JSON = open("queue.json")
queue = json.loads(JSON.read())
JSON.close()
LVL = {
"Id"          : "PLA-CEH-OLD",
"Creator"     : "Defender",
"Aproved"     : False,
"Title"       : "A Place Holder Level",
"Description" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
}
def add(ID,Creator,Title,Desc):
    temp = {"Id"          : ID,
            "Creator"     : Creator,
            "Title"       : Title,
            "Description" : Desc
            }
    for i in queue:
        if i["Id"] == ID:
            print("I'm sorry, that level is already in the queue")
            return(1)
    print("@"+Creator+" your level, \""+Title+"\" Has been added to the queue, you are currently in position", len(queue), "out of", len(queue))
    queue.append(temp)

def getpos(In):
    count = 0
    for i in queue:
        if i["Id"] == In:
            print(queue[count]["Id"],"is in position",count,"out of",len(queue)-1)
            break;
        elif i["Title"] == In:
            print('"'+queue[count]["Title"]+'"',"is in position",count,"out of",len(queue)-1)
            break;
        count = count + 1
pos = 0
def Cleared():
    queue.remove(queue[pos])
def play():
    print("NEXT LEVEL:\n\n"+queue[pos]["Title"],"\n"+len(queue[pos]["Title"])*"-","\nId -",queue[pos]["Id"],"\nCreator -",queue[pos]["Creator"],"\n\n\n")
def absent():
    global pos
    pos = pos + 1
def Dump():
    JSON = open("queue.json","w")
    JSON.write(json.dumps(queue))
add(LVL["Id"],LVL["Creator"],LVL["Title"],LVL["Description"])
add("a",LVL["Creator"],LVL["Title"],LVL["Description"])
getpos(LVL["Id"])
getpos(LVL["Title"])
absent()
play()
Dump()


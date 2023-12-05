def createNode(data):
    return {
        "data": data,
        "next": None
    }

def addAtStart(head, data):
    newNode = createNode(data)
    newNode["next"] = head
    return newNode


def addAtEnd(head, data):
    newNode = createNode(data)
    temp = head
    while(temp["next"] != None):
        temp = temp["next"]
    temp["next"] = newNode
    return head

def removeAtStart(head):
    temp = head["next"]
    head["next"] = None
    return temp

def removeAtEnd(head):
    temp = head["next"]
    while(temp["next"]["next"] != None):
        temp = temp["next"]
    temp["next"] = None
    return head

def printList(head):
    temp = head
    while(temp != None):
        print(temp["data"], end=" => ")
        temp = temp["next"]
    print("None")
    

head = {
    "data": 1,
    "next": {
        "data": 2,
        "next": {
            "data": 3,
            "next": None
        }
    }
}


head = addAtStart(head, 5)
printList(head)
head = addAtEnd(head, 6)
printList(head)
head = removeAtStart(head)
printList(head)
head = removeAtEnd(head)
printList(head)








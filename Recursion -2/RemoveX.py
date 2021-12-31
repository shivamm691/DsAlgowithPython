#Given a string, compute recursively a new string where all 'x' chars have been removed.
def removeX(string):
    if len(string)==0:
        return string
    
    if string[0]=='x':
        return removeX(string[1:])
    result =string[0]+removeX(string[1:])
    return result    
        
    pass

# Main
string = input()
print(removeX(string))

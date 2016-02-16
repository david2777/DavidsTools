import socket

def buildCommand(CommandList):
    return "\n".join(CommandList)

def SendCommand(Host, Port, Command):
    """Takes a Command in the form of a list or string and sends it to the
    specified Host and Port"""
    #Verify Input
    if type(Command) == str:
        pass
    elif type(Command) == list:
        Command = buildCommand(Command)
    else:
        print "Error! Command must be string or list!"
        return None
    
    #Establish connection    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = (Host, Port)
    client.connect(conn)

    #Send command and get response
    client.send(Command)
    response = client.recv(1024)
    client.close()
    
    #Format, print and return response
    response = str(response).replace("\n", "").replace("\x00", "").replace("\t", " ")
    print '// Result: {0} //'.format(response)
    return response

if __name__=='__main__':
    thisHost = socket.gethostname()
    #You can send strings, notice the \\n to print a new line rather than
    #   add a new line to the command.
    MelCommand = """sphere;\nprint "Wow this works!\\n";\n"""
    
    #You can also send lists that will be turned into a command
    PyCommand = ["import maya.cmds as cmds",
                "cmds.sphere()",
                "print 'Wow this works too!'"]

    #MEL Commands go to 5555, Python to 6666
    #This can be changed as long as you change it in the mel setup as well
    SendCommand(thisHost, 5555, MelCommand)
    SendCommand(thisHost, 6666, PyCommand)

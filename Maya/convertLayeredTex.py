import maya.cmds as cmds
import maya.mel as mel

"""
convertLayeredTex - By David DuVoisin
This script convertes a LayeredTexture into a series of blend colors nodes.
I made this because RMS20 does not support the LayeredTexture and I wanted
to convert some procedural shaders from VRay to RMS.
This might not work every time but it seems to work enough for me.
"""


def colorTransfer(fromCon, toCon):
    fromVar = cmds.listConnections(fromCon, d = True, p = True)
    if fromVar == None:
        fromVar = cmds.getAttr(fromCon)[0]
        cmds.setAttr(toCon, fromVar[0], fromVar[1], fromVar[2], type = 'float3')
    else:
        cmds.connectAttr(fromVar[0], toCon)

def alphaTransfer(fromCon, toCon):
    fromVar = cmds.listConnections(fromCon, d = True, p = True)
    if fromVar == None:
        fromVar = cmds.getAttr(fromCon)[0]
        cmds.setAttr(toCon, fromVar)
    else:
        cmds.connectAttr(fromVar[0], toCon)


def convertLayeredTex():
    mySel = cmds.ls(sl=True)
    if len(mySel) == 1:
        mySel = mySel[0]
    else:
        raise Exception("Please only select one thing")

    if cmds.nodeType(mySel) != 'layeredTexture':
        raise Exception("Please select a Layered Texture")

    connections = cmds.getAttr(mySel + '.inputs', multiIndices = True)
    baseCon = None

    for con in connections:
        blendType = cmds.getAttr(mySel + '.inputs[' + str(con) + '].blendMode')
        if blendType == 0:
            baseCon = con
            break

    if baseCon == None:
        raise Exception("No base, looking for a base connection with the blend mode set to None")

    connections.remove(baseCon)
    connections.reverse()



    lastMixer = cmds.shadingNode('blendColors', au = True)
    colorTransfer(mySel + '.inputs[' + str(baseCon) + '].color', lastMixer + '.color2')


    for con in connections:
        colorTransfer(mySel + '.inputs[' + str(con) + '].color', lastMixer + '.color1')
        alphaTransfer(mySel + '.inputs[' + str(con) + '].alpha', lastMixer + '.blender')

        newMixer = cmds.shadingNode('blendColors', au = True)
        cmds.connectAttr(lastMixer + '.output', newMixer + '.color2')
        lastMixer = newMixer

    cmds.delete(lastMixer)



convertLayeredTex()

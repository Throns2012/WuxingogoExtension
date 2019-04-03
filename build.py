#!/usr/bin/python
#coding=utf-8
import sys, csv , operator
import os
import glob
import shutil
import platform


def removefile(filepath, suffix):
    print ("Root Path : " + filepath)
    for root, dirs, files in os.walk(filepath):
        for name in files:
            if name.endswith(suffix):
                os.remove(os.path.join(root, name))
                print("Delete File: " + os.path.join(root, name))
                

def UsePlatform():
  sysstr = platform.system()
  if(sysstr =="Windows"):
    DoWindowsCommand();
  else:
    DoUnixCommand();
  print ("Environment : " + sysstr)


def DoWindowsCommand():
    os.system("msbuild WuxingogoRuntime.sln")
    os.system("msbuild WuxingogoEditor.sln")

def DoUnixCommand():
    os.system("msbuild WuxingogoRuntime.sln")
    os.system("msbuild WuxingogoEditor.sln")


def copyfile(filepath, despath):
    try:
        shutil.copyfile(filepath,despath)
        print(filepath + " or " + despath + " was success !")
    except Exception: 
        print(filepath + " or " + despath + " was error !")
    pass
def copyDirectory(dirpath, despath):
    try:
        from distutils.dir_util import copy_tree
        copy_tree(dirpath, despath)
    except Exception as e:
        #print(dirpath + " OR " despath + " Was error !")
        print(e)
    pass
	

def abspath(filepath):
    return os.path.abspath

def currPath():
    return os.path.abspath(os.curdir)

def CopyToProject(despath):
    copyfile( currPath()+"/" + editorSourceFile,despath + "Editor/WuxingogoEditor.dll")
    copyfile( currPath()+"/" + runtimeSourceFile,despath + "Plugins/WuxingogoRuntime.dll");
    copyfile( currPath()+"/" + editorDllPdb,despath + "Editor/WuxingogoEditor.pdb")
    copyfile( currPath()+"/" + editorDllMdb,despath + "Editor/WuxingogoEditor.dll.mdb")
    copyfile( currPath()+"/" + runtimeDllPdb,despath + "Plugins/WuxingogoRuntime.pdb")
    copyfile( currPath()+"/" + runtimeDllMdb,despath + "Plugins/WuxingogoRuntime.dll.mdb")
    
def CopyPluginDirectory(despath):
    copyDirectory( currPath()+ "/" + OutPutDirectory, despath)



print("remove all meta")
path = os.getcwd()
removefile("WuxingogoEditor", ".meta")
removefile("WuxingogoRuntime", ".meta")
print("remove all meta success")

UsePlatform()

os.chdir(currPath())

isSecure = 0
editorSourceFile = "OutPutDll/WuxingogoEditor.dll"
runtimeSourceFile = "OutPutDll/WuxingogoRuntime.dll"
editorDllPdb = "OutPutDll/WuxingogoEditor.pdb"
editorDllMdb = "OutPutDll/WuxingogoEditor.dll.mdb"
runtimeDllPdb = "OutPutDll/WuxingogoRuntime.pdb"
runtimeDllMdb = "OutPutDll/WuxingogoRuntime.dll.mdb"
OutPutDirectory = "WuxingogoExtension"

copyfile(editorSourceFile, "WuxingogoExtension/Editor/WuxingogoEditor.dll")
copyfile(runtimeSourceFile, "WuxingogoExtension/Plugins/WuxingogoRuntime.dll")

if(isSecure == 1):
    os.system("Reactor.lnk -file " + currPath()+"\\" + editorSourceFile + " -mono 1 -unprintable_characters 1")
    os.system("Reactor.lnk -file " + currPath()+"\\" + editorSourceFile + " -mono 1 -unprintable_characters 1")

    editorSourceFile = "OutPutDll\WuxingogoEditor_Secure\WuxingogoEditor.dll"
    runtimeSourceFile = "OutPutDll\WuxingogoRuntime_Secure\WuxingogoRuntime.dll"





sysstr=platform.system()
if(sysstr =="Windows"):
    

    #copyfile( currPath()+"\\" + editorSourceFile, "E:\Work\UnityProject\PhysicsDemo\Assets\Plugins\WuxingogoExtension\Editor\WuxingogoEditor.dll")
    #copyfile( currPath()+"\\" + runtimeSourceFile, "E:\Work\UnityProject\PhysicsDemo\Assets\Plugins\WuxingogoExtension\Plugins\WuxingogoRuntime.dll")
    CopyToProject("C:/Project/gayou/Client/GameCollection/Assets/Plugins/WuxingogoExtension/")
else:
    # copyfile(currPath()+"/" + editorSourceFile,"/Users/Wuxingogo/Documents/UnityProject/Casting/OneSideWar/Assets/Plugins/WuxingogoExtension/Editor/WuxingogoEditor.dll")
    # copyfile(currPath()+"/" + runtimeSourceFile,"/Users/Wuxingogo/Documents/UnityProject/Casting/OneSideWar/Assets/Plugins/WuxingogoExtension/Plugins/WuxingogoRuntime.dll")

    copyfile(currPath()+"/" + editorSourceFile,"/Users/wuxingogo/Documents/UnityProject/MyProject/Wuliao/Assets/Plugins/WuxingogoExtension/Editor/WuxingogoEditor.dll")
    copyfile(currPath()+"/" + runtimeSourceFile,"/Users/wuxingogo/Documents/UnityProject/MyProject/Wuliao/Assets/Plugins/WuxingogoExtension/Plugins/WuxingogoRuntime.dll")
    # CopyToProject("/Users/Wuxingogo/Documents/UnityProject/Casting/OneSideWar/Assets/Plugins/WuxingogoExtension/")
    # CopyToProject("/Users/wuxingogo/Documents/Github/Unity_Shaders_Book-master/Assets/Plugins/WuxingogoExtension/")
    # CopyToProject("/Users/wuxingogo/Documents/Github/GameUpdater/Assets/Plugins/WuxingogoExtension/")
    CopyToProject("/Users/apple/Documents/MusicAndroid/Music/Assets/Plugins/WuxingogoExtension/")
    CopyToProject("/Users/wuxingogo/Documents/UnityProject/MusicCopy/Assets/Plugins/WuxingogoExtension/")
    CopyToProject("/Users/wuxingogo/Documents/UnityProject/Music/Assets/Plugins/WuxingogoExtension/")
    CopyToProject("/Users/apple/Documents/Projects_LoveTwoBalls_iOS/Assets/Plugins/WuxingogoExtension/")
    CopyToProject("/Users/apple/Documents/Github/19HelixArrow/Project/Twisty Arrow/Arrow/Assets/Twisty Arrow/Plugins/WuxingogoExtension/")
    CopyToProject("/Users/apple/Documents/Github/2DPhysics/2DPhysics/Assets/Plugins/WuxingogoExtension/")
    CopyToProject("/Users/wuxingogo/Documents/UnityProject/SplitTexture/split_texture/Assets/Plugins/WuxingogoExtension/")
#print currPath()  + "OutPutDll\WuxingogoEditor.dll"



#copyfile( currPath()  + "\OutPutDll\WuxingogoEditor.dll", "E:/Work/UnityProject/New Unity Project/Assets/WuxingogoExtension/Editor/WuxingogoEditor.dll")
#copyfile( currPath()  + "\OutPutDll\WuxingogoRuntime.dll", "E:\Work\UnityProject\New Unity Project\Assets\WuxingogoExtension\Runtime\WuxingogoRuntime.dll")



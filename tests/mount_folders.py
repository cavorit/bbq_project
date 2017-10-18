import os, sys

def get_parent(folder:str) -> str:

    tmp = testfolder.split(sep='/')
    tmp.pop()
    return '/'.join(tmp)

def mount():
    sys.path.append(servicesfolder)
    sys.path.append(flaskfolder)

testfolder = os.path.abspath(os.path.dirname(__file__))
rootfolder = get_parent(testfolder)
servicesfolder  = rootfolder + '/services'  
flaskfolder = rootfolder + '/app' 

if __name__ == '__main__':
    
    my_paths = {'root' : rootfolder,
                'test' : testfolder,
                'services' : servicesfolder,
                'flask' : flaskfolder}    
    for key in my_paths:
        print(key + ':' + my_paths[key])




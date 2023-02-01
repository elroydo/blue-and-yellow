import requests

def main():
    res =  requests.get('https://google.com/')
    print(res.status_code)
    
    virtual()
    
    
import sys
import site

#creatng isolated virtual environments for external packages 
def virtual():
    print(f'platform: {sys.platform}')
    print('path: ', sys.prefix)
    
    print('pips: ', site.getsitepackages())
    
    #create folder for project and ves
    #create venv within folder
        #python -m venv project_env
        #activate (dep on shell, e.g., bat, ps1, etc.)
        #pip freeze > requirements.txt (packages)
        #where python
        #deactivate
        
    
main()

#upgrade all local packages
#pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
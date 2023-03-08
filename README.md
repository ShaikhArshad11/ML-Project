# ML-Project

# Machine-Learning-Project-Requirements

1. [Github Account](https://github.com/)
2. [Heroku Account](https://id.heroku.com/)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [Git cli](https://git-scm.com/downloads)


Creating Conda Enviornment
'''
conda create -p venv python==3.10 -y
'''

Activating Conda Enviornment
'''
conda activate venv/
'''
OR
'''
conda activate venv
'''

Installing requirement.txt
'''
pip install -r requirement.txt
'''

To add files to git
'''
git add .
'''
OR
'''
git add <file_name>
'''

Note: To ignore files or folder from git we write name of file/folder in .gitignore file

To check the git status 
'''
git status
'''

To check all version maintain by git
'''
git log
'''

 To create version/commit all changes by git
 '''
 git commit -m "message"
 '''

 To save version/changes to github
 '''
 git push origin main
 '''

 To check remote url
 '''
 git remote -v
 '''
 
 To setup CI/CD pipeline in heroku we need three information
 1. HEROKU_EMAIL = ***
 2. HEROKU_API_KEY = ***
 3. HEROKU_APP_NAME = 

 Build Docker Image
 '''
 docker build -t <image_name>:<tagname> .
 '''

Note: Image name for docker must be lowercase.


To list Docker image
'''
docker images
'''

Run docker image 
'''
docker run -p 5000:5000 -e PORT=5000 <image id>
'''

To check running containers in docker
'''
docker ps
'''

To stop docker container
'''
docker stop <container_id>
'''

'''
python setup.py install
'''

Install ipynb kernal
'''
pip install ipykernal
'''
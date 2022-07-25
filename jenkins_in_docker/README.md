# Downloading and running Jenkins in Docker
## Via macOs and Linux 
- Open up a terminal window.
- Create a bridge network in Docker using the following docker network create command:
```shell
docker network create jenkins
```
-In order to execute Docker commands inside Jenkins nodes, download and run the docker:dind Docker image using the following docker run command:
```shell
docker run \
  --name jenkins-docker \
  --rm \
  --detach \
  --privileged \
  --network jenkins \
  --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 2376:2376 \
  docker:dind \
  --storage-driver overlay2
```
##### 1
( Optional ) Specifies the Docker container name to use for running the image. By default, Docker will generate a unique name for the container.  
##### 2
( Optional ) Automatically removes the Docker container (the instance of the Docker image) when it is shut down.  
##### 3
( Optional ) Runs the Docker container in the background. This instance can be stopped later by running docker stop jenkins-docker.  
##### 4
Running Docker in Docker currently requires privileged access to function properly. This requirement may be relaxed with newer Linux kernel versions.  
##### 5 
This corresponds with the network created in the earlier step.  
##### 6 
Makes the Docker in Docker container available as the hostname docker within the jenkins network.  
##### 7 
Enables the use of TLS in the Docker server. Due to the use of a privileged container, this is recommended, though it requires the use of the shared volume described below. This environment variable controls the root directory where Docker TLS certificates are managed.  
##### 8 
Maps the /certs/client directory inside the container to a Docker volume named jenkins-docker-certs as created above.  
##### 9 
Maps the /var/jenkins_home directory inside the container to the Docker volume named jenkins-data. This will allow for other Docker containers controlled by this Docker container’s Docker daemon to mount data from Jenkins.  
##### 10 
( Optional ) Exposes the Docker daemon port on the host machine. This is useful for executing docker commands on the host machine to control this inner Docker daemon.  
##### 11 
The docker:dind image itself. This image can be downloaded before running by using the command: docker image pull docker:dind.  
##### 12 
The storage driver for the Docker volume. See "Docker storage drivers" for supported options.  


- Note: If copying and pasting the command snippet above does not work, try copying and pasting this annotation-free version here:
```shell
docker run --name jenkins-docker --rm --detach \
  --privileged --network jenkins --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 2376:2376 \
  docker:dind --storage-driver overlay2
```
- Build a new docker image from this Dockerfile and assign the image a meaningful name, e.g. "myjenkins-blueocean:2.346.2-1":
```shell
docker build -t myjenkins-blueocean:2.346.2-1 .
```

- Run your own myjenkins-blueocean:2.346.2-1 image as a container in Docker using the following docker run command:
```shell 
docker run \
  --name jenkins-blueocean \
  --restart=on-failure \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 7080:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.346.2-1 
```
##### 1
( Optional ) Specifies the Docker container name for this instance of the Docker image.  
##### 2
Always restart the container if it stops. If it is manually stopped, it is restarted only when Docker daemon restarts or the container itself is manually restarted.  
##### 3
( Optional ) Runs the current container in the background (i.e. "detached" mode) and outputs the container ID. If you do not specify this option, then the running Docker log for this container is output in the terminal window.  
##### 4 
Connects this container to the jenkins network defined in the earlier step. This makes the Docker daemon from the previous step available to this Jenkins container through the hostname docker.  
##### 5
Specifies the environment variables used by docker, docker-compose, and other Docker tools to connect to the Docker daemon from the previous step.  
##### 6
Maps (i.e. "publishes") port 8080 of the current container to port 7080 on the host machine. The first number represents the port on the host while the last represents the container’s port. Therefore, if you specified -p 49000:8080 for this option, you would be accessing Jenkins on your host machine through port 49000.  
##### 7
( Optional ) Maps port 50000 of the current container to port 50000 on the host machine. This is only necessary if you have set up one or more inbound Jenkins agents on other machines, which in turn interact with your jenkins-blueocean container (the Jenkins "controller"). Inbound Jenkins agents communicate with the Jenkins controller through TCP port 50000 by default. You can change this port number on your Jenkins controller through the Configure Global Security page. If you were to change the TCP port for inbound Jenkins agents of your Jenkins controller to 51000 (for example), then you would need to re-run Jenkins (via this docker run …​ command) and specify this "publish" option with something like --publish 52000:51000, where the last value matches this changed value on the Jenkins controller and the first value is the port number on the machine hosting the Jenkins controller. Inbound Jenkins agents communicate with the Jenkins controller on that port (52000 in this example). Note that WebSocket agents do not need this configuration.  
##### 8
Maps the /var/jenkins_home directory in the container to the Docker volume with the name jenkins-data. Instead of mapping the /var/jenkins_home directory to a Docker volume, you could also map this directory to one on your machine’s local file system. For example, specifying the option
--volume $HOME/jenkins:/var/jenkins_home would map the container’s /var/jenkins_home directory to the jenkins subdirectory within the $HOME directory on your local machine, which would typically be /Users/<your-username>/jenkins or /home/<your-username>/jenkins. Note that if you change the source volume or directory for this, the volume from the docker:dind container above needs to be updated to match this.  
##### 9
Maps the /certs/client directory to the previously created jenkins-docker-certs volume. This makes the client TLS certificates needed to connect to the Docker daemon available in the path specified by the DOCKER_CERT_PATH environment variable.  
##### 10
The name of the Docker image, which you built in the previous step.  

- Note: If copying and pasting the command snippet above does not work, try copying and pasting this annotation-free version here:
```shell
docker run --name jenkins-blueocean --restart=on-failure --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.346.2-1
```
### Post-installation setup wizard
#### Unlocking Jenkins
When you first access a new Jenkins instance, you are asked to unlock it using an automatically-generated password.
- Browse to http://localhost:7080 (or whichever port you configured for Jenkins when installing it) and wait until the Unlock Jenkins page appears.
- Open up a terminal window and type (example: docker logs 08b3e08ffd60):
```shell
docker logs {docker CONTAINER ID}
```
- From the Jenkins console log output, copy the automatically-generated alphanumeric password (between the 2 sets of asterisks).

![2022-07-25_10-53_37](https://user-images.githubusercontent.com/59145841/180726597-6af35090-0c2c-4524-b9e7-fa1a5e8251cf.png)

- Paste this code into the field ```Administrator password``` in the http://localhost:7080 and click [Continue] button

![2022-07-25_11-53_09](https://user-images.githubusercontent.com/59145841/180737869-b0a95ff7-fa11-4451-a501-451703b05e4f.png)

- Click tab ```Install suggested plugins```

![2022-07-25_11-51_50](https://user-images.githubusercontent.com/59145841/180738220-c0f77f3a-708f-4e2b-9a8d-0055ddc99cf7.png)
- Note:  
```Install suggested plugins``` - to install the recommended set of plugins, which are based on most common use cases.   
```Select plugins to install``` - to choose which set of plugins to initially install. When you first access the plugin selection page, the suggested plugins are selected by default.

#### Creating the first administrator user

Finally, after customizing Jenkins with plugins, Jenkins asks you to create your first administrator user. 
##### 1
When the Create First Admin User page appears, specify the details for your administrator user in the respective fields and click Save and Finish.  
##### 2  
When the Jenkins is ready page appears, click Start using Jenkins.  
Notes:  
- This page may indicate Jenkins is almost ready! instead and if so, click Restart.  
- If the page does not automatically refresh after a minute, use your web browser to refresh the page manually.  
##### 3 
If required, log in to Jenkins with the credentials of the user you just created and you are ready to start using Jenkins!

### To run a project inside Jenkins, you need:
- Copy the HTTPS path to this repository (point 1)
```shell
https://github.com/vladislav094/python-ui-framework.git
```
![2022-07-13_22-06_38](https://user-images.githubusercontent.com/59145841/178812825-2535ac6c-c087-447f-a321-d7438e1b840d.png)
- Open Jenkins in your local machine (point 1)
Enter into the address bar of the browser http://localhost:7080 / (Jenkins uses port:8080 by default) 
```shell
http://localhost:7080
```
- Create a new Job (point 2)
Click of the link 'Create Item'

![2022-07-13_22-25_11](https://user-images.githubusercontent.com/59145841/178815590-5352d7d2-0a4e-433b-98d8-5563c137577f.png)
- Fill input field with name of job (required field) (point 1):
```shell
ui_framework
```
- Choose type job: Pipeline (point 2)
- Click button [OK] (point 3)

![2022-07-13_22-29_10](https://user-images.githubusercontent.com/59145841/178816503-ac566223-be28-4f95-b1f5-6304887805ed.png)
- In the page that opens, click tab [Pipeline] (point 1)
- Expand the drop-down list: Definition (point 2)
- In the drop-dowp list select: Pipeline script from SCM (point 3)

![2022-07-13_22-35_44](https://user-images.githubusercontent.com/59145841/178818485-23d36038-e9a3-4397-b182-15a8a40e9cb7.png)
- Expand the drop-down list: SCM (point 1)
- In the drop-down list select: Git (point 2)
- In the input field "Repository URL" input HTTPS path for GitHub repo (point 3):
```shell
https://github.com/vladislav094/python-ui-framework.git 
```
- Do not change the drop-down list Credentials, because a public repo is used to launch this job (point 4)
- Enter in the input field "Branch Specifier (blank for 'any')": 
```shell
*/jenkins-in-docker
```
(this branch contains a test framework) (point 5)

![2022-07-13_22-56_35](https://user-images.githubusercontent.com/59145841/178825428-60334f3f-dd56-42dd-a518-4fd61555363c.png)

- In the input field "Script Path" enter:     
(This is a pipeline file that contains steps with commands: building a docker image, launching a docker container, as well as running tests of files with PyTest.The file is located in the root of the project) (point 1)
```shell
Jenkinsfile
```
- Click button [Save] (point 2)
![2022-07-13_23-10_19](https://user-images.githubusercontent.com/59145841/178829082-a5219d79-c5b8-4e85-95e3-790f582bcd84.png)

- On the job page click of the link 'Build' (point 1)

![2022-07-13_23-27_55](https://user-images.githubusercontent.com/59145841/178829224-698ab541-f17f-4cc0-8147-500f0800cfe2.png)

- Click on the link to view allure-report (point1)

![2022-07-25_12-22_48](https://user-images.githubusercontent.com/59145841/180744201-3f2ebef1-3d6b-4dc1-a1dc-ece454ac54a4.png)
![2022-07-25_12-24_41](https://user-images.githubusercontent.com/59145841/180744351-d007da7e-1fc8-4646-917d-f6242faa9d39.png)





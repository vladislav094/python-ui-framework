## Installing and running a test framework on a local machine
### Via Jenkins (local)
The developer of this framework expects that Jenkins (CI) is installed and configured on your local machine
#### To run a project inside Jenkins, you need:
- Copy the HTTPS path to this repository (point 1)
```shell
https://github.com/vladislav094/python-ui-framework.git
```
![2022-07-13_22-06_38](https://user-images.githubusercontent.com/59145841/178812825-2535ac6c-c087-447f-a321-d7438e1b840d.png)
- Open Jenkins in your local machine (point 1)
Enter into the address bar of the browser http://localhost:8080 / (Jenkins uses port:8080 by default) 
```shell
http://localhost:8080
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
- In the input field "Repository URL" input HTTPS path for GitHub repo (first step in README.md):
```shell
https://github.com/vladislav094/python-ui-framework.git 
```
- Do not change the drop-down list Credentials, because a public repo is used to launch this job (point 4)
- Enter in the input field "Branch Specifier (blank for 'any')": */master (this branch contains a test framework) (point 5)

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

#### Viewing job results (step-by-step output of execution):
- Click on a job in the build history (point 1)

![2022-07-13_23-50_07](https://user-images.githubusercontent.com/59145841/178908763-379b333e-5d2b-4a2e-9a36-5014e6523719.png)

- Click of the link 'Console Output'
 
![2022-07-13_23-50_30](https://user-images.githubusercontent.com/59145841/178909040-dfb14296-f6fa-4ada-83d1-426377bc5ddf.png)

- The page with the output of the execution steps

![2022-07-14_08-49_59](https://user-images.githubusercontent.com/59145841/178909684-92562cd5-7878-4e93-a794-8f9620cf6322.png)
![2022-07-14_08-50_20](https://user-images.githubusercontent.com/59145841/178909702-a7dd8b29-1a51-46cd-9bbc-1c8e78497050.png)
![2022-07-14_18-06_57](https://user-images.githubusercontent.com/59145841/179015143-ad72d967-43c4-45cd-a889-619729b704af.png)


#### Jenkinsfile (file with (pipeline) commands for performing job steps)
- The `--rm` flag deletes the docker container after execution (point 1)
- The `-e` flag sets the environment variables `RUN_HEADLESS=True` and launches the docker container with the browser in the mode `headless` (point 2)
- Flag `web_test` tag docker image (point 3)

![2022-07-15_00-03_56](https://user-images.githubusercontent.com/59145841/179085883-4a5ce15f-8a97-4e94-b0c1-283c095fb154.png)

#### Pytest.ini (configuration file for PyTest)
The file includes the flag --reruns=5 - the number of repeated runs of tests when falling (because the tested site may crash, due to public access and heavy load) (point 1)
```shell 
--reruns=5
```
- For the specified flag to work, the "pytest-rerunfailures" plugin was added to the project

![2022-07-14_09-18_32](https://user-images.githubusercontent.com/59145841/178914902-b6df7aab-6f4b-4d77-9dd2-0adb20df839f.png)

### Via Docker (local)
- Copy the HTTPS path to this repository (point 1)
```shell
https://github.com/vladislav094/python-ui-framework.git
```
![2022-07-13_22-06_38](https://user-images.githubusercontent.com/59145841/178812825-2535ac6c-c087-447f-a321-d7438e1b840d.png)

- Open a terminal (Linux):
```shell
command: [Ctrl + Alt + T]
```
- Make directory (point 2):
```shell
mkdir framework
```
- Change work directory (point 3):
```shell
cd framework
```
- Clone repository using HTTPS path (point 4):
```shell 
git clone https://github.com/vladislav094/python-ui-framework.git .
```
- Build a docker image and assign a tag using the '-t' flag (point 5):
```shell
docker build -t ui_framework . 
```
![2022-07-14_14-31_00](https://user-images.githubusercontent.com/59145841/178972923-9bae4e40-709b-4156-a543-9f72c8ff132a.png)

- Run a docker container with the execution of pytest test cases
```shell
docker run --rm -e RUN_HEADLESS=True ui_framework pytest
```
- The `--rm` flag deletes the docker container after execution
- The `-e` flag sets the environment variables `RUN_HEADLESS=True` and launches the docker container with the browser in the mode `headless`
- The `ui_framework` is a tag for the docker image

![2022-07-15_09-39_58](https://user-images.githubusercontent.com/59145841/179166246-442df012-0bef-431b-aa32-d42fce6295db.png)

#### Results run of the test cases in the docker container

![2022-07-14_17-13_52](https://user-images.githubusercontent.com/59145841/179003931-6f95f313-1f36-4ee9-8ed6-f7d6a6f4ed3c.png)

## Installing and running a test framework on a local machine
### GitHub repo in Jenkins (local)
The developer of this framework expects that Jenkins (CI) is installed and configured on your local machine
#### To run a project inside Jenkins, you need:
```shell
Copy the HTTPS path to this repository
```
![2022-07-13_22-06_38](https://user-images.githubusercontent.com/59145841/178812825-2535ac6c-c087-447f-a321-d7438e1b840d.png)
```shell
- Open Jenkins in your local machine (point 1)
Enter into the address bar of the browser http://localhost:8080 / (Jenkins uses port:8080) 
- Create a new Job (point 2)
Click of the link Create Item 
```
![2022-07-13_22-25_11](https://user-images.githubusercontent.com/59145841/178815590-5352d7d2-0a4e-433b-98d8-5563c137577f.png)
```shell
- Fill input field with name of job (required field) (point 1)
- Choose type job: Pipeline (point 2)
- Click button [OK] (point 3)
```
![2022-07-13_22-29_10](https://user-images.githubusercontent.com/59145841/178816503-ac566223-be28-4f95-b1f5-6304887805ed.png)
```shell
- In the page that opens, click tab [Pipeline] (point 1)
- Expand the drop-down list: Definition (point 2)
- In the drop-dowp list select: Pipeline script from SCM (point 3)
```
![2022-07-13_22-35_44](https://user-images.githubusercontent.com/59145841/178818485-23d36038-e9a3-4397-b182-15a8a40e9cb7.png)
```shell
- Expand the drop-down list: SCM (point 1)
- In the drop-down list select: Git (point 2)
- In the input field "Repository URL" input HTTPS path for GitHub repo (first step in README.md) (point 3)
- Do not change the drop-down list Credentials, because a public repo is used to launch this job (point 4)
- Enter in the input field "Branch Specifier (blank for 'any')": */master (this branch contains a test framework) (point 5)
```
![2022-07-13_22-56_35](https://user-images.githubusercontent.com/59145841/178825428-60334f3f-dd56-42dd-a518-4fd61555363c.png)
```shell
- In the input field "Script Path" enter: Jenkinsfile (This is a pipeline file that contains steps with commands: building a docker image, launching a docker container, as well as running tests of files with PyTest.
The file is located in the root of the project) (point 1)
- Click button [Save] (point 2)
```




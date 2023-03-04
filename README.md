# Work Out Manual
## Project Goal
1. Create a customized Docker container from the current version of Python that deploys a simple python script.
2. Push image to DockerHub, or Cloud based Container Registery (ECR)
3. Project should deploy automatically to Kubernetes cluster
4. Deployment should be to some form of Kubernetes service (can be hosted like Google Cloud Run or Amazon EKS, etc)

## Functionality
1. Calculate BMR for men and women
2. Suggest suitable calory intake for the whole day for people who want to lose weight healthly based on their BMR
3. Suggest breakdown calory intake for breakfast, lunch, dinner, and snack based on the whole day calory intake

## Run in local docker
the docker command already included in the Makefile
1. make all
2. make run



## Result
Url format:
function(calculate_bmr / suggest_diet) + gender(male / female) + weight(in kg) + height(in cm) + age + activity_factor(1-2)
Url: http://0.0.0.0:8080/calculate_bmr/male/80/172/23/1.5
![Dockerhub-demo](https://github.com/nogibjj/lyk-ids-project2/blob/main/calculate_bmr.png)


Url: http://0.0.0.0:8080/suggest_diet/male/80/172/23/1.5 
![Dockerhub-demo](https://github.com/nogibjj/lyk-ids-project2/blob/main/suggest_diet.png)


## Push to dockerhub
![Dockerhub-demo](https://github.com/nogibjj/lyk-ids-project2/blob/main/Dockerhub.png)


## Use of MiniKubes
![MiniKubes-demo1](https://github.com/nogibjj/lyk-ids-project2/blob/main/MiniKube1.png)
![MiniKubes-demo2](https://github.com/nogibjj/lyk-ids-project2/blob/main/MiniKube2.png)


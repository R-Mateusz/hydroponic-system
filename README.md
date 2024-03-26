# hydroponic-system
**DEV Manual:**

Specified docker commands describe launching the app: 
* _**docker ps**_ - View containers list 
* _**docker exec -it [id] bash**_ - Enter specific container 
* _**docker-compose build [container_name]**_ - Build container 
* _**docker-compose up**_ - Run containers 
* _**docker-compose down**_ - Stop containers 

Application urls:
* **_localhost:8000/admin/_** - admin page
* **_localhost:8000/systems/_** - view hydroponic systems list of specific user
* **_localhost:8000/systems/[id]_** - view specific hydroponic system with measurements details
* **_localhost:8000/app-auth_** - log in page
* **_localhost:8000/scheme_** - download scheme docs with .yml extension
* **_localhost:8000/scheme/docs_** - view API documentation

Kubernetes:

* **_minikube dashboard_** - Shows management dashboard of docker images 
* **_minikube start_** - Starts a local Kubernetes cluster
* **_minikube stop_** - Stop a local Kubernetes cluster
* **_minikube pause_** - pause Kubernetes
* **_minikube unpause_** - unpause Kubernetes
* **_minikube status_** - check Kubernetes cluster status
* **_minikube image load {image}_**- load docker image 
* **_kubectl apply -k ._** - apply changes in a configuration to resource by file name

**NOTE:**

After some attempts to load image for Kubernetes of app-web docker container, by command _minikube image load app-web_, an error shows up:
"_X Exiting due to GUEST_IMAGE_LOAD: Failed to load image: save to dir: caching images: caching image "path/...": write: unable to calculate manifest: blob sha256:XXXX not found_"


**Possible fix solution:**
Downgrade docker desktop to version X<25.0


**Application should be running from docker-level**



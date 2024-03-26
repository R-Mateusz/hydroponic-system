# hydroponic-system
**DEV Manual:**

Specified docker commands describe launching the app: 
* View containers list '_**docker ps**_'
* Enter specific container '_**docker exec -it [id] bash**_'
* Build container '_**docker-compose build [container_name]**_'
* Run containers '_**docker-compose up**_'
* Stop containers '_**docker-compose down**_'

Application urls:
* **_localhost:8000/admin/_** - admin page
* **_localhost:8000/systems/_** - view hydroponic systems list of specific user
* **_localhost:8000/systems/[id]_** - view specific hydroponic system with measurements details
* **_localhost:8000/app-auth_** - log in page
* **_localhost:8000/scheme_** - download scheme docs with .yml extension
* **_localhost:8000/scheme/docs_** - view API documentation

Kubernetes:

* **minikube dashboard** - Shows management dashboard of docker images 
* **minikube start** - Starts a local Kubernetes cluster
* **minikube stop** - Stop a local Kubernetes cluster
* **minikube pause** - pause Kubernetes
* **minikube unpause** - unpause Kubernetes
* **minikube status** - check Kubernetes cluster status
* **minikube image load {image}**- load docker image 
* **kubectl apply -k .** - apply changes in a configuration to resource by file name

**NOTE:**

After some attempts to load image for Kubernetes of app-web docker container, by command _minikube image load app-web_, an error shows up:
"_X Exiting due to GUEST_IMAGE_LOAD: Failed to load image: save to dir: caching images: caching image "path/...": write: unable to calculate manifest: blob sha256:XXXX not found_"


**Possible fix solution:**
Downgrade docker desktop to version X<25.0


**Application should be running from docker-level**



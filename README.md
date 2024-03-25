# hydroponic-system
**DEV Manual:**

Specified docker commands describe launching the app: 
1. View containers list '_**docker ps**_'
2. Enter specific container '_**docker exec -it [id] bash**_'
3. Build container '_**docker-compose build [container_name]**_'
4. Run containers '_**docker-compose up**_'
5. Stop containers '_**docker-compose down**_'

Application urls:
* **_localhost:8000/admin/_** - admin page
* **_localhost:8000/systems/_** - view hydroponic systems list of specific user
* **_localhost:8000/systems/[id]_** - view specific hydroponic system with measurements details
* **_localhost:8000/app-auth_** - log in page
* **_localhost:8000/scheme_** - download scheme docs with .yml extension
* **_localhost:8000/scheme/docs_** - view API documentation


# Dockerfile [22 Nov 2022 Homework]

## Docker & Podman primary differences

| Item            | Docker                              | Podman                              |
| --------------- | ----------------------------------- | ----------------------------------- |
| Architecture    | Daemon                              | Daemon-less (Systemd service)       |
| Privileges      | Require root privileges             | Normal user                         |
| Security        | Attacker gains access to OS as root | As normal doesn't have access to OS |
| Building images | Self-sufficiente                    | Buildah assisted                    |
| Package         | All in one, monolitic               | Modular approach, specialized tools |

## Creating a React project in a container

1. Create a Dockerfile with folder explorer or using:

```
touch Dockerfile
```

2. In the same folder create a project React project using:

```bash
npx create-react-app react-dockerized-app
```

3. Open Dockerfile and write:

```Dockerfile
#FROM is used to setup the base image, in this case node:16 (Look for more images at https://hub.docker.com/)
FROM node:16
#WORKDIR is establish container work directory
WORKDIR /usr/src/react-dockerized-app
#EXPOSED is used to select the port to be exposed (In this case using 3000 because is the React default port)
EXPOSE 3000
#CMD runs commands whent getting up the container. In this case runs the app
CMD npm start
```

3. In directory where Dockerfile is located, run the following command to build the Docker image:

```bash
#Example: Change <image name> for the name you want to assign
docker build . -t <image name>
```

4. Confirm your image has been created by using

```bash
docker images
```

5. Run the container based on the created image by using

```bash
docker run -v <local/absolute/path/direction>/react-dockerized-app:/usr/src/app/react-dockerized-app -p 3000:3000 -d --name <container name> <project name>
#Use -p to redirect a public port to a private port inside the container (In this case we will se the exposed port 3000 in localhost:3000)
#Use -d to detach the container
#Use --name to assign a name to the container so it can be easily to start and stop
#Use -v to connect a local directory with a directory inside the container
```

6. Use a browser and go to `http://localhost:3000/`. To test React is working.

7. To stop the container use:

```
docker stop <container name>
```

8. In case you want to run the container again use:

```
docker start <container name>
```

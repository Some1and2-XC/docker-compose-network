# Demo Docker-Compose network
## Configuration Notes
### Web Server
 - Internal IP : `10.20.0.1`
 - Net Domain : `web-app`
### SQL
 - Internal IP : `10.20.0.2`
 - Net Domain : `dtb-app`
 - MySQL is setup such that all the files for the data get saved to the host computer, this is done with volumes on the docker compose file. 
### NGINX
 - Internal IP : `10.20.0.3`
 - Net Domain : `rev-prox`
 - NGINX connects to the WWW interal server by connecting to the web-app:5000 alias. 
 - NGINX connects its port 80 to host port 80. 
## To Run
 - To start the service up, simply make sure that the docker daemon is running & run the following command at the root directory of the project: `docker compose up -d`. 

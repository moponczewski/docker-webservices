# docker-webservices 

Three webservices, each running in a docker container, doing nothing more than a whalesay with startrek quote.

This is a short and simple demo of interacting containerized webservices each located in a docker container and connected through a local docker network, running on one docker host. The "cow-webservice" is outputting a whalesay (which is a modified cowsay) quote of combined output from the "date-webservice" and the "fortune-webservice" (using StarTrek quotes).
All webservices are created with the Flask microframework for Python (http://flask.pocoo.org/docs/0.11/license/), credits to the docker team for the docker.cow file used in the cow-webservice.

What else...
- docker and docker-compose are necessary (tested with docker v1.12.1 and docker-compose v1.8.0)
- the docker images are based on Ubuntu 16.04 (fortune & cowsay) and Alpine Linux (date)
- as cowsay is a commandline tool with ascii output it looks not that nice in a web browswer, use curl instead

## 1) Get the code
Clone the git repo to your local machine
`$ git clone https://github.com/moponczewski/docker-webservices`
the `cd` into the directory and perform the following steps

## 2) Build and start... 
###### ...from scratch 
docker-compose grabs the docker-compose.yml file and starts building the docker images, based on the Dockerfiles in each build directory, maps ports and volumes if necessary, names the image and containers and finally fires the containers. Due to not using the `-d` flag the combined output from all webservices will be displayed in the terminal window.  

```
$ docker-compose up
```

###### ...in case of changes
If necessary to restart the containerized services remove the already existing containers first and start docker-compose with command `--build` to rebuild images and start the containers. 

```
$ docker ps -aq | xargs docker rm -f
$ docker-compose up --build
```

## 3) Finally let it run

$ docker-compose has been started not daemonized/ detached, so use curl in a separate terminal 

```
$ curl localhost/cow
```



## This is how it looks like
<pre>
 _______________________________
/ Thu Sep 8 20:36:09 UTC 2016   \
|                               |
| Request from: curl/7.47.0     |
|                               |
| Beam me up, Scotty, theres no |
\ intelligent life down here!   /
 -------------------------------
    \
     \
      \     
                    ##        .            
              ## ## ##       ==            
           ## ## ## ##      ===            
       /""""""""""""""""___/ ===        
  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~   
       \______ o          __/            
        \    \        __/             
          \____\______/   
</pre>



Have fun! 

# docker-webservices 

Three webservices, each running in a docker container, doing nothing more than a whalesay with startrek quote

This is a short demo of interacting webservices each located in a docker container and connected through a local docker network, running on one docker host. The "cow-webservice" is outputting a whalesay (which is a modified cowsay) quote of combined output from the "date-webservice" and the "fortune-webservice" (using StarTrek quotes).
All webservices are created with the Flask microframework for Python (http://flask.pocoo.org/docs/0.11/license/), credits to the docker team for the docker.cow file used in the cow-webservice.

What else...
- docker and docker-compose are necessary (tested with docker v1.12.1 and docker-compose v1.8.0)
- all docker images are built on Ubuntu 16.04
- the images are all equal (same tools installed), for productive environments use only the minimum set of installed tools
- as cowsay is a commandline tool with ascii output it looks not that nice in a web browswer, use curl instead


## BUILD AND START FROM SCRATCH
docker-compose is not daemonized, so use curl in a separate terminal 
```
docker-compose up
curl localhost/cow
```

## BUILD AND START IF NOT FROM SCRATCH
```
docker ps -aq | xargs docker rm -f
docker-compose up --build
curl localhost/cow
```

This is how it looks like
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

# Description
A console application that gets the last ten match results in League of Legends by summoner name. Can be used in a *Docker Container*

It can be executed with a simple python command, it is mandatory to use three parameters to make it work.

These are the mandatory parameters:

* -s,  --SUMMONER : Summoner Name.
* -r,  --REGION : Region (check -h --help for correct notation.).
* -k,  --KEY : Riot api key (A private key provided by Riot to utilize their apis ).

## How to use locally

1. Install requirements:

```bash
    $python3 -m pip install -r requirements.txt
```
2. Run App:

```bash
    $python3 prueba.py -s <SummonerName> -r <REGION> -k <API_KEY>
```

## How to use with Docker

First, go to [docker hub](https://hub.docker.com/r/javo3000/10matchespy/tags) and search for the image tag. or follow the next commands:

```bash
    $docker pull javo3000/10matchespy:latest
```

After download:

```bash
    $docker run javo3000/10matchespy:latest python prueba.py -s <SummonerName> -r <REGION> -k <API_KEY>
```
# Description
A console application that gets the lasts ten matches results of a summoner in League of Legends. Can be use in a *Docker Container*

It can be execute with a simple python command, it is mandatory to use three parameters to make it work.

This are the mandatory parameters:

* -s --SUMMONER : Summoner Name.
* -r --REGION : Region (check -h --help for correct notation.).
* -k --KEY : Riot api key (A private key provided by Riot to utilize their apis ).

## How to use localy

```bash
    $python3 prueba.py -s <SummonerName> -r <REGION> -k <API_KEY>
```

## How to use with Docker

First go to [docker hub](https://hub.docker.com/r/javo3000/10matchespy/tags) and search for the image tag. or follow the next commands:

```bash
    $docker pull javo3000/10matchespy:latest
```

After download:

```bash
    $docker run javo3000/10matchespy:latest -s <SummonerName> -r <REGION> -k <API_KEY>
```
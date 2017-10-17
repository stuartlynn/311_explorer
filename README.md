# 311 Explorer 

## What is this 

At the 311 DataJam in 2017 there was discussion of how we might create an opensource, high quality 311 dashboard that would give better insights into New York 311 data.
This is an attempt to build such a dashboard.

## Approatch

The approatch is to seperate out a ETL process that will grab new 311 calls daily, perform cleaning tasks on those dumps and ingest them in to a postgresql database.
In addition to this source of truth store, scripts will be run to produce derivative datasets.

Then a front end will be created using react + d3 to consume data from the postgresql database along with the derived data products to produce various ways
for people to interact with the 311 data.

## Proposed Data products 

- Database: The ground truth database that holds the raw 311 data 
- Extracts: Static dumps of the 311 data per community district for other people's ease of use
- Building Level Data: Aggregating the 311 data to PLUTO buildings to be able to show building level results 
- Probablisic Database: Would  be really interesting to get the 311 data into [BayesDB](http://probcomp.org/bayesdb/) to enable inference based queries 
- Vector Tiles: Might be interesting to produce a vector tile set for 311 over given areas.   

## Tools

- docker: [docker](https://www.docker.com/) To containerize everything.
- ETL: [Airflow](https://airflow.incubator.apache.org/) For organising the ETL process and running other tasks 
- Database: [Postgresql + PostGIS](https://www.postgresql.org/) For storing the ground truth data 
- Porbablistic Inference Engine: [BayesDB](http://probcomp.org/bayesdb/) For asking questions of the data.
- Vector Rendering: [Tangram]()
- Front end: [d3](https://reactjs.org/), [React](https://reactjs.org/), [semanticUI ?](https://semantic-ui.com/)

## Status / Roadmap

- [ ] Write ETL script that pulls in data from socrata each day 
- [ ] Write scripts to clean data: standardize zip codes, categories, etc 
- [ ] Write scripts to join with PLUTO data 
- [ ] Scripts for extracts 
- [ ] Simple query server 
- [ ] Mapping exploration
- [ ] Front end build out 

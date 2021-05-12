# MP-Distributed-Systems initial task

## Task 1

Functions written in go for this part can be found [here](https://github.com/BieVic/MP-Distributed-Systems/tree/master/task1) and contain 
* [hasher.go](https://github.com/BieVic/MP-Distributed-Systems/blob/master/task1/hasher.go): Simple function returning md5 hash of "Victor" + course. Example JSON request: { "course": "testCourse" }. If no course is specified it defaults to `course = "Master Project: Distributed Systems 2021"`
* [trigger.go](https://github.com/BieVic/MP-Distributed-Systems/blob/master/task1/trigger.go): Crawls an exchange rates api and filters for the EUR-USD exchange rate. Also saves the timestamp.

API used: 
* https://api.exchangerate-api.com/v4/latest/EUR

## Task 2

Functions written in python for this part can be found [here](https://github.com/BieVic/MP-Distributed-Systems/tree/master/task2) and contain
* [contaminated-food-checker.py](https://github.com/BieVic/MP-Distributed-Systems/tree/master/task2/contaminated-food-checker): Start the workflow by requesting the FDA api, which then picks randomly one contaminated food, sends the reason for the contamination to the sentiment-analysis function and lastly checks the returned polarity. If polarity > 0.0, request the positive-polarity-function, else the negative polarity-function. If a different gateway is used, the variable `gatewayURL` needs to be adjusted.
* [positive-polarity](https://github.com/BieVic/MP-Distributed-Systems/tree/master/task2/positive-polarity): Simple function responsing with a string.
* [negative-polarity](https://github.com/BieVic/MP-Distributed-Systems/tree/master/task2/negative-polarity): Request an inspirational quote from an open api and return it.

Additionally, the sentiment-analysis function from openfaas needs to be deployed via `faas-cli store deploy SentimentAnalysis`. 

A general workflow of all implemented functions can be seen here:
![Workflow graph](./workflow_graph.png?raw=true "Workflow graph")

API used: 
* https://api.fda.gov/food/enforcement.json?limit=20
* https://zenquotes.io/api/random

If you plan on deploying the functions, don't forget to add yml files for each function. For example for the **contaminated-food-checker.yml**:
```yml
version: 1.0
provider:
  name: openfaas
  gateway: <your-gateway-address>
functions:
  contaminated-food-checker:
    lang: python3
    handler: ./contaminated-food-checker
    image: <your-docker-hub-username>/contaminated-food-checker:latest
```
To deploy, run `faas-cli up -f contaminated-food-checker.yml`

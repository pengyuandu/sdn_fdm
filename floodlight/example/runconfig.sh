#!/bin/bash

curl -X POST -d '{"cmd":"ADD","dst-port":"1","dst-switch":"00:00:00:00:00:00:00:01","src-switch":"00:00:00:00:00:00:00:01","src-port":"1","requirement":"3.0"}' http://localhost:8080/wm/fdm/config/json

curl -X POST -d '{"cmd":"ADD","dst-port":"1","dst-switch":"00:00:00:00:00:00:00:05","src-switch":"00:00:00:00:00:00:00:05","src-port":"1","requirement":"3.0"}' http://localhost:8080/wm/fdm/config/json

curl -X POST -d '{"cmd":"ADD","dst-port":"1","dst-switch":"00:00:00:00:00:00:00:06","src-switch":"00:00:00:00:00:00:00:06","src-port":"1","requirement":"3.0"}' http://localhost:8080/wm/fdm/config/json

curl -X POST -d '{"cmd":"ADD","dst-port":"1","dst-switch":"00:00:00:00:00:00:00:07","src-switch":"00:00:00:00:00:00:00:07","src-port":"1","requirement":"3.0"}' http://localhost:8080/wm/fdm/config/json

curl -X POST -d '{"cmd":"ADD","dst-port":"1","dst-switch":"00:00:00:00:00:00:00:08","src-switch":"00:00:00:00:00:00:00:08","src-port":"1","requirement":"3.0"}' http://localhost:8080/wm/fdm/config/json

curl -X POST -d '{"cmd":"ADD","dst-port":"2","dst-switch":"00:00:00:00:00:00:00:04","src-switch":"00:00:00:00:00:00:00:03","src-port":"2","capacity":"10.0"}' http://localhost:8080/wm/fdm/config/json


curl -X POST -d '{"cmd":"ADD","dst-port":"1","dst-switch":"00:00:00:00:00:00:00:04","src-switch":"00:00:00:00:00:00:00:02","src-port":"2","capacity":"7.0"}' http://localhost:8080/wm/fdm/config/json

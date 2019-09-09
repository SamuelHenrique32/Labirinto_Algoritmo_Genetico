import { EventEmitter } from "events";
import axios from "axios";

EventEmitter.EventEmitter.defaultMaxListeners = 0;


class MazeStore extends EventEmitter {
    init = (callBack) => {
        this.axios = axios.get('http://localhost:8080/init', {
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(response => {
                if (typeof response.data !== "undefined") {
                    callBack(response.data)
                } else {
                    callBack({});
                }
            })
            .catch(e =>console.log(e));
    }

    getNextGeneration = (callBack) => {
        this.axios = axios.get('http://localhost:8080/next', {
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(response => {
                if (typeof response.data !== "undefined") {
                    callBack(response.data)
                } else {
                    callBack({});
                }
            })
            .catch();

    }

    getParams = (callBack) => {
        this.axios = axios.get('http://localhost:8080/params', {
            headers: {
                'Content-Type': 'application/json; charset=UTF-8',
                "Access-Control-Allow-Origin":"*",
                "Access-Control-Allow-Methods":"GET, POST, PUT, OPTIONS",
                "Access-Control-Allow-Headers": "Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token"
            },
        })
            .then(response => {
                console.log(response)
                if (typeof response.data !== "undefined") {
                    callBack(response.data)
                } else {
                    callBack({});
                }
            })
            .catch( e => console.log(e));
    }

    setParams = (callBack, params) => {
        console.log(params)
        this.axios = axios.post('http://localhost:8080/params', params, {
            headers: {
                'Content-Type': 'application/json; charset=UTF-8',
                "Access-Control-Allow-Origin": "*",
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
                'Access-Control-Allow-Headers': 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, X-HTTP-Method-Override'   ,
            }
        })
            .then(response => {
                console.log(response)
                if (typeof response.data !== "undefined") {
                    callBack(response.data)
                } else {
                    callBack({});
                }
            })
            .catch();
    }
}

const mazeStore = new MazeStore();

export default mazeStore;
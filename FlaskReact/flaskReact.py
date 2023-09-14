from flask import Flask
from flask import request, jsonify
players = [
{'id': 0,
'name': 'Opa',
'age': 80},
{'id': 1,
'name': 'Filip Filchev',
'age': 21},
{'id':2,
'name':'Filip Finch',
'age': 100}
]
app = Flask(__name__)
app.config["DEBUG"] = True
@app.route("/", methods=["GET", "POST"])
def home():
    return jsonify(players)
app.run()


"""

// Example React App

import React, {useEffect, useState} from 'react';
import './App.css';

function App() {

    useEffect(()=>{
        const [datata, setDatata] = useState([]);
        fetch('http://localhost:8000').then(response => response.json().then(data => {
            console.log(data);
            setDatata(data.datata);
        }) );
    }, []);

    return(
        <div className='App'>
            {datata.length}
        </div>
    );
}

export default App;
"""
const lib = require('weatherapi-Node');

//Config param and credentials
lib.Configuration.key = "e971d133174345acbcb143149222103";
var controller = lib.APIsController;

var q = '15217';
var lang = 'lang';

//text logging init @ output.txt
const fs = require('fs');
const myConsole = new console.Console(fs.createWriteStream('./output.txt'));

controller.getRealtimeWeather(q, lang, function(error, response, context) {
    myConsole.log(response);
    });

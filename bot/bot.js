var express    = require('express');        // call express
var app        = express();                 // define our app using express
var bodyParser = require('body-parser');
var token = "";
var request = require('request');


// configure app to use bodyParser()
// this will let us get the data from a POST
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 8082;        // set our port

// ROUTES FOR OUR API
// =============================================================================
var router = express.Router();              // get an instance of the express Router


// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get('/', function(req, res) {

  if (req.query['hub.verify_token'] === 'gababot') {
    res.send(req.query['hub.challenge']);
  }
  res.send('Error, wrong validation token');
});


router.post('/', function(req, res) {

  messaging_events = req.body.entry[0].messaging;
  for (i = 0; i < messaging_events.length; i++) {
    event = req.body.entry[0].messaging[i];
    sender = event.sender.id;
    if (event.message && event.message.text) {
      text = event.message.text;
      text = text.toLowerCase();
      // Handle a text message from this sender
      if (text === 'generic') {
        sendGenericMessage(sender);
        continue;
      }

    }

      if (event.postback) {
        postbackValue = JSON.parse(JSON.stringify(event.postback));
        payloadValue = postbackValue.payload;
        console.log("PAYLOAD IS " + payloadValue);

        if (payloadValue === 'payload') {
          sendTextMessage(sender,columbiaUniversityDescription);
          sendImage(sender,"http://i.imgur.com/QCk6oGa.jpg");
          //sendEducationDetails(sender);
          continue;
        }

      }
  }
  res.send(200);

});

const ttn = require('ttn');

data = ttn.data;
application = ttn.application;
 
const appID = ""
const accessKey = ""
 
data(appID, accessKey)
  .then(function (client) {
    client.on("uplink", function (devID, payload) {
      console.log("Received uplink from ", devID)
      console.log(payload)
    })
  })
  .catch(function (err) {
    console.error(err)
    process.exit(1)
  })
 
application(appID, accessKey)
  .then(function (client) {
    return client.get()
  })
  .then(function (app) {
    console.log("Got app", app)
  })
  .catch(function (err) {
    console.error(err)
    process.exit(1)
  })
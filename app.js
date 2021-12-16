// set up express and body-parser
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 8000;
var path = require('path')
app.use(bodyParser.urlencoded({ extended: true }));

// set up three pages (index, about, and newsletter pages)
app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, "/index.html"))
});
app.get('/about', function (req, res) {
  res.sendFile(path.join(__dirname, "/about.html"))
});
app.get('/newsletter', function (req, res) {
  res.sendFile(path.join(__dirname, "/newsletter.html"))
});

// add subscriber to mailing list
app.post("/newsletter", function (req, res) {
  // read in values from form submission
  const firstName = req.body.fName;
  const lastName = req.body.lName;
  const email = req.body.email;
  
  // Write values to CSV containing mailing list
  // With help from: https://stackabuse.com/reading-and-writing-csv-files-with-node-js/
  function adding() {
    const createCsvWriter = require('csv-writer').createObjectCsvWriter;
    const csvWriter = createCsvWriter({
      path: 'subscribers.csv',
      append: true,
      header: [
        { id: 'firstName', title: 'firstName' },
        { id: 'lastName', title: 'lastName' },
        { id: 'email', title: 'email' }
      ]
    });
    
    const data = [{
      firstName: firstName,
      lastName: lastName,
      email: email
    }];

    csvWriter.writeRecords(data).then(() => console.log('Subscriber added successfully.'));
    return "subscribed";
  }

  // show success or failure pages
  async function run() {
    try {
      const response = await adding();
      if (response === "subscribed")
        res.sendFile(path.join(__dirname, "/success.html"));
    }
    catch (error) {
      var e = error["response"]["text"]
      console.log(e)
      res.sendFile(path.join(__dirname, "/failure.html"));
    }
  }
  run();
});

app.listen(process.env.PORT || port, () => {
  console.log(`The server is running at http://localhost:${port}`)
});

// Learned about Node JS from the following links:
// https://expressjs.com/en/guide/routing.html
// https://javascript.plainenglish.io/how-to-set-up-your-own-newsletter-for-free-41929018aae6
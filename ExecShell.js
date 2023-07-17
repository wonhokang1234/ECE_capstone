const express = require('express')
const app = express()

// respond with "hello world" when a GET request is made to the homepage
app.get('/', (req, res) => {
  res.send('received request')
  const { exec } = require("child_process");

  exec("bash ./../automation.sh", (error, stdout, stderr) => {
      if (error) {
          console.log(`error: ${error.message}`);
      }
      if (stderr) {
          console.log(`stderr: ${stderr}`);
      }
      console.log(`stdout: ${stdout}`);
  });
})

app.listen(3000, () => {
    console.log(
      'server is running at http://172.26.109.155:3000'
    );
});

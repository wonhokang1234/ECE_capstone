// server.js

const express = require('express');
const multer = require('multer');
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());

const storage = multer.diskStorage({
  destination(req, file, callback) {
    callback(null, './uploads/');
  },
  filename(req, file, callback) {
    let filename = Date.now() + '.png';
    req.body.file = filename;
    callback(null, filename);
  },
});

const upload = multer({ limits: { fieldSize: 10 * 1024 * 1024 }, storage: storage });

app.get('/', (req, res) => {
  res.status(200).send('You can post to /api/upload.');
});

app.post('/api/upload', upload.single('photo'), (req, res) => {
  const file = req.file;
  if (!file) {
    console.log('fuck me');
  }
  console.log(req.body);
  console.log(req.body.file);
  // console.log('file', req.files);
  // console.log('body', req.body);
  res.status(200).json({
    message: 'success!',
  });
});

app.listen(3000, () => {
  console.log(
    'server is running at http://10.0.0.84:3000'
  );
});
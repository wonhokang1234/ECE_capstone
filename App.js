import React from "react";
import { NativeRouter as Router, Route, Routes } from "react-router-native";

import AddPhoto from "./AddPhotoScreen";
import Home from "./Home";
import Setup from "./Setup";
import End from "./End";

function App() {
  return (
    <Router>
      <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/addPhoto" element={<AddPhoto />} />
      <Route path="/setup" element={<Setup />} />
      <Route path="/end" element={<End />} />
    </Routes>
   </Router>
  );
}

export default App;
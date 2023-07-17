import React from 'react';
import axios from "axios";
import { View, Image, Button } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import { useLocation } from 'react-router-dom';
import { useNavigate } from "react-router-dom";
import { StyleSheet } from 'react-native';
import { useEffect } from 'react';

const SERVER_URL = 'https://sheet.best/api/sheets/725a3d83-79cc-4a91-90ec-aefe53604c53';
const LOCALHOST_URL = 'http://10.0.0.84:3000';

function AddPhoto() {
  const location = useLocation();
  const category = location.state.category_;
  const typeOfClothing = location.state.type_;
  const formality = location.state.formality_;
  const length = location.state.length_;
  const season = location.state.season_;
  const color = location.state.color_;
  console.log(location.state.category_);
  console.log(location.state.type_);
  console.log(location.state.formality_);
  console.log(location.state.length_);
  console.log(location.state.season_);
  console.log(location.state.color_);
  const [photo, setPhoto] = React.useState(null);
  const [displayUrl, setDisplayUrl] = React.useState("");
  let navigate = useNavigate();

  const handleChoosePhoto = async() => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.All,
      allowsEditing: true,
      quality: 1,
    });
    setPhoto(result);
  };

  const logChange = useEffect(() => {
    console.log('new value of display url ', displayUrl);
  }, [displayUrl]);

  function cloudinaryUpload(photo) {
    const data = new FormData()
    data.append('file', photo)
    data.append('upload_preset', 'imageuploads')
    data.append("cloud_name", "dmunxqdae")
    fetch("https://api.cloudinary.com/v1_1/dmunxqdae/upload", {
      method: "POST",
      body: data
    }).then(res => res.json()).
      then(data => {
        console.log(data.secure_url);
        setDisplayUrl(data.secure_url);
      });
  }

  const handleUploadPhoto = () => {
    const uri = photo.uri;
    const type = photo.type;
    let name = photo.fileName;
    if(typeof photo.fileName === "undefined"){
        var getFilename = uri.split("/");
        name = getFilename[getFilename.length - 1];
    }
    const source = {
      uri,
      type,
      name,
    }
    cloudinaryUpload(source);
    logChange;
    axios.post(SERVER_URL, { displayUrl })
    .then((response) => {
      console.log(response);
    });
  };

  const uploadToSpreadsheet = () => {
    axios.post(SERVER_URL, { category, typeOfClothing, formality, length, season, color, displayUrl })
    .then((response) => {
      console.log(response);
    })
    // axios.post(SERVER_URL, {  })
    // .then((response) => {
    //   console.log(response);
    // });
  }

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      {photo && (
        <>
          <Image
            source={{ uri: photo.uri }}
            style={{ width: 300, height: 300 }}
          />
          <Button title="Upload Photo" onPress={handleUploadPhoto} />
        </>
      )}
      <Button title="Choose Photo" onPress={handleChoosePhoto} />
      <View style={styles.space} />
      <Button title="Finished" onPress={() => {uploadToSpreadsheet(); navigate("/setup")}} />
      <View style={styles.space} />
      <Button title="Add another" onPress={() => {uploadToSpreadsheet(); navigate("/")}} />
    </View>
  );
};

const styles = StyleSheet.create({
  space: {
    // width: 20, // or whatever size you need
    height: 50,
  },
})

export default AddPhoto;

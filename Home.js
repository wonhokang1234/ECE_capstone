// Home.js

import axios from "axios";
import React from "react";
import { View, StyleSheet, Button } from "react-native";
import { Text } from "react-native";
import { useNavigate } from "react-router-dom";
import DropDownPicker from 'react-native-dropdown-picker';

function Home() {
  const uri = 'https://sheet.best/api/sheets/725a3d83-79cc-4a91-90ec-aefe53604c53'
  const [open, setOpen] = React.useState(false);
  const [open1, setOpen1] = React.useState(false);
  const [open2, setOpen2] = React.useState(false);
  const [open3, setOpen3] = React.useState(false);
  const [open4, setOpen4] = React.useState(false);
  const [open5, setOpen5] = React.useState(false);

  const [category, setValue] = React.useState(null);
  const [typeOfClothing, setValue1] = React.useState(null);
  const [formality, setValue2] = React.useState(null);
  const [length, setValue3] = React.useState(null);
  const [season, setValue4] = React.useState(null);
  const [color, setValue5] = React.useState(null);

  const [categoryOpt, setCategory] = React.useState([
    {label: 'Top', value: 'top'},
    {label: 'Bottom', value: 'bottom'},
    {label: 'Accessory', value: 'accessory'}
  ]);
  const [colorOpt, setColor] = React.useState([
    {label: 'Black', value: 'black'},
    {label: 'Silver', value: 'silver'},
    {label: 'Gray', value: 'gray'},
    {label: 'White', value: 'white'},
    {label: 'Brown', value: 'brown'},
    {label: 'Light Blue', value: 'lightblue'},
    {label: 'Blue', value: 'blue'},
    {label: 'Dark Blue', value: 'darkblue'},
    {label: 'Purple', value: 'purple'},
    {label: 'Dark Red', value: 'darkred'},
    {label: 'Red', value: 'red'},
    {label: 'Pink', value: 'pink'},
    {label: 'Orange', value: 'orange'},
    {label: 'Light Yellow', value: 'lightyellow'},
    {label: 'Yellow', value: 'yellow'},
    {label: 'Dark Yellow', value: 'darkyellow'},
    {label: 'Light Green', value: 'lightgreen'},
    {label: 'Green', value: 'green'},
    {label: 'Dark Green', value: 'darkgreen'},
  ]);
  const [typeOfClothingOpt, setTypeOfClothing] = React.useState([
    {label: 'Shirt', value: 'shirt'},
    {label: 'Sweater', value: 'sweater'},
    {label: 'Hoodie', value: 'hoodie'},
    {label: 'Suit', value: 'suit'},
    {label: 'Jacket', value: 'jacket'},
    {label: 'Coat', value: 'coat'},
    {label: 'Dress', value: 'dress'},
    {label: 'Pants', value: 'pants'},
    {label: 'Skirt', value: 'skirt'},
    {label: 'Scarf', value: 'scarf'},
    {label: 'Hat', value: 'hat'}
  ]);
  const [formalityOpt, setFormality] = React.useState([
    {label: 'Formal', value: 'formal'},
    {label: 'Informal', value: 'informal'}
  ]);
  const [lengthOpt, setLength] = React.useState([
    {label: 'Long', value: 'long'},
    {label: 'Short', value: 'short'},
    {label: 'Sleeveless', value: 'sleeveless'}
  ]);
  const [seasonOpt, setSeason] = React.useState([
    {label: 'Summer', value: 'summer'},
    {label: 'Spring', value: 'spring'},
    {label: 'Winter', value: 'winter'}
  ]);

  let navigate = useNavigate();


  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Category</Text>
      <DropDownPicker
        style={{width: 300, height: 40}}
        containerStyle={{alignContent: "center", alignItems: "center", zIndex: 1000}}
        dropDownDirection="AUTO"
        dropDownContainerStyle={{zIndex: 1000, width: 300}}
        placeholder="Select the category"
        open={open}
        value={category}
        items={categoryOpt}
        setOpen={setOpen}
        setValue={setValue}
        setItems={setCategory}
      />
      <View style={styles1.space} />

      <Text>Type</Text>
      <DropDownPicker
        style={{width: 300, height: 40}}
        containerStyle={{alignContent: "center", alignItems: "center", zIndex: 800}}
        dropDownDirection="AUTO"
        dropDownContainerStyle={{zIndex: 800, width: 300}}
        placeholder="Select the type of clothing"
        open={open1}
        value={typeOfClothing}
        items={typeOfClothingOpt}
        setOpen={setOpen1}
        setValue={setValue1}
        setItems={setTypeOfClothing}
      />
      <View style={styles1.space} />

      <Text>Formality</Text>
      <DropDownPicker
        style={{width: 300, height: 40}}
        containerStyle={{alignContent: "center", alignItems: "center", zIndex: 600}}
        dropDownDirection="AUTO"
        dropDownContainerStyle={{zIndex: 600, width: 300}}
        placeholder="Select the formality"
        open={open2}
        value={formality}
        items={formalityOpt}
        setOpen={setOpen2}
        setValue={setValue2}
        setItems={setFormality}
      />
      <View style={styles1.space} />

      <Text>Length</Text>
      <DropDownPicker
        style={{width: 300, height: 40}}
        containerStyle={{alignContent: "center", alignItems: "center", zIndex: 400}}
        dropDownDirection="AUTO"
        dropDownContainerStyle={{zIndex: 400, width: 300}}
        placeholder="Select the length"
        open={open3}
        value={length}
        items={lengthOpt}
        setOpen={setOpen3}
        setValue={setValue3}
        setItems={setLength}
      />
      <View style={styles1.space} />

      <Text>Color</Text>
      <DropDownPicker
        style={{width: 300, height: 40}}
        containerStyle={{alignContent: "center", alignItems: "center", zIndex: 200}}
        dropDownDirection="BOTTOM"
        dropDownContainerStyle={{zIndex: 200, width: 300}}
        placeholder="Select the color"
        open={open5}
        value={color}
        items={colorOpt}
        setOpen={setOpen5}
        setValue={setValue5}
        setItems={setColor}
      />
      <View style={styles1.space} />

      <Text>Season</Text>
      <DropDownPicker
        style={{width: 300, height: 40}}
        containerStyle={{alignContent: "center", alignItems: "center", zIndex: 100}}
        dropDownDirection="BOTTOM"
        dropDownContainerStyle={{zIndex: 100, width: 300}}
        placeholder="Select the season"
        open={open4}
        value={season}
        items={seasonOpt}
        setOpen={setOpen4}
        setValue={setValue4}
        setItems={setSeason}
      />
      <View style={styles1.space} />

      <Button
        title="Next"
        style={{zIndex: 1}}
        onPress={() => {
          // axios.post(uri, { category, typeOfClothing, formality, length, season, color })
          // .then((response) => {
          //   console.log(response);
          // })
          navigate("/addPhoto", {state: {category_: category, type_: typeOfClothing, formality_: formality, length_: length, season_: season, color_: color}});
      }}
      />
    </View>
    
  )
}

const styles = StyleSheet.create({
  input: {
    height: 40,
    width: 300,
    margin: 12,
    borderWidth: 1,
    padding: 10,
  },
});

const styles1 = StyleSheet.create({
  space: {
    // width: 20, // or whatever size you need
    height: 30,
  },
})

export default Home;
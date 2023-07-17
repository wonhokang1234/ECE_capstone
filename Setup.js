// Setup.js
// we want two buttons (formal or informal)
// then a start button at the button which runs 
import React from "react";
import { TextInput, View, StyleSheet, Button } from "react-native";
import { Text } from "react-native";
import { useNavigate } from "react-router-dom";

function Setup() {
  let navigate = useNavigate();
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
    <Text style={styles.title}>
      Choose your formality.
    </Text>
    <Button
      title="Formal"
      onPress={() => {
        console.log("requested formal attire");
        navigate("/end");
      }}
    />
    <Button
      title="Informal"
      onPress={() => {
        console.log("request informal attire");
        navigate("/end");
      }}
    />
  </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    marginHorizontal: 16,
  },
  title: {
    textAlign: 'center',
    marginVertical: 8,
  },
  fixToText: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  separator: {
    marginVertical: 8,
    borderBottomColor: '#737373',
    borderBottomWidth: StyleSheet.hairlineWidth,
  },
});

export default Setup;
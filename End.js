import React from "react";
import { TextInput, View, StyleSheet, Button } from "react-native";
import { Text } from "react-native";

const SERVER_URL = 'http://172.26.109.155:3000'

function End() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
    <Text style={styles.title}>
      Start outfit recommendation!
    </Text>
    <Button
      title="Start"
      onPress={() => {
        console.log("starting outfit recommendation script");
        fetch(`${SERVER_URL}`, {
          method: 'GET',
        })
        .then((response) => console.log(response.json()))
        .catch((error) => console.log('error:', error));
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

export default End;
import { InputBox } from "./InputBox";
import { Configuration, OpenAIApi } from "openai";
import React, { useState } from 'react';

const configuration = new Configuration({
  apiKey: process.env.REACT_APP_API_Key,

 
});
const openai = new OpenAIApi(configuration);

function App() {
  const [userPrompt, setUserPrompt] = useState("skinned sida patient");
  //const [number, setNumber] = useState(1);
  //const [size, setSize] = useState("256x256");
  const [imageUrl, setImageUrl] = useState("");

  const generateImage = async () => {
   
    const imageParameters = {
      prompt: userPrompt,
      n: 1,
      size: "256x256",
    };
   
    const response = await openai.createImage(imageParameters);
    const urlData = response.data.data[0].url;
    setImageUrl(urlData);

  };
  return (
    
    <main className="App">
      
      {imageUrl && <img src={imageUrl} className="image" alt="imageUrl" />}
      <InputBox label={"Description"} setAttribute={setUserPrompt} />
      
      <button className="main-button" onClick={generateImage}>Generate</button>
      
    </main>
  );
}

export default App;

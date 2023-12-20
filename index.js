const express = require("express");
const app = express();
const { Recorder } = require("node-rtsp-recorder");
const path = require("path");

app.use(express.json());

app.post("/start-recording", (req, res) => {
  const { rtspUrl, stationName, subtitleText } = req.body;
  if (!rtspUrl || !stationName) {
    return res.status(400).send("RTSP URL과 관측소 이름이 필요합니다.");
  }

  const rec = new Recorder({
    url: rtspUrl,
    timeLimit: 60, // 각 비디오 파일의 녹화 시간 (초)
    folder: path.join(__dirname, `/recordings/`),
    name: "cam1",
    stationName: stationName,
    subtitleText: subtitleText,
  });

  // 녹화 시작
  rec.startRecording();

  setTimeout(() => {
    console.log("녹화 중지");
    rec.stopRecording();
  }, 30000); // 이 예제에서는 15초 후에 녹화를 중지

  res.send(`${stationName} 관측소의 녹화가 시작되었습니다.`);
});

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`server ${PORT}`);
});

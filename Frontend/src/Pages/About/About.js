// import React from "react";
// import "./Style.scss";

// const About = () => {
//   const handleScriptSubmit = (script) => {
//     fetch("/run_script", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({ script }),
//     }).then((response) => {
//       // Handle response if needed
//       console.log("Script executed:", script);
//     });
//   };

//   const handleStopScript = () => {
//     fetch("/stop_script", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//     }).then((response) => {
//       // Handle response if needed
//       console.log("Script stopped.");
//     });
//   };

//   return (
//     <>
//       <h1 className="two_h">Face Detection and Tracking</h1>
//       <div className="containerr">
//         <button
//           className="box"
//           onClick={() => handleScriptSubmit("face_detection")}
//         >
//           Face Detection
//         </button>
//         <button
//           className="box"
//           onClick={() => handleScriptSubmit("face_tracking")}
//         >
//           Head Target
//         </button>
//         <button
//           className="box"
//           onClick={() => handleScriptSubmit("tracking_system")}
//         >
//           Track Motion
//         </button>
//         <button className="stop-button" onClick={handleStopScript}>
//           Stop Script
//         </button>
//       </div>
//     </>
//   );
// };

// export default About;

import React, { useState } from "react";
import "./Style.scss";

function About() {
  const [status, setStatus] = useState("");

  const handleScriptAction = async (script, action) => {
    const url = action === "start" ? "/run_script" : "/stop_script";
    const data = action === "start" ? { script } : {};

    try {
      const response = await fetch(`http://127.0.0.1:5000${url}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      const result = await response.json();
      setStatus(result.status);
    } catch (error) {
      console.error("Error:", error);
      setStatus("Error communicating with the server");
    }
  };

  return (
    <>
      <h1 className="two_h">Face Detection and Tracking</h1>
      <div className="containerr">
        <button
          className="box"
          onClick={() => handleScriptAction("face_detection", "start")}
        >
          Face Detection
        </button>
        <button
          className="box"
          onClick={() => handleScriptAction("face_tracking", "start")}
        >
          Head Target
        </button>
        <button
          className="box"
          onClick={() => handleScriptAction("tracking_system", "start")}
        >
          Track Motion
        </button>
        <button
          className="stop-button"
          onClick={() => handleScriptAction("", "stop")}
        >
          Stop Script
        </button>
      </div>
      {status && <p>Status: {status}</p>}
    </>
  );
}

export default About;

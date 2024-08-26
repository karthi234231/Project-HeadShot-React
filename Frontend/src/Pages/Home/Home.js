import React from "react";
import "../Home/Style.scss";
import { motion } from "framer-motion";
import me from "../../Assets/Images/file.png";
import { animations } from "../../Styles/Animations/Animations";
import Socials from "../../Components/Socials/Socials";

const Home = () => {
  return (
    <>
      <div className="home">
        <div className="info-section">
          <motion.h1 {...animations.h1}>
            P<span className="span_one">R</span>O<span className="span_one">J</span>E<span className="span_one">C</span>T : <br />
            <span>H</span>E<span>A</span>D <span>S</span>H<span>O</span>T
          </motion.h1>
          <motion.h3 {...animations.fade}>A Full Stack Developer</motion.h3>
          <motion.p {...animations.fade}>
            This is an Webiste to showcase, <br /> My Machine learning HeadShot Project🎯.
          </motion.p>
          <Socials />
        </div>
        <div className="image-section">
          <img src={me} alt="" />
        </div>
      </div>
    </>
  );
};

export default Home;

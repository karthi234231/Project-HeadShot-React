import React from "react";
import "../Socials/Style.scss";
import {
  AiFillInstagram,
  AiFillLinkedin,

  AiOutlineGithub,
} from "react-icons/ai";

const socialIcons = [
  {
    Component: AiOutlineGithub,
    color: "#4078c0",
    link: "https://github.com/karthi234231",
  },
  {
    Component: AiFillInstagram,
    color: "#26a7de",
    link: "https://twitter.com/dev_palwar2",
  },
  {
    Component: AiFillLinkedin,
    color: "#0072b1",
    link: "https://www.linkedin.com/in/karthikjogi/",
  },
];

const Socials = () => {
  return (
    <div className="icons">
      {socialIcons.map(({ Component, color, link }, index) => (
        <a href={link} target="_blank" rel="noreferrer" key={index}>
          <Component style={{ color }} />
        </a>
      ))}
    </div>
  );
};

export default Socials;

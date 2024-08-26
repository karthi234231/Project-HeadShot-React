import React, { useState } from "react";
import "../Work/Style.scss";
import Card from "../../Components/Card/Card";
import Data from "../../Assets/project-data.json";
import Heading from "../../Components/Heading/Heading";
import { LoadMore } from "../../Components/Loader/Loader";


const Work = () => {
  const [projects, setProjects] = useState(Data.slice(0, 5));
  const [showAllProjects, setShowAllProjects] = useState(false);
  const [display, setDisplay] = useState("none");

  const handleShowAllProjects = () => {
    setProjects(Data);
    setShowAllProjects(true);
    setDisplay(null);
  };
  setTimeout(() => {
    window.scrollTo({
      top: 199,
      behavior: "smooth",
    });
  }, 200);

  return (
    <div className="work">
      <Heading Heading={"my work"} />


      <div className="cards">
        {projects.map((value) => (
          <Card
            key={value.id}
            heading={value.heading}
            url={value.link}
            image={value.img}
            github={value.github}
          />
        ))}
        {!showAllProjects && (
          <LoadMore
            image={Data[5].img}
            heading={"Show More"}
            onClick={handleShowAllProjects}
          />
        )}
      </div>
    </div>
  );
};

export default Work;

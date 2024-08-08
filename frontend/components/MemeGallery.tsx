"use client";
import React, { useState, useEffect } from "react";
import Image from "next/image";

const MemeGallery = () => {
  const [memes, setMemes] = useState([]);

  useEffect(() => {
    const apiUrl =
      process.env.NODE_ENV === "production"
        ? "https://tamil-meme-database.onrender.com"
        : "http://localhost:8000";
    fetch(apiUrl + "/memes")
      .then((response) => response.json())
      .then((data) => setMemes(data));
  }, []);

  console.log(memes);

  const images = [
    "https://picsum.photos/200/300",
    "https://picsum.photos/200/300",
    "https://picsum.photos/200/300",
    "https://picsum.photos/200/300",
    "https://picsum.photos/200/300",
    "https://picsum.photos/200/300",
  ];

  return (
    <section className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6 p-4 md:p-6">
      {memes.map((memes, index) => (
        <div
          className="justify-center items-center group relative overflow-hidden rounded-lg"
          key={index}
        >
          <Image src={memes} alt="Meme" width={200} height={200} />
        </div>
      ))}
    </section>
  );
};

export default MemeGallery;

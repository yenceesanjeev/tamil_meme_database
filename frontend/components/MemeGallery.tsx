import React from "react";
import Image from "next/image";

const images = [
  "https://picsum.photos/200/300",
  "https://picsum.photos/200/300",
  "https://picsum.photos/200/300",
  "https://picsum.photos/200/300",
  "https://picsum.photos/200/300",
  "https://picsum.photos/200/300",
];

const MemeGallery = () => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
      {images.map((image, index) => (
        <div className="bg-gray-200 rounded-md p-4" key={index}>
          <Image
            src={image}
            alt="Meme"
            width={500}
            height={500}
            className="rounded-md"
          />
        </div>
      ))}
    </div>
  );
};

export default MemeGallery;

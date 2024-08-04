import React from "react";

const SearchBar = () => {
  return (
    <div className="min-w-[300px] items-center justify-center">
      <input
        className="w-full p-2 border-2 border-gray-300 rounded-md"
        placeholder="Search for Tamil Memes"
      />
    </div>
  );
};

export default SearchBar;

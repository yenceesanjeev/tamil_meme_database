"use client";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { Input } from "@/components/ui/input";
import React from "react";
import { Button } from "@/components/ui/button";
import { useState, useEffect } from "react";

const AddMeme = () => {
  const [memeUrl, setMemeUrl] = useState("");
  const [memeName, setMemeName] = useState("");

  const handleAddMeme = async () => {
    const apiUrl =
      process.env.NODE_ENV === "production"
        ? "https://tamil-meme-database.onrender.com"
        : "http://localhost:8000";
    const response = await fetch(`${apiUrl}/add-memes`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ image_url: memeUrl, meme_name: memeName }),
    });
    const data = await response.json();
    console.log(data);
  };

  return (
    <Popover>
      <PopoverTrigger asChild>
        <Button variant="outline">Add Meme</Button>
      </PopoverTrigger>
      <PopoverContent>
        <div className="flex flex-col gap-4">
          <Input
            id="meme-url"
            onChange={(e) => setMemeUrl(e.target.value)}
            type="text"
            placeholder="Meme URL"
          />
          <Button className="w-32" onClick={handleAddMeme}>
            Add Meme
          </Button>
        </div>
      </PopoverContent>
    </Popover>
  );
};

export default AddMeme;

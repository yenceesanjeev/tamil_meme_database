"use client";
import React, { useState } from "react";
import { useRouter } from "next/navigation";

const MemeUploader = () => {
  const [isUploading, setIsUploading] = useState(false);
  const router = useRouter();

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setIsUploading(true);

    const formData = new FormData();
    formData.append("meme", file);

    try {
      const response = await fetch("/api/upload-meme", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        console.log("Meme uploaded successfully");
        router.refresh(); // Refresh the current route
      } else {
        console.error("Failed to upload meme");
      }
    } catch (error) {
      console.error("Error uploading meme:", error);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div>
      <input
        type="file"
        accept="image/*"
        onChange={handleUpload}
        style={{ display: "none" }}
        id="meme-upload"
      />
      <label htmlFor="meme-upload">
        <button disabled={isUploading}>
          {isUploading ? "Uploading..." : "Upload Meme"}
        </button>
      </label>
    </div>
  );
};

export default MemeUploader;

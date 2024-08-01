import React from "react";
import Header from "../components/Header";
import MemeUploader from "../components/MemeUploader";
import UserList from "../components/UserList";

export default function Home() {
  return (
    <div>
      <Header />
      <UserList />
    </div>
  );
}

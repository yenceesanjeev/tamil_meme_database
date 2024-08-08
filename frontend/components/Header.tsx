"use client";

import React from "react";
import {
  Command,
  CommandInput,
  CommandGroup,
  CommandItem,
} from "@/components/ui/command";
import { Button } from "@/components/ui/button";
import { BellIcon } from "lucide-react";
import { useState } from "react";
import AddMeme from "./AddMeme";

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

const Header = () => {
  return (
    <div className="flex gap-4 p-4 border-b justify-between items-center">
      <h1 className="text-xl"> Tamil Meme Database </h1>
      <AddMeme />
    </div>
  );
};

export default Header;

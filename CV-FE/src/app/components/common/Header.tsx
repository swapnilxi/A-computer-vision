import React from 'react'
import { Calendar, User } from "lucide-react";

export default function Header() {
 return (
    <header className="flex justify-end items-center p-4 bg-white shadow">
      <Calendar className="w-6 h-6 mx-2 text-gray-600 cursor-pointer" />
      <User className="w-6 h-6 mx-2 text-gray-600 cursor-pointer" />
    </header>
  )
}

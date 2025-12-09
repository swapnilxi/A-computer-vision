"use client"
import Link from "next/link";
import { Plus, ChevronLeft, ChevronRight } from "lucide-react";
import { useState } from "react";

export default function Sidebar() {
  const [isCollapsed, setIsCollapsed] = useState(false);
  const days = Array.from({ length: 40 }, (_, i) => i + 1);

  return (
    <aside className={`w-64 bg-gray-900 p-4 flex flex-col h-full transition-all duration-300 ${
      isCollapsed ? "w-16" : "w-64"
    }`}>
      <div className="flex items-center justify-between mb-6">
        <button className="flex items-center px-2 py-1 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors">
          <Plus className="w-5 h-5 mr-2" /> Day Labs
        </button>
        <button 
          className="p-2 rounded hover:bg-gray-800 transition-colors"
          onClick={() => setIsCollapsed(!isCollapsed)}
        >
          <ChevronLeft className={`w-5 h-5 text-white transition-transform ${
            isCollapsed ? "rotate-180" : ""
          }`} />
        </button>
      </div>

      <nav className="flex-1 overflow-y-auto">
        {days.map(day => (
          <Link
            key={day}
            href={`/day/${day}`}
            className={`block px-2 py-1 rounded transition-colors ${
              isCollapsed ? "text-center" : ""
            }`}
          >
            <span className="flex items-center justify-center w-full">
              <span className={`text-gray-300 hover:text-white transition-colors ${
                isCollapsed ? "opacity-0" : "opacity-100"
              }`}>Day </span>
              <span className="text-white">{day}</span>
            </span>
          </Link>
        ))}
      </nav>
    </aside>
  )
}

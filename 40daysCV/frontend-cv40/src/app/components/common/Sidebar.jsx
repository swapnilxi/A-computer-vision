import Link from "next/link";
import { Plus } from "lucide-react";

export default function Sidebar() {
  const days = Array.from({ length: 40 }, (_, i) => i + 1);

  return (
    <aside className="w-64 bg-gray-50 p-4 flex flex-col h-full">
      {/* Top "New Chat"-style icon button */}
      <button className="flex items-center px-2 py-1 mb-6 bg-blue-500 text-white rounded hover:bg-blue-600">
        <Plus className="w-5 h-5 mr-2" /> Day Labs
      </button>

      {/* Day-wise links */}
      <nav className="flex-1 overflow-y-auto">
        {days.map(day => (
          <Link
            key={day}
            href={`/day/${day}`}
            className="block px-2 py-1 rounded hover:bg-gray-100"
          >
            Day {day}
          </Link>
        ))}
      </nav>
    </aside>
  )
}

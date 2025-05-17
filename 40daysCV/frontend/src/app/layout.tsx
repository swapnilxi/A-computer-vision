import Sidebar from "./components/common/Sidebar";
import Header from "./components/common/Header";
import "@/app/globals.css";

export const metadata = {
  title: "Computer Vision Lab",
  description: "Day-wise CV exercises"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="flex h-screen">
        <Sidebar />
        <div className="flex-1 flex flex-col overflow-hidden">
          <Header />
          <main className="p-4 overflow-auto">{children}</main>
        </div>
      </body>
    </html>
  );
}

import NavBar from "@/components/NavBar";
import MemeGallery from "@/components/MemeGallery";
import Footer from "@/components/Footer";
import SearchBar from "@/components/SearchBar";
import Header from "@/components/Header";

export default function Home() {
  return (
    <main className="min-h-screen bg-white pb-16">
      <div className="mx-2">
        <Header />
        <div className="mx-6 px-4 my-6">
          <SearchBar />
          <MemeGallery />
        </div>
        <Footer />
      </div>
    </main>
  );
}

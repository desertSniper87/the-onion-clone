'use client';

import React, { useEffect, useState } from 'react';

interface Story {
  id: number;
  title: string;
  original: string;
  category: string;
  author: string;
}

export default function Home() {
  const [stories, setStories] = useState<Story[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/api/news')
      .then(res => res.json())
      .then(data => {
        setStories(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to fetch news:", err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center font-serif text-2xl">
        সংবাদ লোড হচ্ছে...
      </div>
    );
  }

  const featuredStory = stories[0];
  const sidebarStories = stories.slice(1, 5);
  const gridStories = stories.slice(5, 9);
  const opinionStories = stories.slice(9, 12);

  return (
    <main className="min-h-screen bg-[#fcfcfc] text-black p-4 md:p-8 font-serif">
      <header className="border-b-4 border-black pb-4 mb-8 text-center">
        <h1 className="text-6xl md:text-8xl font-black uppercase tracking-tighter">
          অনিয়ন বাংলা
        </h1>
        <div className="flex justify-between items-center mt-4 border-t border-black pt-2 text-sm uppercase font-sans font-bold">
          <span>ভলিউম ১, সংখ্যা ১</span>
          <span>{new Date().toLocaleDateString('bn-BD')}</span>
          <span>মূল্য: অমূল্য</span>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
        {/* Left Sidebar */}
        <div className="md:col-span-1 border-r border-gray-300 pr-4">
          <h2 className="text-xl font-bold border-b-2 border-black mb-4 uppercase">সংক্ষিপ্ত সংবাদ</h2>
          <div className="space-y-4">
            {sidebarStories.map(story => (
              <div key={story.id} className="border-b border-gray-200 pb-2">
                <h3 className="font-bold hover:underline cursor-pointer text-lg leading-tight">
                  {story.title}
                </h3>
                <p className="text-sm text-gray-600 mt-1">ক্যাটাগরি: {story.category}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Main Content */}
        <div className="md:col-span-2">
          {featuredStory && (
            <article className="mb-8">
              <h2 className="text-4xl md:text-5xl font-extrabold leading-tight mb-4 hover:underline cursor-pointer">
                {featuredStory.title}
              </h2>
              <div className="flex items-center text-sm text-gray-500 mb-4 font-sans">
                <span className="font-bold text-black mr-2">{featuredStory.author}</span> | <span>২ মিনিট আগে</span>
              </div>
              <p className="text-lg leading-relaxed text-justify">
                রাজধানীর ব্যস্ততম সড়কে এখন শুধুই পানির হাহাকার। তবে এই হাহাকার খাওয়ার পানির জন্য নয়, বরং গাড়ি চালানোর জন্য। গতকাল এক বিশেষ সংবাদ সম্মেলনে বিশেষজ্ঞরা দাবি করেন যে, এই ঘটনার পেছনে আসল খবর হলো: &quot;{featuredStory.original}&quot;।
              </p>
            </article>
          )}

          <div className="grid grid-cols-2 gap-4 border-t-2 border-black pt-4">
            {gridStories.map((story, index) => (
              <div key={story.id} className={`col-span-1 ${index % 2 !== 0 ? 'border-l border-gray-300 pl-4' : ''}`}>
                <h3 className="text-2xl font-bold leading-tight hover:underline cursor-pointer">{story.title}</h3>
                <p className="text-sm mt-2 leading-snug">সূত্র: {story.original}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Right Sidebar */}
        <div className="md:col-span-1 border-l border-gray-300 pl-4">
          <h2 className="text-xl font-bold border-b-2 border-black mb-4 uppercase">মতামত</h2>
          <div className="space-y-6">
            {opinionStories.map(story => (
              <div key={story.id} className="italic border-b border-gray-200 pb-4">
                <p className="font-bold text-lg hover:underline cursor-pointer">&quot;{story.title}&quot;</p>
                <p className="text-sm text-gray-600 mt-2">— {story.author}</p>
              </div>
            ))}
          </div>
        </div>
      </div>

      <footer className="mt-12 border-t-4 border-black pt-4 text-center text-sm font-sans font-bold uppercase">
        © ২০২৪ অনিয়ন বাংলা - আমরা সত্য বলি না
      </footer>
    </main>
  );
}

import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen bg-white">
      {/* Hero */}
      <section className="max-w-7xl mx-auto px-6 py-24 grid gap-12 md:grid-cols-2 items-center">
        <div className="space-y-6">
          <h1 className="text-4xl md:text-5xl font-extrabold text-slate-900 leading-tight">
            Manage Your System Efficiently
          </h1>
          <p className="text-lg text-slate-600">
            A simple overview for Users, Products, and Orders. Focused, clean,
            and ready to expand.
          </p>
          <div className="flex gap-4">
            <Link
              href="/signup"
              className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl font-bold shadow-lg shadow-blue-500/20 transition-all active:scale-[0.95]"
            >
              Get Started
            </Link>
            <Link
              href="#features"
              className="px-6 py-3 rounded-xl font-bold text-slate-700 border border-slate-300 hover:bg-slate-50 transition-all"
            >
              Learn More
            </Link>
          </div>
        </div>
        <div className="h-64 md:h-80 rounded-2xl bg-slate-100 border border-slate-200 flex items-center justify-center text-slate-400">
          System Preview
        </div>
      </section>

      {/* Simple Sections for Users, Products, Orders */}
      <section id="features" className="bg-slate-50 border-t border-slate-200">
        <div className="max-w-7xl mx-auto px-6 py-20 grid gap-8 md:grid-cols-3">
          {["Users", "Products", "Orders"].map((section) => (
            <div
              key={section}
              className="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm"
            >
              <div className="h-10 w-10 rounded-lg bg-blue-100 mb-4 flex items-center justify-center text-blue-600 font-bold">
                {section[0]}
              </div>
              <h3 className="font-bold text-slate-900 mb-2">{section}</h3>
              <p className="text-slate-600 text-sm">
                Quick overview placeholder for {section.toLowerCase()}{" "}
                management.
              </p>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}

import Link from "next/link";

// هدر جدید هماهنگ با فرم ثبت‌نام
export const Header = () => {
  return (
    <header className="sticky top-0 z-50 w-full bg-white/70 backdrop-blur-md border-b border-slate-100">
      <div className="container mx-auto px-6 h-16 flex justify-between items-center">
        {/* لوگو: استفاده از آبی فقط برای تاکید */}
        <h1 className="text-xl font-black tracking-tighter">
          <Link href="/" className="flex items-center gap-2">
            <span className="text-blue-600">●</span>
            <span className="text-slate-800">MyApp</span>
          </Link>
        </h1>

        <nav>
          <ul className="flex items-center gap-8">
            <li>
              <Link
                href="/signin"
                className="text-sm font-bold text-slate-500 hover:text-slate-800 transition-colors"
              >
                Sign In
              </Link>
            </li>
            <li>
              {/* دکمه ثبت نام: هماهنگ با استایل دکمه فرم اما با رنگ برند */}
              <Link
                href="/signup"
                className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2.5 rounded-xl text-sm font-bold shadow-lg shadow-blue-500/20 transition-all active:scale-[0.95]"
              >
                Get Started
              </Link>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

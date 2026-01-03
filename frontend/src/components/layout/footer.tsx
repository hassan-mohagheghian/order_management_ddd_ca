import Link from "next/link";

export const Footer = () => {
  return (
    <footer className="bg-white border-t border-slate-200">
      <div className="max-w-7xl mx-auto px-6 py-6 flex flex-col md:flex-row items-center justify-between text-sm text-slate-500">
        <p>© {new Date().getFullYear()} YourProduct. All rights reserved.</p>
        <div className="flex gap-4 mt-2 md:mt-0">
          <Link href="#" className="hover:text-slate-700 transition-colors">
            Privacy
          </Link>
          <Link href="#" className="hover:text-slate-700 transition-colors">
            Terms
          </Link>
          <Link href="#" className="hover:text-slate-700 transition-colors">
            Contact
          </Link>
        </div>
      </div>
    </footer>
  );
};

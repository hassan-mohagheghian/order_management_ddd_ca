// src/app/auth/signup/page.tsx
import { SigninForm } from "@/features/auth/components/signin-form";

export default function SigninPage() {
  return (
    <section className="min-h-[calc(100vh-(--spacing(16)))] bg-[radial-gradient(#e5e7eb_1px,transparent_1px)] bg-size-[16px_16px] bg-slate-50 flex items-center py-12 px-4">
      <div className="container mx-auto max-w-md">
        <div className="bg-white p-8 md:p-10 rounded-[2.5rem] shadow-xl shadow-slate-200/60 border border-slate-100">
          <div className="mb-10">
            <h1 className="text-3xl font-black text-slate-800  text-center tracking-tight">
              Sign in to Account
            </h1>
            <p className="text-center text-slate-400 mt-2 text-sm">
              Please enter you information
            </p>
          </div>
          <SigninForm />
          <div className="mt-8 pt-6 border-t border-slate-100 text-center">
            <p className="text-sm text-slate-500">
              Already have an account?{" "}
              <a
                href="/auth/login"
                className="text-blue-500 font-bold hover:text-blue-800 transition-colors"
              >
                Log in
              </a>
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

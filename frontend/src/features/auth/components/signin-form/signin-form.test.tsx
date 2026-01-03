import { render, screen } from "@testing-library/react";
import { vi, describe, test, expect } from "vitest";
import { SigninForm } from "./signin-form";
import { useSignin } from "@/features/auth/hooks/use-signin";

vi.mock("@/features/auth/hooks/use-signin");

describe("SigninForm", () => {
  test("should render form elements", () => {
    (useSignin as any).mockReturnValue({
      mutate: vi.fn(),
      isPending: false,
      error: null,
    });

    render(<SigninForm />);

    expect(
      screen.getByPlaceholderText(/name@example.com/i)
    ).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/••••••••/i)).toBeInTheDocument();
    expect(
      screen.getByRole("button", { name: /sign in/i })
    ).toBeInTheDocument();
  });

  test("in loading state the button must be disabled", () => {
    (useSignin as any).mockReturnValue({
      mutate: vi.fn(),
      isPending: true,
      error: null,
    });

    render(<SigninForm />);

    const button = screen.getByRole("button");
    expect(button).toBeDisabled();
    expect(screen.getByText(/Signing up.../i)).toBeInTheDocument();
  });

  test("handle errors", () => {
    const mockErrorMessage = "Incorrect password";

    (useSignin as any).mockReturnValue({
      mutate: vi.fn(),
      isPending: false,
      error: { message: mockErrorMessage },
    });

    render(<SigninForm />);

    const errorBox = screen.getByText(mockErrorMessage);
    expect(errorBox).toBeInTheDocument();
    expect(errorBox).toHaveClass("text-red-500");
    expect(errorBox).toHaveClass("animate-shake");
  });
});

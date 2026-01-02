import { useMutation } from "@tanstack/react-query";
import { useRouter } from "next/navigation"
import { signup } from "../api/signup";


export const useSignup = () => {
    const router = useRouter();
    return useMutation({
        mutationFn: signup,
        onSuccess: () => {
            router.push("/");
        },
        onError: (error) => {
            console.error("Signup failed:", error);
        }
    });
}

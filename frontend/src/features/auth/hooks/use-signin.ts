import { useMutation } from "@tanstack/react-query";
import { useRouter } from "next/navigation"
import { signin } from "../api/signin";


export const useSignin = () => {
    const router = useRouter();
    return useMutation({
        mutationFn: signin,
        onSuccess: () => {
            router.push("/");
        },
    });
}

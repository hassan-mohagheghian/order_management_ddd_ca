import { SignupPayload, SignupResponse } from "../types";


export const signin = async (data: SignupPayload): Promise<SignupResponse> => {
    const response = await fetch("http://localhost:8000/users/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });
    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || "Failed to sign in");
    }
    return response.json()
}
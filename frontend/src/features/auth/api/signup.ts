import { SignupPayload, SignupResponse } from "../types";


export const signup = async (data: SignupPayload): Promise<SignupResponse> => {
    const response = await fetch("http://localhost:8000/users/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });
    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || "Failed to sign up");
    }
    return response.json()
}
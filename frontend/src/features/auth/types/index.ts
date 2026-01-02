export type SignupPayload = {
    name: string;
    email: string;
    password: string;
};

export type SignupResponse = {
    id: string;
    name: string;
    email: string;
    role: string;
};
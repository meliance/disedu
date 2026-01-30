import axios from "./axios";

export const loginUser = async (email, password) => {
  const response = await axios.post("/accounts/login/", {
    email,
    password,
  });
  return response.data;
};

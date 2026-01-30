import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/api";

const axiosInstance = axios.create({
  baseURL: BASE_URL,
});

axiosInstance.interceptors.request.use(
  (config) => {
    const auth = JSON.parse(localStorage.getItem("auth"));
    if (auth?.access) {
      config.headers.Authorization = `Bearer ${auth.access}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default axiosInstance;

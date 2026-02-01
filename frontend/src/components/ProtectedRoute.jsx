import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";

const ProtectedRoute = ({ children }) => {
  const token = localStorage.getItem("access");

  if (!token) {
    return <Navigate to="/login" />;
  }

  try {
    const decoded = jwtDecode(token);

    if (decoded.role === "student") {
      return children;
    }

    if (decoded.role === "admin") {
      return <Navigate to="/admin-dashboard" />;
    }

  } catch (err) {
    localStorage.clear();
    return <Navigate to="/login" />;
  }

  return children;
};

export default ProtectedRoute;

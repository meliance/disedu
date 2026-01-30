import { Navigate, Outlet } from "react-router-dom";
import { useContext } from "react";
import AuthContext from "../context/AuthContext";

const RequireAuth = ({ allowedRoles }) => {
  const { auth } = useContext(AuthContext);

  if (!auth) return <Navigate to="/login" />;

  if (
    allowedRoles &&
    !allowedRoles.includes(auth.user.role)
  ) {
    return <Navigate to="/unauthorized" />;
  }

  return <Outlet />;
};

export default RequireAuth;

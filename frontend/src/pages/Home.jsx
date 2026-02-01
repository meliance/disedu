import { Link } from "react-router-dom";

const Home = () => {
  const access = localStorage.getItem("access");

  return (
    <div className="min-h-screen flex flex-col justify-center items-center bg-gray-100">
      <h1 className="text-4xl font-bold text-blue-600 mb-4">
        Student Registration System
      </h1>

      <p className="text-gray-600 mb-8 text-center max-w-md">
        Manage course registration, payments, approvals,
        and academic records in one centralized platform.
      </p>

      {access ? (
        <Link
          to="/dashboard"
          className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
        >
          Go to Dashboard
        </Link>
      ) : (
        <div className="space-x-4">
          <Link
            to="/login"
            className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
          >
            Login
          </Link>

          <Link
            to="/register"
            className="border border-blue-600 text-blue-600 px-6 py-2 rounded hover:bg-blue-50"
          >
            Register
          </Link>
        </div>
      )}
    </div>
  );
};

export default Home;

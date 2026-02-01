import { Link } from "react-router-dom";

const Home = () => {
  const access = localStorage.getItem("access");

  return (
    <div style={{ padding: "60px", textAlign: "center" }}>
      <h1>Student Registration System</h1>
      <p>
        Welcome to the SRS platform. Manage registrations, payments,
        and academic records easily.
      </p>

      <div style={{ marginTop: "30px" }}>
        {access ? (
          <Link to="/dashboard">
            <button>Go to Dashboard</button>
          </Link>
        ) : (
          <>
            <Link to="/login">
              <button style={{ marginRight: "10px" }}>Login</button>
            </Link>

            <Link to="/register">
              <button>Register</button>
            </Link>
          </>
        )}
      </div>
    </div>
  );
};

export default Home;

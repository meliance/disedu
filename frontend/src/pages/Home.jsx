import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-50">

      {/* HERO SECTION */}
      <section className="bg-gradient-to-r from-blue-600 to-indigo-700 text-white">
        <div className="max-w-7xl mx-auto px-6 py-24 text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-6">
            Student Registration System
          </h1>
          <p className="text-lg md:text-xl mb-8 text-blue-100">
            Manage registrations, payments, and approvals easily in one platform.
          </p>

          <div className="flex justify-center gap-4">
            <Link
              to="/login"
              className="bg-white text-blue-700 px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition"
            >
              Login
            </Link>

            <Link
              to="/dashboard"
              className="border border-white px-6 py-3 rounded-lg font-semibold hover:bg-white hover:text-blue-700 transition"
            >
              Go to Dashboard
            </Link>
          </div>
        </div>
      </section>

      {/* FEATURES SECTION */}
      <section className="max-w-7xl mx-auto px-6 py-20">
        <h2 className="text-3xl font-bold text-center mb-12 text-gray-800">
          System Features
        </h2>

        <div className="grid md:grid-cols-3 gap-8">
          
          <div className="bg-white p-8 rounded-2xl shadow-md hover:shadow-xl transition">
            <h3 className="text-xl font-semibold mb-4 text-blue-600">
              Course Registration
            </h3>
            <p className="text-gray-600">
              Students can register for courses online and track approval status in real-time.
            </p>
          </div>

          <div className="bg-white p-8 rounded-2xl shadow-md hover:shadow-xl transition">
            <h3 className="text-xl font-semibold mb-4 text-indigo-600">
              Online Payments
            </h3>
            <p className="text-gray-600">
              Secure payment integration with Chapa for seamless tuition transactions.
            </p>
          </div>

          <div className="bg-white p-8 rounded-2xl shadow-md hover:shadow-xl transition">
            <h3 className="text-xl font-semibold mb-4 text-purple-600">
              Role-Based Dashboard
            </h3>
            <p className="text-gray-600">
              Different dashboards for students, registrar, finance, and admin users.
            </p>
          </div>

        </div>
      </section>

      {/* FOOTER */}
      <footer className="bg-gray-900 text-gray-300 text-center py-6">
        <p>© 2026 Student Registration System. All rights reserved.</p>
      </footer>

    </div>
  );
}

import React, { useEffect, useState } from "react";
import api from "../api/axios";

export default function Dashboard() {
  const [student, setStudent] = useState(null);

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        const res = await api.get("/api/students/dashboard/");
        setStudent(res.data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchDashboard();
  }, []);

  if (!student) return <div>Loading...</div>;

  return (
    <div>
      <h1>Welcome, {student.user_full_name}</h1>
      <p>Email: {student.user_email}</p>
      <p>Student ID: {student.student_id}</p>
      <p>Program: {student.program}</p>
      <p>Department: {student.department}</p>
      <p>Year: {student.year}</p>

      <h2>Registrations:</h2>
      {student.registrations.length === 0 ? (
        <p>No registrations yet</p>
      ) : (
        <ul>
          {student.registrations.map((reg) => (
            <li key={reg.id}>
              {reg.terms} - Paid: {reg.is_paid ? "Yes" : "No"} - Approved:{" "}
              {reg.is_approved ? "Yes" : "No"}
              <ul>
                {reg.courses.map((course) => (
                  <li key={course.id}>
                    {course.code} - {course.title} ({course.credit_hours} CH)
                  </li>
                ))}
              </ul>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

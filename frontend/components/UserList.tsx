"use client";
import React, { useEffect, useState } from "react";

interface User {
  id: number;
  name: string;
  email: string;
  profile_pic: string | null;
}

const UserList = () => {
  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const apiUrl =
          process.env.NODE_ENV === "production"
            ? "https://tamil-meme-database.onrender.com"
            : "http://localhost:8000";
        console.log("API URL:", apiUrl); // Add this line for debugging
        const response = await fetch(`${apiUrl}/users`);
        const data = await response.json();
        setUsers(data);
      } catch (error) {
        console.error("Error fetching users:", error);
      }
    };

    fetchUsers();
  }, []);

  return (
    <div className="mx-4">
      <h1 className="text-2xl font-bold mb-4">Users</h1>

      <div className="">
        <table className="w-96 divide-y-2 divide-gray-200 bg-white text-sm">
          <thead className="ltr:text-left rtl:text-right">
            <tr>
              <th className="whitespace px-4 py-2 font-medium text-gray-900">
                Name
              </th>
              <th className="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                Email
              </th>
              <th className="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                Profile Picture
              </th>
            </tr>
          </thead>

          <tbody className="divide-y divide-gray-200">
            {users.map((user) => (
              <tr key={user.id}>
                <td className="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                  {user.name}
                </td>
                <td className="whitespace-nowrap px-4 py-2 text-gray-700">
                  {user.email}
                </td>
                <td className="whitespace-nowrap px-4 py-2 text-gray-700">
                  {user.profile_pic ? (
                    <img
                      src={user.profile_pic}
                      alt={`${user.name}'s profile`}
                      className="w-10 h-10 rounded-full"
                    />
                  ) : (
                    "No picture"
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default UserList;

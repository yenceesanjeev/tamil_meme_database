import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [users, setUsers] = useState([]);
  const [newUser, setNewUser] = useState({ name: '', email: '', profile_pic: '' });

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    const response = await fetch('http://localhost:8000/users');
    const data = await response.json();
    setUsers(data);
  };

  const addUser = async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:8000/add_user', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newUser),
    });
    if (response.ok) {
      setNewUser({ name: '', email: '', profile_pic: '' });
      fetchUsers();
    }
  };

  const deleteUser = async (userId) => {
    const response = await fetch(`http://localhost:8000/users/${userId}`, {
      method: 'DELETE',
    });
    if (response.ok) {
      fetchUsers();
    }
  };

  return (
    <div className="App">
      <h1>User Management</h1>
      
      <form onSubmit={addUser}>
        <input
          type="text"
          placeholder="Name"
          value={newUser.name}
          onChange={(e) => setNewUser({ ...newUser, name: e.target.value })}
        />
        <input
          type="email"
          placeholder="Email"
          value={newUser.email}
          onChange={(e) => setNewUser({ ...newUser, email: e.target.value })}
        />
        <input
          type="text"
          placeholder="Profile Picture URL"
          value={newUser.profile_pic}
          onChange={(e) => setNewUser({ ...newUser, profile_pic: e.target.value })}
        />
        <button type="submit">Add User</button>
      </form>

      <button className="refresh-button" onClick={fetchUsers}>Refresh Users</button>

      <ul>
        {users.map((user) => (
          <li key={user.id}>
            <span>{user.name} ({user.email})</span>
            <button className="delete-button" onClick={() => deleteUser(user.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
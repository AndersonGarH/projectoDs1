import React, {useEffect, useState} from 'react';
import {Table} from 'react-bootstrap';
import {getAllUsers} from '../api/UserApi';
import "../App.css";

const Users = () => {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        let mounted = true;
        getAllUsers()
            .then(data => {
                if (mounted) {
                    setUsers(data)
                }
            })
        return () => mounted = false;
    }, [])

    return (
        <div className="container-fluid side-container">
            <div className="row side-row">
                <p id="before-table"></p>
                <Table striped bordered hover className="react-bootstrap-table" id="dataTable">
                    <thead>
                    <tr>
                        <th>No.</th>
                        <th>Username</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Identification</th>
                    </tr>
                    </thead>
                    <tbody>
                    {users.map((user) =>
                        <tr key={user.id}>
                            <td>{user.id}</td>
                            <td>{user.username}</td>
                            <td>{user.first_name}</td>
                            <td>{user.last_name}</td>
                            <td>{user.email}</td>
                            <td>{user.identification}</td>
                        </tr>)}
                    </tbody>
                </Table>
            </div>
        </div>
    );
};

export default Users;
import React,{ useEffect, useState }from 'react';
import {Table} from 'react-bootstrap';

import {Button,ButtonToolbar } from 'react-bootstrap';
import { FaEdit } from 'react-icons/fa';
import { RiDeleteBin5Line } from 'react-icons/ri';
import AddUserModal from "./AddUserModal";
import UpdateUserModal from "./UpdateUserModal";
import { getAllUsers, deleteUser } from '../api/UserApi';


const Manage = () => {
    const [users, setUsers] = useState([]);
    const [addModalShow, setAddModalShow] = useState(false);
    const [editModalShow, setEditModalShow] = useState(false);
    const [editUser, setEditUser] = useState([]);
    const [isUpdated, setIsUpdated] = useState(false);

    useEffect(() => {
        let mounted = true;
        if(users.length && !isUpdated) {
            return;
        }
        getAllUsers()
            .then(data => {
                if(mounted) {
                    setUsers(data);
                }
            })
        return () => {
            mounted = false;
            setIsUpdated(false);
        }
    }, [isUpdated, users])

    const handleUpdate = (e, user) => {
        e.preventDefault();
        setEditModalShow(true);
        setEditUser(user);
    };

    const handleAdd = (e) => {
        e.preventDefault();
        setAddModalShow(true);
    };

    const handleDelete = (e, userId) => {
        if(window.confirm('Are you sure ?')){
            e.preventDefault();
            deleteUser(userId)
                .then((result)=>{
                        alert(result);
                        setIsUpdated(true);
                    },
                    (error)=>{
                        alert("Failed to Delete User");
                    })
        }
    };

    let AddModelClose=()=>setAddModalShow(false);
    let EditModelClose=()=>setEditModalShow(false);
    return(
        <div className="container-fluid side-container">
            <div className="row side-row" >
                <p id="manage"></p>
                <Table striped bordered hover className="react-bootstrap-table" id="dataTable">
                    <thead>
                    <tr>
                        <th>No.</th>
                        <th>Username</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Identification</th>
                        <th>Action</th>
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
                            <td>
                                <Button className="mr-2" variant="danger"
                                        onClick={event => handleDelete(event, user.id)}>
                                    <RiDeleteBin5Line/>
                                </Button>
                                <span>&nbsp;&nbsp;&nbsp;</span>
                                <Button className="mr-2"
                                        onClick={event => handleUpdate(event, user)}>
                                    <FaEdit/>
                                </Button>
                                <UpdateUserModal show={editModalShow} user={editUser} setUpdated={setIsUpdated}
                                                 onHide={EditModelClose}></UpdateUserModal>
                            </td>
                        </tr>)}
                    </tbody>
                </Table>
                <ButtonToolbar>
                    <Button variant="primary" onClick={handleAdd}>
                        Add User
                    </Button>
                    <AddUserModal show={addModalShow} setUpdated={setIsUpdated}
                                  onHide={AddModelClose}></AddUserModal>
                </ButtonToolbar>
            </div>
        </div>
    );
};

export default Manage;
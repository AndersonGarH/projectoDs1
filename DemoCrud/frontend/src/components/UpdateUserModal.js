import React,{Component} from 'react';
import {Modal, Col, Row, Form, Button} from 'react-bootstrap';
import {FormControl, FormGroup, FormLabel} from 'react-bootstrap';
import { updateUser } from '../api/UserApi';



const UpdateUserModal = (props) => {

    const handleSubmit = (e) => {
        e.preventDefault();
        updateUser(props.user.id, e.target)
            .then((result)=>{
                    alert(result);
                    props.setUpdated(true);
                },
                (error)=>{
                    alert("Failed to Update User");
                })
    };

    return(
        <div className="container">

            <Modal
                {...props}
                size="lg"
                aria-labelledby="contained-modal-title-vcenter"
                centered >

                <Modal.Header closeButton>
                    <Modal.Title id="contained-modal-title-vcenter">
                        Update User Information
                    </Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Row>
                        <Col sm={6}>
                            <Form onSubmit={handleSubmit}>
                                <Form.Group controlId="username">
                                    <Form.Label>Username</Form.Label>
                                    <Form.Control type="text" name="Username" required defaultValue={props.user.username} placeholder="" />
                                </Form.Group>
                                <Form.Group controlId="first_name">
                                    <Form.Label>First Name</Form.Label>
                                    <Form.Control type="text" name="FirstName" required defaultValue={props.user.first_name} placeholder="" />
                                </Form.Group>
                                <Form.Group controlId="last_name">
                                    <Form.Label>Last Name</Form.Label>
                                    <Form.Control type="text" name="LastName" required defaultValue={props.user.last_name} placeholder="" />
                                </Form.Group>
                                <Form.Group controlId="email">
                                    <Form.Label>Email</Form.Label>
                                    <Form.Control type="text" name="Email" required defaultValue={props.user.email} placeholder="" />
                                </Form.Group>
                                <Form.Group controlId="identification">
                                    <Form.Label>Identification</Form.Label>
                                    <Form.Control type="text" name="Identification" required defaultValue={props.user.identification} placeholder="" />
                                </Form.Group>
                                <Form.Group>
                                    <p></p>
                                    <Button variant="primary" type="submit">
                                        Submit
                                    </Button>
                                </Form.Group>
                            </Form>
                        </Col>
                    </Row>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="danger" type="submit" onClick={props.onHide}>
                        Close
                    </Button>

                </Modal.Footer>
            </Modal>
        </div>
    );
};


export default UpdateUserModal;
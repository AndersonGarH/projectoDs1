import React from 'react';
import {Modal, Col, Row, Form, Button} from 'react-bootstrap';
import {FormControl, FormGroup, FormLabel} from 'react-bootstrap';
import { createUser } from '../api/UserApi';


const AddUserModal = (props) => {

    const handleSubmit = (e) => {
        e.preventDefault();
        createUser(e.target)
            .then((result)=>{
                    alert(result);
                    props.setUpdated(true);
                },
                (error)=>{
                    alert("Failed to Add User");
                })
    }

    return(
        <div className="container">

            <Modal
                {...props}
                size="lg"
                aria-labelledby="contained-modal-title-vcenter"
                centered >

                <Modal.Header closeButton>
                    <Modal.Title id="contained-modal-title-vcenter">
                        Fill In User Information
                    </Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Row>
                        <Col sm={6}>
                            <Form onSubmit={handleSubmit}>
                                <Form.Group controlId="username">
                                    <Form.Label>Username</Form.Label>
                                    <Form.Control type="text" name="username" required placeholder="" />
                                </Form.Group>
                                <Form.Group controlId="first_name">
                                    <Form.Label>First Name</Form.Label>
                                    <Form.Control type="text" name="first_name" required placeholder="" />
                                </Form.Group>
                                <Form.Group controlId="last_name">
                                    <Form.Label>Last Name</Form.Label>
                                    <Form.Control type="text" name="last_name" required placeholder="" />
                                </Form.Group>
                                <Form.Group controlId="email">
                                    <Form.Label>Email</Form.Label>
                                    <Form.Control type="text" name="email" required placeholder="" />
                                </Form.Group>
                                <Form.Group controlId="identification">
                                    <Form.Label>Identification</Form.Label>
                                    <Form.Control type="text" name="identification" required placeholder="" />
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

export default AddUserModal;
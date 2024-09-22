import React, { useState } from 'react';
import { TextInput, Button, Alert, AlertVariant } from '@patternfly/react-core';

const CustomerSearch = () => {
  const [custId, setCustId] = useState('');
  const [customer, setCustomer] = useState(null);
  const [error, setError] = useState('');

  const searchCustomer = () => {
    fetch(`http://127.0.0.1:5000/search_customer?cust_id=${custId}`)
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          setCustomer(null);
          setError(data.error);
        } else {
          setCustomer(data);
          setError('');
        }
      })
      .catch(err => {
        setError('Error fetching customer');
        setCustomer(null);
      });
  };

  return (
    <div>
      <h1>Customer Search</h1>
      <TextInput
        value={custId}
        type="text"
        onChange={setCustId}
        placeholder="Enter Customer ID"
      />
      <Button onClick={searchCustomer}>Search</Button>

      {error && (
        <Alert variant={AlertVariant.danger} title="Error">
          {error}
        </Alert>
      )}

      {customer && (
        <div>
          <h2>Customer Details</h2>
          <p><strong>ID:</strong> {customer.cust_id}</p>
          <p><strong>Name:</strong> {customer.name}</p>
          <p><strong>Address:</strong> {customer.address}</p>
          <p><strong>Phone:</strong> {customer.phone}</p>
        </div>
      )}
    </div>
  );
};

export default CustomerSearch;

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import '@patternfly/react-core/dist/styles/base.css';  // PatternFly styles

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

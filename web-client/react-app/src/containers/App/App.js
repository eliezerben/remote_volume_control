import React from 'react';
import styles from './App.module.css';
import Servers from '../../components/servers/Servers.js';

import { BACKEND_URL } from '../../utilities/Config.js';


class App extends React.Component {

  state = {
    servers: [],
  }

  componentDidMount = async () => {
    const endpoint = `${BACKEND_URL}/servers/`;
    const response = await fetch(endpoint, 
      {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
      }
    });
    const content = await response.json();
    this.setState({
      servers: content
    });
  }

  render() {
    return (
      <div className={styles.App}>
        <Servers servers={this.state.servers}/>
      </div>
    );
  }
}

export default App;

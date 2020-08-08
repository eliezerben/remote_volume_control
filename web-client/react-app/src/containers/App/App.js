import React from 'react';
import styles from './App.module.css';
import Servers from '../../components/servers/Servers.js';

class App extends React.Component {

  state = {
    servers: [
      {
        name: 'Home Computer',
        ip: '192.168.0.101'
      }
    ]
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

import React from 'react';
import Server from './server/Server.js';

function Servers({servers}) {

    return (
        <div>
            { servers.map((server, index) => <Server key={index} server={server}/>) }
        </div>
    )
}

export default Servers;
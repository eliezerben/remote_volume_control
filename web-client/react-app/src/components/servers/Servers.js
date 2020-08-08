import React from 'react';
import Server from './server/Server.js';

function Servers({servers}) {

    return (
        <div>
            { servers.map((server) => <Server server={server}/>) }
        </div>
    )
}

export default Servers;
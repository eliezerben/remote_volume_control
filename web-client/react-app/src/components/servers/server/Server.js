import React, {useState, useEffect} from 'react';

import 'material-design-icons/iconfont/material-icons.css';

import { Slider } from '@rmwc/slider';
import '@rmwc/slider/styles';

import { IconButton } from '@rmwc/icon-button';
import '@rmwc/icon-button/styles';

import { Elevation } from '@rmwc/elevation';
import '@rmwc/elevation/styles';

import styles from './Server.module.css';


function Server({server}) {

    const [volume, setVolume] = useState(0);
    const [mute, setMute] = useState(false);

    return (
        <Elevation z='3' wrap>
            <div className={styles.serverWrapper}>
                <div className={styles.header}>
                    <div className={styles.serverName}>{server.name}</div>
                    <div className={styles.serverIp}>({server.ip})</div>
                </div>
                <div className={styles.body}>
                    <div className={styles.volControlsRow}>
                        <div className={styles.volSlider}>
                            <Slider
                                min={0}
                                max={100}
                                discrete
                                step={1}
                                value={volume}
                                onChange={evt => setVolume(evt.detail.value)}
                                onInput={evt => setVolume(evt.detail.value)}
                            />
                        </div>
                        <IconButton
                            checked={mute}
                            onClick={() => setMute(!mute)}
                            icon='volume_up'
                            onIcon='volume_off'
                            className={styles.muteButton}
                        />
                    </div>
                </div>
            </div>
        </Elevation>
    );
}

export default Server;

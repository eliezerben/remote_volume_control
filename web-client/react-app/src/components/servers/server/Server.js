import React, {useState, useEffect, useRef} from 'react';

import VolumeControlApi from '../../../utilities/VolumeControlApi.js'

import 'material-design-icons/iconfont/material-icons.css';

import { Slider } from '@rmwc/slider';
import '@rmwc/slider/styles';

import { IconButton } from '@rmwc/icon-button';
import '@rmwc/icon-button/styles';

import { Elevation } from '@rmwc/elevation';
import '@rmwc/elevation/styles';

import { Typography } from '@rmwc/typography';
import '@rmwc/typography/styles';

import styles from './Server.module.css';

import { BACKEND_URL } from '../../../utilities/Config.js';


function Server({server}) {

    const [volume, setVolume] = useState(0);
    const [mute, setMute] = useState(false);

    const volControlApi = useRef(new VolumeControlApi(BACKEND_URL, server.ip));
    const curVolumeTimeoutId = useRef(null);

    useEffect(() => {
        volControlApi.current.getVol().then(volResponse => {
            if (volResponse !== null) {
                setVolume(volResponse);
            }
        });
        volControlApi.current.getMute().then(muteResponse => {
            if (muteResponse !== null) {
                setMute(muteResponse);
            }
        });
    }, []);

    useEffect(() => {
        // Throttle frequency in which commands are sent to server
        if (curVolumeTimeoutId.current) {
            clearTimeout(curVolumeTimeoutId.current);
        }
        curVolumeTimeoutId.current = setTimeout(() => {
            volControlApi.current.setVol(volume);
            curVolumeTimeoutId.current = null;
        }, 200);
    }, [volume]);

    useEffect(() => {
        mute ?
        volControlApi.current.mute() :
        volControlApi.current.unmute();
    }, [mute]);

    return (
        <Elevation z='3' wrap>
            <div className={styles.serverWrapper}>
                <div className={styles.header}>
                    <Typography className={styles.serverName} use='body1'>{server.name}</Typography>
                    <Typography use='caption'>({server.ip})</Typography>
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

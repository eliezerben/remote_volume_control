
class VolumeControlApi {

    constructor(backendUrl, volControlServerIp) {
        this.backendUrl = backendUrl;
        this.volControlServerIp = volControlServerIp;
        this.volControlEndpoint = `${this.backendUrl}/servers/${this.volControlServerIp}/send-command/`;
    }

    post = async (endpoint, data_obj) => {
        const response = await fetch(
            endpoint,
            {
                // mode: 'no-cors',
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data_obj)
            }
        );
        const content = await response.json();
        return content;
    }

    get = async (endpoint) => {
        const response = await fetch(
            endpoint,
            {
                method: 'GET',
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
                }
            }
        );
        const content = await response.json();
        return content;
    } 

    setVol = async (vol) => {
        const data = {
            command: 'SET_VOL',
            value: vol.toString(),
        }
        return await this.post(this.volControlEndpoint, data);
    }

    getVol = async () => {
        const data = {
            command: 'GET_VOL',
            value: '',
        }
        const result = await this.post(this.volControlEndpoint, data);
        if (result.status === 'success') {
            return result.value;
        } else {
            return null;
        }
    }

    mute = async () => {
        const data = {
            command: 'MUTE',
            value: '',
        }
        return await this.post(this.volControlEndpoint, data);
    }

    unmute = async () => {
        const data = {
            command: 'UNMUTE',
            value: '',
        }
        return await this.post(this.volControlEndpoint, data);
    }

    getMute = async () => {
        const data = {
            command: 'GET_MUTE',
            value: '',
        }
        const result = await this.post(this.volControlEndpoint, data);
        if (result.status === 'success') {
            return Boolean(Number(result.value));
        } else {
            return null;
        }
    }

}

export default VolumeControlApi;

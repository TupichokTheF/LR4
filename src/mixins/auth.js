import axios from "axios";

export const authMixin = {
    methods: {
        async checkAuth() {
            await axios.get('http://localhost:8000/api/takeToken', {
                headers: {
                Authorization: "Bearer " + localStorage.getItem('access_token'),
            }
            }).then(response => (this.info = response.data)).catch(error => (this.refreshToken()))

            if ( this.info.status == "success" ) {
                this.token = true;
            }
        },

        async refreshToken() {
            await axios.post('http://localhost:8000/api/refresh', {
                refresh: localStorage.getItem('refresh_token'),
            }).then(response => (this.info = response.data)).catch(error => (this.token = false))
            
            if ( this.info != null ) {
                localStorage.setItem("access_token", this.info.access);
                this.token = true;
            }
        },
    }
};
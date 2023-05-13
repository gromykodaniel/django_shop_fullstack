import axios from 'axios';
import { getSession } from 'next-auth/react';
import {API_SERVER_URL} from '@/config.js';

const custom_axios = axios.create({
    baseURL: API_SERVER_URL,
    withCredentials: true,
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFToken",
    validateStatus: (status) => {
        return status >= 200 && status < 500
    },
});

custom_axios.interceptors.request.use(async (request) => {
    const session = await getSession();
    if (session) {
        request.headers.Authorization = `Bearer ${session.access}`;
    }
    return request;
});

async function fetchData(url) {
    const response = await custom_axios.get(url);
    return response.data;
};

export async function fetchAllData(url) {
    let results = [];
    let response = await fetchData(url);
    results = results.concat(response.results);
    
    while (response.next !== null) {
        response = await fetchData(response.next);
        results = results.concat(response.results);
    }
    return results;
};

export async function fetchPagesAmount(url) {
    let result = 0;
    let response = await fetchData(url);
    result += 1;
    
    while (response.next !== null) {
        response = await fetchData(response.next);
        result += 1;
    }
    return result;
};

export default custom_axios;
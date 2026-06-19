import axios from "axios";

export default axios.create({
    baseURL:
        "https://friendly-invention-xr5gvxgg7w9wc6wq7-8000.app.github.dev",
    headers: {
        "Content-Type": "application/json"
    }
});
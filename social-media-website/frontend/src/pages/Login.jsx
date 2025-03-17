import React from 'react';

const Login = () => {
    const handleLogin = (event) => {
        event.preventDefault();
        // Implement login logic here
    };

    return (
        <form onSubmit={handleLogin}>
            <input type=\"text\" placeholder=\"Username\" required />
            <input type=\"password\" placeholder=\"Password\" required />
            <button type=\"submit\">Login</button>
        </form>
    );
};

export default Login;

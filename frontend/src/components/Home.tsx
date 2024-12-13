import axios from 'axios';
import React from 'react'

const Home: React.FC = () =>{
    const handleGoogleLogin= async()=>{
        //user calls backend api fetch, backend sends google details to frontend alongside a access token
        try{
            const url = "http://127.0.0.1:8000/api/auth/google/login/";
            const response = await axios.get(url);
            if (response.status === 200) {
                window.location.href = response.data.redirect_url; // Redirect user to Google login page
            } else {
                console.error("Failed to start Google login:", response);
            }
            
        }catch(err){
            console.log(err);
            throw err;
        }
    }
    return (<>
        <div className='d-flex flex-column justify-content-center align-items-center vh-100'>
            <h6>Ranked Studying</h6>  
            <p className='w-50 text-center'>Have no motivation to study? Do you have a competitive drive? Try ranked studying with friends!</p> 
            <button className='btn-container' onClick={handleGoogleLogin}>
                <div className='d-flex flex-row align-items-center text-start gap-2 ps-1'>
                    <img className="btn-logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Google_%22G%22_logo.svg/1200px-Google_%22G%22_logo.svg.png"/>
                    Login with Google
                </div>
            </button>
            <button className='btn-container mt-2'>
                <div className='d-flex flex-row align-items-center text-start gap-2 ps-1'>
                    <img className='btn-logo ' src="https://static.cdnlogo.com/logos/d/64/discord.png"/>
                    Login with Discord
                </div>
            </button>
        </div>
    </>);
}

export default Home;
import React, {useEffect, useRef, useState} from "react";
import { fetchData } from "../utility/APIManager";

interface UserData {
    id: number;
    username: string;
    email: string;
    first_name: string;
    last_name: string;
    profile_picture?: string;
}


const Dashboard:React.FC = ()=>{
    const [userData, setUserData] = useState<UserData | null>(null);
    const executeOnce = useRef(false); 
    useEffect(()=>{
        if (executeOnce.current) return;
        executeOnce.current = true; 
        const accessToken = localStorage.getItem('access_token');
        if (!accessToken) {
            throw new Error('Access token not found. Please log in again.');
          }
        const fetchUserData = async()=>{
            const url = "http://localhost:8000/api/user"
            const response = await fetchData(url, accessToken);
            setUserData(response);
        }
        fetchUserData();
    },[]);
    return(<>
     <div className='d-flex flex-row justify-content-center align-items-center vh-100 gap-5'>
        <div className="border">
            user profile box
        </div>   
        <div className="border">
            user inventory box 
        </div>   
    </div>
    </>);
}

export default Dashboard;
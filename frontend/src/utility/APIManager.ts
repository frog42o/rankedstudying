import axios from "axios";


export const fetchData = async<T = any>(url:string, accessToken:string)=>{
    if(!accessToken) return;
    try{
        const response = await axios.get<T>(url,{
            headers: {
                Authorization: `Bearer ${accessToken}`, 
              },
            }
        );
        return response.data;
        
    }catch(err){
        console.log(err);
        throw err;
    }
}
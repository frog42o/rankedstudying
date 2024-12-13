import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import CallBack from './components/authentication/Callback';
import Dashboard from './components/Dashboard';
function App() {
  return (
    <>
      <Router>
        <div>
          <Routes>
            <Route path ='/' element={<Home/>}/>
            <Route path ='/auth/success' element={<CallBack/>}/>
            <Route path ='/dashboard' element={<Dashboard/>}/>
          </Routes>
        </div>
      </Router>
    </>
  )
}

export default App

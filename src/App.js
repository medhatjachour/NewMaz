import React from 'react';
import { Routes, Route } from "react-router-dom";

import PrimarySearchAppBar from './components/MainNavBar'
import Home from './pages/Home'
import ProductPage from './pages/ProductPage'

function App() {
  return (
    <div className="App">
      
      <PrimarySearchAppBar/>
      <Routes>
        <Route index element={<Home />} />
        {/*<Route path="/ProductPage/:id" element={<ProductPage />} />*/}
      </Routes>
    </div>
  );
}

export default App;

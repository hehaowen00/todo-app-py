import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

import App from './App';
import Login from './views/Login';
import Home from './views/Home';
import Collection from './views/Collection';
import List from './views/List';
import Item from './views/Item';

import reportWebVitals from './reportWebVitals';

import { BrowserRouter, Route, Routes } from 'react-router-dom';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <BrowserRouter>
    <Routes>
      <Route path='/login' element={<Login />} />
      <Route path='/home' element={<Home />} />
      <Route path='/collection/:id' element={<Collection />} />
      <Route path='/list/:id' element={<List />} />
      <Route path='/item/:id' element={<Item />} />
      <Route path='*' element={<App />} />
    </Routes>
  </BrowserRouter>
);

reportWebVitals();

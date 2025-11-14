import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import HomePage from '@/pages/HomePage';
import PreRegistrationForm from '@/pages/PreRegistrationForm';
import CoordinatorLogin from '@/pages/CoordinatorLogin';
import CoordinatorDashboard from '@/pages/CoordinatorDashboard';

function App() {
  return (
    <Router 
      future={{
        v7_startTransition: true,
        v7_relativeSplatPath: true
      }}
    >
      <div className="min-h-screen">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/preinscripcion" element={<PreRegistrationForm />} />
          <Route path="/coordinador/login" element={<CoordinatorLogin />} />
          <Route path="/coordinador/dashboard/*" element={<CoordinatorDashboard />} />
          <Route path="/dashboard/*" element={<CoordinatorDashboard />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Customizer from "./pages/Customizer";
import Result from "./pages/Result";
import Navbar from "./components/Navbar";

export default function App() {
  return (
    <BrowserRouter>
      <div className="app">
        <Navbar />

        <div className="page-container">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/customizer" element={<Customizer />} />
            <Route path="/result" element={<Result />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}
import { useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();

  return (
    <div className="navbar">
      <div className="logo">🎨 Customizer</div>

      <div className="nav-links">
        <button onClick={() => navigate("/")}>Home</button>
        <button onClick={() => navigate("/customizer")}>Design</button>
        <button onClick={() => navigate("/login")}>Admin</button>
      </div>
    </div>
  );
}
import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="container">
      <h1>Product Customizer</h1>

      <button onClick={() => navigate("/customizer")}>
        Try Now
      </button>

      <br />

      <button onClick={() => navigate("/login")}>
        Admin Login
      </button>
    </div>
  );
}
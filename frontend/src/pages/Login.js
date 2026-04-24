export default function Login() {
  const handleLogin = () => {
    window.location.href = "http://127.0.0.1:8000/admin/";
  };

  return (
    <div className="container">
      <h2>Admin Login</h2>
      <button onClick={handleLogin}>Go to Admin</button>
    </div>
  );
}
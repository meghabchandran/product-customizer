import { useLocation, useNavigate } from "react-router-dom";

export default function Result() {
  const location = useLocation();
  const navigate = useNavigate();

  const image = location.state?.image;
  const url = image ? `http://127.0.0.1:8000${image}` : null;

  return (
    <div className="result-container">

      <h2>✨ Generated Result</h2>

      <div className="result-box">
        {url ? (
          <img src={url} alt="result" />
        ) : (
          <p>No image found</p>
        )}
      </div>

      <button
        className="download-btn"
        onClick={() => {
          const a = document.createElement("a");
          a.href = url;
          a.download = "result.png";
          a.click();
        }}
      >
        ⬇ Download
      </button>

      <button onClick={() => navigate("/")}>
        🏠 Back Home
      </button>

    </div>
  );
}
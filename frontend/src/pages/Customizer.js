import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function Customizer() {
  const [products, setProducts] = useState([]);
  const [selected, setSelected] = useState("");
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);

  const navigate = useNavigate();

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/products/")
      .then(res => res.json())
      .then(data => setProducts(data));
  }, []);

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("product", selected);
    formData.append("design", file);

    const res = await fetch("http://127.0.0.1:8000/api/render/", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    navigate("/result", { state: data });
  };

  return (
    <div className="container">
      <h2>Design Your Product</h2>

      <div className="grid">
        {/* LEFT PANEL */}
        <div className="card">
          <h3>Select Product</h3>

          <select onChange={(e) => setSelected(e.target.value)}>
            <option value="">Choose product</option>
            {products.map(p => (
              <option key={p.id} value={p.id}>{p.name}</option>
            ))}
          </select>

          <h3>Upload Design</h3>
          <input
            type="file"
            onChange={(e) => {
              setFile(e.target.files[0]);
              setPreview(URL.createObjectURL(e.target.files[0]));
            }}
          />

          <button onClick={handleSubmit}>
            Generate Preview
          </button>
        </div>

        {/* RIGHT PANEL */}
        <div className="card">
          <h3>Preview</h3>

          {preview ? (
            <img src={preview} alt="preview" />
          ) : (
            <p>No design uploaded yet</p>
          )}
        </div>
      </div>
    </div>
  );
}
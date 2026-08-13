import { useState } from "react";
import "./UploadBox.css";

function UploadBox({ setFile }) {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];

    if (file) {
      setSelectedFile(file);
      setFile(file);
    }
  };

  return (
    <label className="upload-box">
      <input
        type="file"
        accept=".pdf"
        onChange={handleFileChange}
        hidden
      />

      <div className="upload-content">
        <div className="pdf-icon">📄</div>

        <h2>Upload Your Resume</h2>

        {selectedFile ? (
          <div className="selected-file">
            <p>Selected Resume:</p>
            <strong>📄 {selectedFile.name}</strong>
          </div>
        ) : (
          <p>
            Drag & Drop your PDF here
            <br />
            or click to browse
          </p>
        )}

        <span className="browse-btn">
          {selectedFile ? "Change PDF" : "Choose PDF"}
        </span>
      </div>
    </label>
  );
}

export default UploadBox;
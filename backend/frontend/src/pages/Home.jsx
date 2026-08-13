import { useState } from "react";
import API from "../services/api";

import UploadBox from "../components/UploadBox";
import Loading from "../components/Loading";
import ATSCard from "../components/ATSCard";

import "../styles/Home.css";

function Home() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const uploadResume = async () => {
    if (!file) {
      alert("Please select a PDF");
      return;
    }

    try {
      const formData = new FormData();
      formData.append("file", file);

      setLoading(true);
      setResult(null);

      const response = await API.post(
        "/resume/upload",
        formData
      );

      console.log("Backend response:", response.data);
      console.log("Analysis result:", response.data.analysis);

      setResult(response.data.analysis);

    } catch (error) {
      console.error("Resume analysis error:", error);

      alert(
        error.response?.data?.detail ||
        "Something went wrong while analyzing the resume."
      );

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="home">

      <div className="container">

        <div className="header">

          <div className="brand-badge">
            ✨ AI POWERED RESUME ANALYZER
          </div>

          <h1>
            🤖 Roshani AI Resume Analyzer
          </h1>

          <p className="subtitle">
            Analyze Resume Using{" "}
            <strong>Google Gemini AI</strong>
          </p>

          <p className="description">
            Upload your resume and get an AI-powered ATS score,
            strengths, missing skills and personalized suggestions.
          </p>

        </div>

        <div className="upload-section">

          <div className="section-label">
            <span>1</span>
            Upload Your Resume
          </div>

          <UploadBox setFile={setFile} />

          {file && (
            <div className="file-selected">
              📄
              <span>
                Selected: <strong>{file.name}</strong>
              </span>
            </div>
          )}

        </div>

        <button
          className="btn"
          onClick={uploadResume}
          disabled={loading}
        >
          {loading ? "⏳ Analyzing Resume..." : "🚀 Analyze Resume"}
        </button>

        {loading && <Loading />}

        {result && <ATSCard result={result} />}

      </div>

    </div>
  );
}

export default Home;
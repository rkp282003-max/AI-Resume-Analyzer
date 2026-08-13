function ATSCard({ result }) {
  const score = Number(result?.ats_score) || 0;

  return (
    <div className="result">

      {/* ATS SCORE */}
      <div className="card ats-card">
        <h2>ATS Score</h2>

        <div
          className="score"
          style={{
            "--score": `${score}%`
          }}
        >
          <div className="score-inner">
            <div className="score-number">
              {score}
            </div>

            <div className="score-total">
              /100
            </div>
          </div>
        </div>
      </div>


      {/* SUMMARY */}
      <div className="card">
        <h2>Summary</h2>

        <p>
          {result?.summary || "No summary available."}
        </p>
      </div>


      {/* STRENGTHS */}
      <div className="card">
        <h2>Strengths</h2>

        <ul>
          {result?.strengths?.map((item, index) => (
            <li key={index}>
              {item}
            </li>
          ))}
        </ul>
      </div>


      {/* MISSING SKILLS */}
      <div className="card">
        <h2>Missing Skills</h2>

        <ul>
          {result?.missing_skills?.map((item, index) => (
            <li key={index}>
              {item}
            </li>
          ))}
        </ul>
      </div>


      {/* SUGGESTIONS */}
      <div className="card">
        <h2>Suggestions</h2>

        <ul>
          {result?.suggestions?.map((item, index) => (
            <li key={index}>
              {item}
            </li>
          ))}
        </ul>
      </div>

    </div>
  );
}

export default ATSCard;
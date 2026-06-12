import { useState } from "react";
import axios from "axios";

function App() {

  const [resumeSkills, setResumeSkills] = useState("");
  const [jdText, setJdText] = useState("");
  const [result, setResult] = useState(null);

  const analyzeResume = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/analyze-resume",
        {
          resume_skills: resumeSkills
            .split(",")
            .map(skill => skill.trim()),

          jd_text: jdText
        }
      );

      setResult(response.data);

    } catch (error) {

      console.error("Error:", error);

      alert("Failed to connect to backend");

    }

  };

  return (
    <div style={{ padding: "20px" }}>

      <h1>AI Career Assistant</h1>

      <h3>Resume Skills</h3>

      <textarea
        rows="5"
        cols="50"
        value={resumeSkills}
        onChange={(e) => setResumeSkills(e.target.value)}
        placeholder="Python, AWS, React"
      />

      <h3>Job Description</h3>

      <textarea
        rows="5"
        cols="50"
        value={jdText}
        onChange={(e) => setJdText(e.target.value)}
        placeholder="Looking for Python AWS React Docker developer"
      />

      <br />
      <br />

      <button onClick={analyzeResume}>
        Analyze
      </button>

      <br />
      <br />

      {result && (

        <div>

          <h2>
            Match Score: {result.match_score}%
          </h2>

          <h3>Matched Skills</h3>

          <ul>
            {result.matched_skills.map((skill, index) => (
              <li key={index}>
                {skill}
              </li>
            ))}
          </ul>

          <h3>Missing Skills</h3>

          <ul>
            {result.missing_skills.map((skill, index) => (
              <li key={index}>
                {skill}
              </li>
            ))}
          </ul>

          <h3>Recommendations</h3>

          <ul>
            {result.recommendations.map((item, index) => (
              <li key={index}>
                {item}
              </li>
            ))}
          </ul>

        </div>

      )}

    </div>
  );
}

export default App;
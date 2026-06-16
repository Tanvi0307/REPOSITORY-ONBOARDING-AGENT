import axios from "axios";

const API_URL = "http://localhost:8000";

export const analyzeRepo = async (url) => {
  const response = await axios.post(
    `${API_URL}/analyze`,
    { url }
  );

  return response.data;
};

export const chatWithRepo = async (
  question,
  repoData
) => {
  const response = await axios.post(
    `${API_URL}/chat`,
    {
      question,
      repo_data: repoData,
    }
  );

  return response.data.answer;
};
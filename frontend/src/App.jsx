import { useState } from "react";
import {
  Globe,
  Search,
  Rocket,
  Bot,
  Send,
  FileText,
  FolderTree,
  BookOpen,
} from "lucide-react";

import { ClipLoader } from "react-spinners";
import {
  analyzeRepo,
  chatWithRepo
} from "./api";

function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: "Hi! I'm your repository assistant. Ask me anything about the repository.",
    },
  ]);

  const [question, setQuestion] = useState("");

  const submit = async () => {
    if (!url) return;

    setLoading(true);

    try {
      const data = await analyzeRepo(url);
      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Unable to analyze repository.");
    } finally {
      setLoading(false);
    }
  };

 const sendMessage = async () => {
  if (!question.trim() || !result) return;

  const userQuestion = question;

  setMessages((prev) => [
    ...prev,
    {
      role: "user",
      text: userQuestion,
    },
  ]);

  setQuestion("");

  try {
    const answer = await chatWithRepo(
      userQuestion,
      result
    );

    setMessages((prev) => [
      ...prev,
      {
        role: "assistant",
        text: answer,
      },
    ]);
  } catch (error) {
    console.error(error);

    setMessages((prev) => [
      ...prev,
      {
        role: "assistant",
        text: "Sorry, I couldn't answer that question.",
      },
    ]);
  }
};

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        {/* Header */}

        <div className="mb-10 text-center">
          <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-purple-400/20 bg-purple-500/10 px-4 py-2">
            <Rocket size={16} className="text-purple-300" />
            <span className="text-sm text-purple-200">
              AI-Powered Repository Insights
            </span>
          </div>

          <h1 className="mb-4 text-5xl font-bold md:text-7xl">
            Repository Onboarding Agent
          </h1>

          <p className="text-lg text-slate-300">
            Understand any GitHub repository in seconds
          </p>
        </div>

        {/* Search */}

        <div className="mb-10 flex flex-col gap-4 md:flex-row">
          <div className="relative flex-1">
            <Globe
  size={20}
  className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"
/>

            <input
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="https://github.com/facebook/react"
              className="w-full rounded-2xl border border-white/10 bg-white/5 py-4 pl-12 pr-4 outline-none backdrop-blur-md"
            />
          </div>

          <button
            onClick={submit}
            disabled={loading}
            className="flex items-center justify-center gap-2 rounded-2xl bg-gradient-to-r from-fuchsia-500 to-violet-600 px-8 py-4 font-semibold transition hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? (
              <ClipLoader size={18} color="white" />
            ) : (
              <>
                <Search size={18} />
                Analyze
              </>
            )}
          </button>
        </div>

        {/* Main Content */}

        {result && (
          <div className="grid gap-6 lg:grid-cols-3">
            {/* Left Section */}

            <div className="space-y-6 lg:col-span-2">
              {/* Summary */}

              <section className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-md">
                <h2 className="mb-4 flex items-center gap-2 text-2xl font-bold">
                  <FileText />
                  Summary
                </h2>

                <p className="leading-8 text-slate-300">
                  {result.summary}
                </p>
              </section>

              {/* Important Files */}

              <section className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-md">
                <h2 className="mb-6 flex items-center gap-2 text-2xl font-bold">
                  <FolderTree />
                  Important Files
                </h2>

                <div className="flex flex-wrap gap-3">
                  {result.important_files?.map((file) => (
                    <span
                      key={file}
                      className="rounded-xl border border-purple-400/20 bg-purple-500/10 px-4 py-2 text-sm"
                    >
                      {file}
                    </span>
                  ))}
                </div>
              </section>

              {/* Learning Path */}

              <section className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-md">
                <h2 className="mb-6 flex items-center gap-2 text-2xl font-bold">
                  <BookOpen />
                  Learning Path
                </h2>

                <div className="space-y-4">
                  {result.learning_path?.map((step, index) => (
                    <div key={index} className="flex gap-4">
                      <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-violet-600 font-semibold">
                        {index + 1}
                      </div>

                      <p className="text-slate-300">{step}</p>
                    </div>
                  ))}
                </div>
              </section>
            </div>

            {/* Chat Panel */}

            <div className="flex h-[700px] flex-col rounded-3xl border border-white/10 bg-white/5 backdrop-blur-md">
              <div className="flex items-center gap-3 border-b border-white/10 p-5">
                <Bot className="text-violet-400" />

                <div>
                  <h3 className="font-semibold">Repo Assistant</h3>

                  
                </div>
              </div>

              <div className="flex-1 space-y-4 overflow-y-auto p-5">
                {messages.map((message, index) => (
                  <div
                    key={index}
                    className={`max-w-[90%] rounded-2xl p-3 ${
                      message.role === "user"
                        ? "ml-auto bg-gradient-to-r from-fuchsia-500 to-violet-600"
                        : "bg-slate-800/80"
                    }`}
                  >
                    {message.text}
                  </div>
                ))}
              </div>

              <div className="flex gap-2 border-t border-white/10 p-4">
                <input
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                  placeholder="Ask about this repository..."
                  className="flex-1 rounded-xl bg-slate-900/80 px-4 py-3 outline-none"
                  onKeyDown={(e) => {
                    if (e.key === "Enter") sendMessage();
                  }}
                />

                <button
                  onClick={sendMessage}
                  className="rounded-xl bg-gradient-to-r from-fuchsia-500 to-violet-600 p-3"
                >
                  <Send size={18} />
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
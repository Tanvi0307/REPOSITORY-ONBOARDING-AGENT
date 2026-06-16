import { Bot, Send } from "lucide-react";
import { useState } from "react";

export default function ChatPanel({ data }) {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: "Hi! Ask me anything about this repository."
    }
  ]);

  const [input, setInput] = useState("");

  const sendMessage = () => {
    if (!input) return;

    const answer = data.summary;

    setMessages([
      ...messages,
      { role: "user", text: input },
      { role: "assistant", text: answer }
    ]);

    setInput("");
  };

  return (
    <div className="rounded-3xl border border-white/10 bg-white/5 backdrop-blur-md">

      <div className="flex items-center gap-3 border-b border-white/10 p-5">
        <Bot className="text-violet-400" />

        <div>
          <h3 className="font-semibold">Repo Assistant</h3>

          
        </div>
      </div>

      <div className="h-[500px] overflow-y-auto p-5 space-y-4">

        {messages.map((message, index) => (
          <div
            key={index}
            className={`max-w-[85%] rounded-2xl p-3 ${
              message.role === "user"
                ? "ml-auto bg-fuchsia-600"
                : "bg-slate-800"
            }`}
          >
            {message.text}
          </div>
        ))}

      </div>

      <div className="flex gap-2 border-t border-white/10 p-4">

        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about this repository..."
          className="flex-1 rounded-xl bg-slate-800 px-4 py-3 outline-none"
        />

        <button
          onClick={sendMessage}
          className="rounded-xl bg-violet-600 p-3"
        >
          <Send size={18} />
        </button>

      </div>

    </div>
  );
}
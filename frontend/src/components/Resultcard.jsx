import {
  BookOpen,
  FileText,
  FolderTree
} from "lucide-react";

export default function ResultCard({ data }) {
  return (
    <div className="space-y-6">

      <section className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-md">
        <h2 className="mb-4 flex items-center gap-2 text-2xl font-bold">
          <FileText />
          Summary
        </h2>

        <p className="text-slate-300 leading-8">
          {data.summary}
        </p>
      </section>

      <section className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-md">
        <h2 className="mb-6 flex items-center gap-2 text-2xl font-bold">
          <FolderTree />
          Important Files
        </h2>

        <div className="flex flex-wrap gap-3">
          {data.important_files.map((file) => (
            <span
              key={file}
              className="rounded-xl bg-violet-700/40 px-4 py-2"
            >
              {file}
            </span>
          ))}
        </div>
      </section>

      <section className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-md">
        <h2 className="mb-6 flex items-center gap-2 text-2xl font-bold">
          <BookOpen />
          Learning Path
        </h2>

        <ol className="space-y-4">
          {data.learning_path.map((step, index) => (
            <li key={index} className="flex gap-4">
              <div className="flex h-8 w-8 items-center justify-center rounded-full bg-violet-600">
                {index + 1}
              </div>

              <p className="text-slate-300">
                {step}
              </p>
            </li>
          ))}
        </ol>
      </section>

    </div>
  );
}
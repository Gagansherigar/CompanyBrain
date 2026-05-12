import { useState } from "react";

import axios from "axios";

import {
  Users,
  AlertTriangle,
  Briefcase,
  Activity,
  BrainCircuit
} from "lucide-react";

import {
  FaSlack
} from "react-icons/fa";


function App() {

  const [question, setQuestion] = useState("");

  const [loading, setLoading] = useState(false);

  const [response, setResponse] = useState(null);


  function getSourceIcon(source) {

    switch (source) {

      case "slack":
        return <FaSlack size={16} />;

      case "meeting":
        return <Users size={16} />;

      case "support_ticket":
        return <AlertTriangle size={16} />;

      case "crm":
        return <Briefcase size={16} />;

      default:
        return <Activity size={16} />;
    }
  }


  async function askQuestion() {

  if (!question) return;

  setLoading(true);

  setResponse(null);

  try {

    const res = await axios.post(
      "http://127.0.0.1:8000/chat",
      {
        question: question
      }
    );

    const uniqueEvidence = [];

    const seen = new Set();

    for (const item of res.data.evidence) {

      if (!seen.has(item.content)) {

        seen.add(item.content);

        uniqueEvidence.push(item);
      }
    }

    const fullAnswer = res.data.answer;

    let currentText = "";

    setResponse({
      ...res.data,
      answer: ""
    });

    for (let i = 0; i < fullAnswer.length; i++) {

      currentText += fullAnswer[i];

      setResponse(prev => ({
        ...prev,
        answer: currentText,
        evidence: uniqueEvidence
      }));

      await new Promise(resolve =>
        setTimeout(resolve, 8)
      );
    }

  } catch (error) {

    console.error(error);

    alert("Request failed");

  } finally {

    setLoading(false);
  }
}


  return (

    <div className="min-h-screen bg-[#FFF7ED] text-[#1D1C1D] p-10">

      <div className="max-w-6xl mx-auto">

        <div className="
          flex
          items-center
          gap-4
          mb-2
        ">

          <div className="
            bg-orange-500
            text-white
            p-3
            rounded-2xl
            shadow-md
          ">

            <BrainCircuit size={34} />

          </div>

          <h1 className="text-5xl font-bold">
            Organizational Intelligence
          </h1>

        </div>

        <p className="text-gray-500 mb-10">
          AI-powered organizational memory and reasoning platform
        </p>

        <div className="
          bg-white
          p-6
          rounded-2xl
          border
          border-orange-100
          shadow-sm
        ">

          <div className="mb-6">

            <p className="text-gray-500 mb-3">
              Suggested Questions
            </p>

            <div className="flex flex-wrap gap-3">

              {
                [
                  "Why are deployment failures increasing?",
                  "What customer complaints are recurring?",
                  "How are infrastructure issues affecting enterprise customers?",
                  "Summarize operational risks in 5 lines"
                ].map((suggestion, index) => (

                  <button
                    key={index}
                    onClick={() => setQuestion(suggestion)}
                    className="
                      bg-orange-100
                      hover:bg-orange-200
                      border
                      border-orange-200
                      px-4
                      py-2
                      rounded-xl
                      text-sm
                      transition
                    "
                  >
                    {suggestion}
                  </button>

                ))
              }

            </div>

          </div>

          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask organizational questions..."
            className="
              w-full
              h-32
              bg-orange-50
              border
              border-orange-200
              rounded-xl
              p-4
              text-black
              outline-none
              resize-none
            "
          />

          <button
            onClick={askQuestion}
            disabled={loading}
            className="
              mt-4
              bg-orange-500
              hover:bg-orange-600
              text-white
              px-6
              py-3
              rounded-xl
              font-semibold
              shadow-sm
              transition
            "
          >

            {
              loading
                ? "Analyzing Organizational Memory..."
                : "Ask Agent"
            }

          </button>

        </div>

        {
          response && (

            <div className="mt-10">

              <div className="
                bg-white
                border
                border-orange-100
                rounded-2xl
                p-6
                shadow-sm
              ">

                <h2 className="text-2xl font-bold mb-4">
                  Agent Answer
                </h2>

                <p className="
                  text-gray-700
                  whitespace-pre-wrap
                  leading-7
                ">
                  {response.answer}
                </p>

              </div>

              <div className="mt-8">

                <h2 className="text-2xl font-bold mb-4">
                  Selected Sources
                </h2>

                <div className="
                  flex
                  gap-3
                  flex-wrap
                ">

                  {
                    response.selected_sources.map(
                      (source, index) => (

                        <div
                          key={index}
                          className="
                            bg-white
                            px-4
                            py-2
                            rounded-xl
                            border
                            border-orange-100
                            flex
                            items-center
                            gap-2
                            shadow-sm
                          "
                        >

                          {getSourceIcon(source)}

                          {source}

                        </div>

                      )
                    )
                  }

                </div>

              </div>

              <div className="mt-10">

                <div className="
                  bg-white
                  border
                  border-orange-100
                  rounded-2xl
                  p-6
                  mb-8
                  shadow-sm
                ">

                  <h3 className="
                    text-xl
                    font-bold
                    mb-5
                  ">
                    Organizational Timeline
                  </h3>

                  <div className="
                    space-y-5
                    border-l
                    border-orange-200
                    pl-6
                  ">

                    {
                      response.evidence.slice(0, 4).map(
                        (memory, index) => (

                          <div
                            key={index}
                            className="relative"
                          >

                            <div className="
                              absolute
                              -left-[31px]
                              top-1
                              w-3
                              h-3
                              rounded-full
                              bg-orange-500
                            " />

                            <div className="
                              text-sm
                              text-gray-500
                              mb-1
                            ">
                              {memory.metadata.source}
                            </div>

                            <div className="
                              font-semibold
                              mb-2
                            ">
                              {memory.metadata.memory_type}
                            </div>

                            <p className="
                              text-gray-700
                              text-sm
                            ">
                              {
                                memory.content.slice(
                                  0,
                                  160
                                )
                              }...
                            </p>

                          </div>

                        )
                      )
                    }

                  </div>

                </div>

                <h2 className="
                  text-2xl
                  font-bold
                  mb-4
                ">
                  Organizational Evidence
                </h2>

                <div className="space-y-4">

                  {
                    response.evidence.map(
                      (memory, index) => (

                        <div
                          key={index}
                          className="
                            bg-white
                            border
                            border-orange-100
                            rounded-2xl
                            p-5
                            shadow-sm
                          "
                        >

                          <div className="
                            flex
                            gap-3
                            flex-wrap
                            mb-4
                          ">

                            <div className="
                              bg-orange-500
                              text-white
                              px-3
                              py-1
                              rounded-lg
                              text-sm
                              flex
                              items-center
                              gap-2
                            ">

                              {
                                getSourceIcon(
                                  memory.metadata.source
                                )
                              }

                              {
                                memory.metadata.source
                              }

                            </div>

                            <div className="
                              bg-orange-400
                              text-white
                              px-3
                              py-1
                              rounded-lg
                              text-sm
                            ">
                              {
                                memory.metadata.memory_type
                              }
                            </div>

                            <div className="
                              bg-orange-600
                              text-white
                              px-3
                              py-1
                              rounded-lg
                              text-sm
                            ">
                              priority:
                              {" "}
                              {
                                memory.metadata.priority
                              }
                            </div>

                          </div>

                          <div className="mb-4">

                            <div className="
                              flex
                              items-center
                              gap-2
                              mb-3
                            ">

                              <div className="
                                text-xs
                                text-gray-500
                              ">
                                Confidence:
                              </div>

                              <div className="
                                text-xs
                                px-2
                                py-1
                                rounded-md
                                bg-orange-500
                                text-white
                              ">

                                {
                                  memory.score > 0.7
                                    ? "High"
                                    : memory.score > 0.5
                                    ? "Medium"
                                    : "Low"
                                }

                              </div>

                            </div>

                            <p className="
                              text-gray-700
                              leading-7
                            ">
                              {memory.content}
                            </p>

                          </div>

                          <div className="
                            flex
                            gap-2
                            flex-wrap
                          ">

                            {
                              memory.metadata.tags?.map(
                                (tag, idx) => (

                                  <div
                                    key={idx}
                                    className="
                                      bg-orange-100
                                      text-orange-700
                                      px-2
                                      py-1
                                      rounded-md
                                      text-xs
                                    "
                                  >
                                    #{tag}
                                  </div>

                                )
                              )
                            }

                          </div>

                        </div>

                      )
                    )
                  }

                </div>

              </div>

            </div>

          )
        }

      </div>

    </div>

  );
}

export default App;
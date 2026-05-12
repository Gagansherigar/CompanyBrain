def build_context(results):

    context = ""

    for result in results:

        context += result.payload["content"]

        context += "\n\n"

    return context
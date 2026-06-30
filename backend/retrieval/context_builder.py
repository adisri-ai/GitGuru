"""
context_builder.py

Builds context supplied to the LLM.
"""


class ContextBuilder:

    def build(
        self,
        documents: list
    ) -> str:
        """
        Convert retrieved chunks
        into prompt context.
        """

        contexts = []

        for doc in documents:

            source = (
                doc.metadata.get(
                    "source",
                    "Unknown"
                )
            )

            contexts.append(
                f"""
SOURCE:
{source}

CONTENT:
{doc.page_content}
"""
            )

        return "\n\n".join(contexts)
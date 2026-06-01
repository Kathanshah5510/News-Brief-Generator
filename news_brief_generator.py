from groq import Groq


def bullet_point_summary(client, text, num_points=5):
    """
    Summarize text into concise bullet points.
    """

    prompt = (
        f"Summarize the following text in "
        f"{num_points} concise bullet points:\n\n{text}"
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0.3,
        max_completion_tokens=300,
        messages=[
            {
                "role": "system",
                "content": "You are a concise and clear summarizer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def abstract_style_summary(client, text, sentence_count=5):
    """
    Summarize text as an academic abstract.
    """

    prompt = (
        f"Summarize the following text as a "
        f"{sentence_count}-sentence abstract:\n\n{text}"
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0.3,
        max_completion_tokens=300,
        messages=[
            {
                "role": "system",
                "content": "You are a concise and clear summarizer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def simple_english_summary(client, text, sentence_count=5):
    """
    Summarize text in simple English suitable for a 12-year-old.
    """

    prompt = (
        f"Summarize the following text in simple English suitable "
        f"for a 12-year-old, in {sentence_count} sentences:\n\n{text}"
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0.3,
        max_completion_tokens=300,
        messages=[
            {
                "role": "system",
                "content": "You are a kind teacher explaining things simply."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def main():

    api_key = input("Enter your Groq API key: ").strip()

    client = Groq(api_key=api_key)

    with open("article.txt", "r", encoding="utf-8") as file:
        article_text = file.read()

    bullet_summary = bullet_point_summary(
        client,
        article_text,
        num_points=5
    )

    abstract_summary = abstract_style_summary(
        client,
        article_text,
        sentence_count=5
    )

    simple_summary = simple_english_summary(
        client,
        article_text,
        sentence_count=5
    )

    print("\n" + "=" * 60)
    print("BULLET-POINT SUMMARY")
    print("=" * 60)
    print(bullet_summary)

    print("\n" + "=" * 60)
    print("ABSTRACT SUMMARY")
    print("=" * 60)
    print(abstract_summary)

    print("\n" + "=" * 60)
    print("SIMPLE ENGLISH SUMMARY")
    print("=" * 60)
    print(simple_summary)


if __name__ == "__main__":
    main()
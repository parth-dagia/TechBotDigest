from transformers import pipeline

# Initialize the summarizer pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    max_chunk = 500
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    
    summary = ""
    for chunk in chunks:
        # Calculate max_length safely (e.g., half the chunk length or capped at 130)
        max_len = min(130, max(15, len(chunk)//2))
        result = summarizer(chunk, max_length=max_len, min_length=10, do_sample=False)
        summary += result[0]['summary_text'] + " "
    return summary.strip()

# Example usage (optional for testing)
if __name__ == "__main__":
    article = """Your long article text here. This can be a few paragraphs describing the tech news article or blog post you want to summarize."""
    print("Summary:")
    print(summarize_text(article))

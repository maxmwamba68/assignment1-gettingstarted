def welcome_assignment_answers(question):
    # Using a dictionary for cleaner "case-like" implementation
    answers = {
        "Are encoding and encryption the same? - Yes/No": "No",
        "Is it possible to decrypt a message without a key? - Yes/No": "No",
        "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?": "pcap",
        "Is it possible to decode a message without a key? - Yes/No": "Yes",
        "Is a hashed message supposed to be un-hashed? - Yes/No": "No",
        "What is the SHA256 hashing value of your NYU email and use the answer in your code - ": "c6657f002b793eff45a324aad909a8f4963250df50144013f99a8aba188ae1ba",
        "Is MD5 a secured hashing algorithm? - Yes/No": "No",
        "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number": 5,
        "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number": 3
    }
    
    # .get() allows us to provide the default "else" message if the question isn't found
    return answers.get(question, "This is not my beautiful wife! This is not my beautiful car! How did I get here?")

if __name__ == "__main__":
    # Test a sample question
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(f"Question: {debug_question}")
    print(f"Answer: {welcome_assignment_answers(debug_question)}")
